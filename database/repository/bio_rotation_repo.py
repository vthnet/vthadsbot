from sqlalchemy import select

from database.session import SessionLocal
from database.models.bio_rotation import BioRotation


class BioRotationRepository:

    @staticmethod
    async def create(account_id: int, interval: int = 3600):

        async with SessionLocal() as session:

            result = await session.execute(
                select(BioRotation)
                .where(BioRotation.account_id == account_id)
                .order_by(BioRotation.id.desc())
            )

            rotation = result.scalars().first()

            if rotation:
                rotation.enabled = True
                rotation.interval = interval

                await session.commit()
                await session.refresh(rotation)

                return rotation

            rotation = BioRotation(
                account_id=account_id,
                enabled=True,
                interval=interval
            )

            session.add(rotation)

            await session.commit()
            await session.refresh(rotation)

            return rotation

    @staticmethod
    async def get(account_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(BioRotation)
                .where(BioRotation.account_id == account_id)
                .order_by(BioRotation.id.desc())
            )

            return result.scalars().first()

    @staticmethod
    async def get_running():

        async with SessionLocal() as session:

            result = await session.execute(
                select(BioRotation)
                .where(BioRotation.enabled == True)
            )

            return result.scalars().all()

    @staticmethod
    async def disable(account_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(BioRotation)
                .where(BioRotation.account_id == account_id)
                .order_by(BioRotation.id.desc())
            )

            rotation = result.scalars().first()

            if rotation:
                rotation.enabled = False

                await session.commit()
                await session.refresh(rotation)

                return True

            return False

    @staticmethod
    async def save(rotation):

        async with SessionLocal() as session:

            await session.merge(rotation)

            await session.commit()