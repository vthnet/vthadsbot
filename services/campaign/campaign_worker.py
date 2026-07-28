import asyncio

from datetime import datetime

from pyrogram import Client
from pyrogram.errors import FloodWait, RPCError

from sqlalchemy import select

from config import config
from loader import bot

from database.session import SessionLocal

from database.models.account import Account
from database.models.campaign import Campaign
from database.models.campaign_target import CampaignTarget
from database.models.user import User

running_campaigns = set()


async def process_campaign(
    campaign,
    session
):

    if campaign.id in running_campaigns:

        print(
            f"⚠️ Campaign #{campaign.id} already running"
        )

        return

    running_campaigns.add(
        campaign.id
    )

    app = None

    sent_count = 0
    failed_count = 0

    campaign.started_at = datetime.utcnow()

    await session.commit()

    try:

        print(
            f"🚀 Starting Campaign #{campaign.id}"
        )

        account_result = await session.execute(
            select(Account).where(
                Account.id == campaign.account_id
            )
        )

        account = account_result.scalar_one_or_none()

        if not account:

            print("❌ Account not found")

            campaign.running = False
            campaign.paused = False
            campaign.completed = True
            campaign.finished_at = datetime.utcnow()

            await session.commit()

            return

        user_result = await session.execute(
            select(User).where(
               User.id == account.user_id
            )
        )

        user = user_result.scalar_one_or_none()

        if not user:

          print("❌ User not found")

          return

        owner_id = user.telegram_id

        target_result = await session.execute(
            select(CampaignTarget).where(
                CampaignTarget.campaign_id == campaign.id
            )
        )

        targets = target_result.scalars().all()

        if not targets:

            campaign.running = False
            campaign.paused = False
            campaign.completed = True
            campaign.finished_at = datetime.utcnow()

            await session.commit()

            await bot.send_message(
                owner_id,
                "❌ Campaign cancelled because no target groups were found."
            )

            return

        app = Client(

            f"campaign_{campaign.id}",

            api_id=config.API_ID,

            api_hash=config.API_HASH,

            session_string=account.session_string,

            in_memory=True

        )

        await app.start()

        async for _ in app.get_dialogs():
            pass

        print("✅ Telegram Ready")

        loop_limit = (
            999999999
            if campaign.infinite
            else max(
                campaign.loop_count,
                1
            )
        )

        while (

            campaign.running

            and

            campaign.completed_loops < loop_limit

        ):
            await session.refresh(campaign)

            if campaign.paused:

                await asyncio.sleep(2)

                continue

            print(

                f"🔁 Loop "

                f"{campaign.completed_loops + 1}/"

                f"{'∞' if campaign.infinite else loop_limit}"

            )

            for target in targets:

                await session.refresh(campaign)

                if not campaign.running:
                    break

                if campaign.paused:
                    break

                try:

                    if campaign.media_path:

                        await app.send_photo(

                            chat_id=target.chat_id,

                            photo=campaign.media_path,

                            caption=campaign.post_data or ""

                        )

                    else:

                        await app.send_message(

                            chat_id=target.chat_id,

                            text=campaign.post_data

                        )

                    sent_count += 1

                    campaign.total_sent += 1

                    campaign.current_target = (

                        target.chat_title

                        or str(target.chat_id)

                    )

                    await session.commit()

                    print("-" * 50)

                    print(
                        f"📤 Sent : {target.chat_title or target.chat_id}"
                    )

                    print(
                        f"📊 Total Sent : {campaign.total_sent}"
                    )

                    print(
                        f"❌ Failed : {campaign.failed_sent}"
                    )

                    print("=" * 50)

                    await asyncio.sleep(
                        campaign.send_delay
                    )

                except FloodWait as e:

                    print(
                        f"⏳ FloodWait {e.value}s"
                    )

                    await asyncio.sleep(
                        e.value
                    )

                except RPCError as e:

                    failed_count += 1

                    campaign.failed_sent += 1

                    await session.commit()

                    print(
                        f"❌ Telegram Error: {e}"
                    )

                except Exception as e:

                    failed_count += 1

                    campaign.failed_sent += 1

                    await session.commit()

                    print(
                        f"❌ Send Error: {e}"
                    )

            campaign.completed_loops += 1

            remaining = (

                "∞"

                if campaign.infinite

                else max(

                    0,

                    loop_limit - campaign.completed_loops

                )

            )

            print(
                f"📊 Remaining Loops : {remaining}"
            )

            await session.commit()

            if (

                not campaign.infinite

                and campaign.completed_loops >= loop_limit

            ):

                break

            print("=" * 50)

            print(
                f"✅ Loop {campaign.completed_loops} Completed"
            )

            print(
                f"📊 Remaining Loops : {remaining}"
            )

            print("=" * 50)

            if campaign.repeat_delay >= 86400:

                delay_text = "24 Hour(s)"

            elif campaign.repeat_delay >= 3600:

                delay_text = f"{campaign.repeat_delay // 3600} Hour(s)"

            elif campaign.repeat_delay >= 60:

                delay_text = f"{campaign.repeat_delay // 60} Minute(s)"

            else:

                delay_text = f"{campaign.repeat_delay} Second(s)"

            print(
                f"⏳ Waiting {delay_text} before next loop..."
            )

            await session.refresh(campaign)

            if not campaign.running:
                break

            if campaign.paused:
                continue

            await asyncio.sleep(
                campaign.repeat_delay
            )


        campaign.finished_at = datetime.utcnow()
        campaign.current_target = "Completed"
        campaign.running = False
        campaign.paused = False
        campaign.completed = True

        await session.commit()

        runtime = campaign.finished_at - campaign.started_at


        await bot.send_message(
            owner_id,



            f"""
🎉 <b>Campaign Completed</b>

🆔 <code>{campaign.id}</code>

📤 Sent : {campaign.total_sent}
❌ Failed : {campaign.failed_sent}
👥 Groups : {len(targets)}
🔁 Loops : {"∞" if campaign.infinite else campaign.completed_loops}
⏱ Runtime : {str(runtime).split(".")[0]}

✅ Campaign Finished Successfully.
"""
        )

        print("=" * 50)

        print(
            f"✅ Campaign #{campaign.id} Completed"
        )

        print(
            f"📤 Total Sent : {sent_count}"
        )

        print(
            f"❌ Total Failed : {failed_count}"
        )

        print("=" * 50)

    except Exception as e:

        print(
            f"❌ Campaign Error #{campaign.id}: {e}"
        )

        campaign.finished_at = datetime.utcnow()
        campaign.current_target = "Error"
        campaign.running = False
        campaign.paused = False
        campaign.completed = True

        await session.commit()

    finally:

        running_campaigns.discard(
            campaign.id
        )

        if app:

            try:

                await app.stop()

            except Exception:

                pass


async def run_single_campaign(
  campaign_id: int
):

    async with SessionLocal() as session:

        result = await session.execute(
            select(Campaign).where(
                Campaign.id == campaign_id
            )
        )

        campaign = result.scalar_one_or_none()

        if not campaign:

            print(
                f"❌ Campaign {campaign_id} not found"
            )

            return

        await process_campaign(
            campaign,
            session
        )


async def run_campaigns():

    print(
        "🚀 Campaign Worker Started"
    )

    while True:

        try:

            async with SessionLocal() as session:

                result = await session.execute(
                    select(Campaign).where(
                        Campaign.running.is_(True)
                    )
                )

                campaigns = result.scalars().all()

                for campaign in campaigns:

                    if campaign.id not in running_campaigns:

                        asyncio.create_task(
                            run_single_campaign(
                                campaign.id
                            )
                        )

        except Exception as e:

            print(
                "❌ Worker Error:",
                e
            )

        await asyncio.sleep(3)