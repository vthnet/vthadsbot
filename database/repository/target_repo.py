from sqlalchemy import select, delete

from database.session import SessionLocal
from database.models.campaign_target import CampaignTarget


class TargetRepository:


    @staticmethod
    async def get_targets(campaign_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(CampaignTarget)
                .where(
                    CampaignTarget.campaign_id == campaign_id
                )
            )

            return result.scalars().all()



    @staticmethod
    async def add_target(
        campaign_id: int,
        chat_id: int,
        chat_username=None,
        chat_title=None
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
    async def delete_campaign_targets(
        campaign_id:int
    ):

        async with SessionLocal() as session:

            await session.execute(
                delete(CampaignTarget)
                .where(
                    CampaignTarget.campaign_id == campaign_id
                )
            )

            await session.commit()