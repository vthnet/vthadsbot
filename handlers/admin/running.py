from aiogram import Router
from aiogram.filters import Command

from sqlalchemy import select

from database.session import SessionLocal
from database.models.user import User
from database.models.account import Account
from database.models.campaign import Campaign

router = Router()


@router.message(Command("running"))
async def running_campaigns(message):

    async with SessionLocal() as session:

        result = await session.execute(
            select(Campaign).where(
                Campaign.running == True
            )
        )

        campaigns = result.scalars().all()

        if not campaigns:

            await message.answer(
                "✅ No campaigns are currently running."
            )

            return

        text = (
            "🚀 <b>LIVE RUNNING CAMPAIGNS</b>\n\n"
            f"Total Running: <b>{len(campaigns)}</b>\n\n"
        )

        for campaign in campaigns:

            account = await session.get(
                Account,
                campaign.account_id
            )

            user = None

            if account:

                user = await session.get(
                    User,
                    account.user_id
                )

            text += (
                "━━━━━━━━━━━━━━\n\n"
                f"🆔 <b>Campaign #{campaign.id}</b>\n\n"
                f"👤 User : <b>{user.first_name if user else 'Unknown'}</b>\n"
                f"📱 Account : <b>{account.account_name if account else 'Unknown'}</b>\n"
                f"🎯 Current : <b>{campaign.current_target or 'Starting...'}</b>\n"
                f"📤 Sent : <b>{campaign.total_sent}</b>\n"
                f"❌ Failed : <b>{campaign.failed_sent}</b>\n"
                f"🔁 Loop : <b>{'∞' if campaign.infinite else f'{campaign.completed_loops}/{campaign.loop_count}'}</b>\n\n"
            )

        await message.answer(text)