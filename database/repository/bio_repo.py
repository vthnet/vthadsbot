from sqlalchemy import (
    select,
    delete,
    func
)

from database.session import SessionLocal
from database.models.bio import Bio


class BioRepository:

    @staticmethod
    async def add(
        user_id: int,
        text: str
    ):

        async with SessionLocal() as session:

            bio = Bio(
                user_id=user_id,
                text=text
            )

            session.add(bio)

            await session.commit()
            await session.refresh(bio)

            return bio

    @staticmethod
    async def get_bios(
        user_id: int
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(Bio).where(
                    Bio.user_id == user_id
                )
            )

            return result.scalars().all()

    @staticmethod
    async def count(
        user_id: int
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(
                    func.count(Bio.id)
                ).where(
                    Bio.user_id == user_id
                )
            )

            return result.scalar() or 0

    @staticmethod
    async def delete(
        bio_id: int
    ):

        async with SessionLocal() as session:

            await session.execute(
                delete(Bio).where(
                    Bio.id == bio_id
                )
            )

            await session.commit()

    @staticmethod
    async def get_by_id(
        bio_id: int
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(Bio).where(
                    Bio.id == bio_id
                )
            )

            return result.scalar_one_or_none()