from sqlalchemy import (
    select,
    delete
)

from database.session import SessionLocal

from database.models.bio_rotation_item import (
    BioRotationItem
)


class BioRotationItemRepository:

    @staticmethod
    async def add(
        rotation_id: int,
        bio_id: int
    ):

        async with SessionLocal() as session:

            item = BioRotationItem(
                rotation_id=rotation_id,
                bio_id=bio_id
            )

            session.add(item)

            await session.commit()

    @staticmethod
    async def get_bios(
        rotation_id: int
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(
                    BioRotationItem
                ).where(
                    BioRotationItem.rotation_id == rotation_id
                )
            )

            return result.scalars().all()

    @staticmethod
    async def clear(
        rotation_id: int
    ):

        async with SessionLocal() as session:

            await session.execute(
                delete(
                    BioRotationItem
                ).where(
                    BioRotationItem.rotation_id == rotation_id
                )
            )

            await session.commit()

    @staticmethod
    async def delete_bio(
        bio_id: int
    ):

        async with SessionLocal() as session:

            await session.execute(
                delete(
                    BioRotationItem
                ).where(
                    BioRotationItem.bio_id == bio_id
                )
            )

            await session.commit()