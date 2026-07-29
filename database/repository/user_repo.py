from sqlalchemy import select

from database.session import SessionLocal
from database.models.user import User


class UserRepository:

    @staticmethod
    async def get_user(telegram_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(User).where(
                    User.telegram_id == telegram_id
                )
            )

            return result.scalar_one_or_none()


    @staticmethod
    async def create_user(
        telegram_id: int,
        username: str | None,
        first_name: str,
    ):

        async with SessionLocal() as session:

            user = User(
                telegram_id=telegram_id,
                username=username,
                first_name=first_name,
            )

            session.add(user)

            await session.commit()

            return user


    @staticmethod
    async def set_premium(
        telegram_id: int,
        premium: bool = True
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(User).where(
                    User.telegram_id == telegram_id
                )
            )

            user = result.scalar_one_or_none()

            if user:

                user.is_premium = premium

                await session.commit()

                return True

            return False


    @staticmethod
    async def update_custom_bio(
        telegram_id: int,
        bio: str
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(User).where(
                    User.telegram_id == telegram_id
                )
            )

            user = result.scalar_one_or_none()

            if user:

                user.custom_bio = bio

                await session.commit()



    @staticmethod
    async def add_wallet(
        telegram_id: int,
        amount: int
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(User).where(
                    User.telegram_id == telegram_id
                )
            )

            user = result.scalar_one_or_none()

            if user:

                user.wallet += amount

                await session.commit()


    @staticmethod
    async def remove_wallet(
        telegram_id: int,
        amount: int
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(User).where(
                    User.telegram_id == telegram_id
                )
            )

            user = result.scalar_one_or_none()

            if user:

                user.wallet -= amount

                await session.commit()


    @staticmethod
    async def get_all_premium():

        async with SessionLocal() as session:

            result = await session.execute(
                select(User).where(
                    User.is_premium.is_(True)
                )
            )

            return result.scalars().all()


    @staticmethod
    async def get_all():

        async with SessionLocal() as session:

            result = await session.execute(
                select(User)
            )

            return result.scalars().all()





