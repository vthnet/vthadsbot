from sqlalchemy import select, delete

from database.session import SessionLocal

from database.models.campaign import Campaign
from database.models.campaign_target import CampaignTarget
from sqlalchemy import func

class CampaignRepository:

    @staticmethod
    async def create(
        account_id: int,
        post_data: str,
        media_path: str = None,
    
    ):

        async with SessionLocal() as session:

            campaign = Campaign(
                account_id=account_id,
                title="New Campaign",
                post_data=post_data,
                media_path=media_path,
                send_delay=5,
                repeat_delay=86400,
                total_sent=0,
                running=False
            )

            session.add(campaign)

            await session.commit()
            await session.refresh(campaign)

            return campaign


    @staticmethod
    async def add_target(
        campaign_id: int,
        chat_id,
        chat_username: str = None,
        chat_title: str = None
    ):

        async with SessionLocal() as session:

            target = CampaignTarget(
                campaign_id=campaign_id,
                chat_id=chat_id,
                chat_username=chat_username,
                chat_title=chat_title
            )

            session.add(target)

            await session.commit()

            return target


    @staticmethod
    async def get_targets(
        campaign_id: int
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(CampaignTarget).where(
                    CampaignTarget.campaign_id == campaign_id
                )
            )

            return result.scalars().all()


    @staticmethod
    async def get_user_campaigns(
        user_id: int
    ):

        from database.models.account import Account

        async with SessionLocal() as session:

            result = await session.execute(
                select(Campaign)
                .join(Account)
                .where(
                    Account.user_id == user_id
                )
            )

            return result.scalars().all()


    @staticmethod
    async def get_campaign(
        campaign_id: int
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(Campaign).where(
                    Campaign.id == campaign_id
                )
            )

            return result.scalar_one_or_none()
        
    @staticmethod
    async def delete_campaign(
        campaign_id: int
    ):

        async with SessionLocal() as session:

            await session.execute(
                delete(Campaign).where(
                    Campaign.id == campaign_id
                )
            )

            await session.commit()


    @staticmethod
    async def update_status(
      campaign_id: int,
      running: bool,
):

     async with SessionLocal() as session:

        campaign = await session.get(
            Campaign,
            campaign_id,
        )

        if not campaign:
            return

        campaign.running = running

        if running:
            campaign.paused = False
            campaign.completed = False
            campaign.finished_at = None

        else:
            campaign.paused = False
            campaign.current_target = "Stopped"

        await session.commit()
        await session.refresh(campaign)

        return campaign


    @staticmethod
    async def pause_campaign(
        campaign_id: int
    ):

        async with SessionLocal() as session:

            campaign = await session.get(
                Campaign,
                campaign_id
            )

            if campaign:

                campaign.paused = True

                await session.commit()


    @staticmethod
    async def resume_campaign(
        campaign_id: int
    ):

        async with SessionLocal() as session:

            campaign = await session.get(
                Campaign,
                campaign_id
            )

            if campaign:

                campaign.paused = False
                campaign.running = True

                await session.commit()


    @staticmethod
    async def update_send_delay(
         campaign_id: int,
         delay: int
    ):

       async with SessionLocal() as session:

        campaign = await session.get(
            Campaign,
            campaign_id
        )

        if campaign:

            campaign.send_delay = delay

            await session.commit()


    @staticmethod
    async def update_repeat_delay(
                campaign_id: int,
                delay: int
            ):    

    

       async with SessionLocal() as session:

        campaign = await session.get(
            Campaign,
            campaign_id
        )

        if campaign:

            campaign.repeat_delay = delay

            await session.commit()


    @staticmethod
    async def update_loop(
        campaign_id: int,
        loops: int,
        infinite: bool = False
    ):

        async with SessionLocal() as session:

            campaign = await session.get(
                Campaign,
                campaign_id
            )

            if campaign:

                campaign.loop_count = loops
                campaign.infinite = infinite

                await session.commit()


    @staticmethod
    async def save(campaign):

        async with SessionLocal() as session:

            db_campaign = await session.get(
                Campaign,
                campaign.id
            )

            if db_campaign:

                db_campaign.total_sent = campaign.total_sent
                db_campaign.running = campaign.running
                db_campaign.completed_loops = campaign.completed_loops
                db_campaign.send_delay = campaign.send_delay
                db_campaign.repeat_delay = campaign.repeat_delay
                db_campaign.paused = campaign.paused
                db_campaign.loop_count = campaign.loop_count
                db_campaign.infinite = campaign.infinite

                await session.commit()


    @staticmethod
    async def update_pause(
        campaign_id: int,
        paused: bool
    ):

        async with SessionLocal() as session:

            campaign = await session.get(
                Campaign,
                campaign_id
            )

            if campaign:

                campaign.paused = paused

                await session.commit()

    @staticmethod
    async def count_user_campaigns(
        user_id: int
    ):

        from database.models.account import Account

        async with SessionLocal() as session:

            result = await session.execute(
                select(
                    func.count(Campaign.id)
                )
                .join(Account)
                .where(
                    Account.user_id == user_id
                )
            )

            return result.scalar() or 0