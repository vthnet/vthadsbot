from sqlalchemy import select, func, delete

from database.session import SessionLocal
from database.models.account import Account
from database.models.user import User


class AccountRepository:


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
    async def get_account(account_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(Account).where(
                    Account.id == account_id
                )
            )

            return result.scalar_one_or_none()



    @staticmethod
    async def count_accounts(user_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(func.count(Account.id))
                .where(Account.user_id == user_id)
            )

            return result.scalar() or 0



    @staticmethod
    async def get_accounts(user_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(Account)
                .where(Account.user_id == user_id)
            )

            accounts = result.scalars().all()

            unique_accounts = []
            seen_sessions = set()

            for acc in accounts:
               if acc.session_string in seen_sessions:
                    continue
 
               seen_sessions.add(acc.session_string)
               unique_accounts.append(acc)

            return unique_accounts



    @staticmethod
    async def add_account(
        user_id: int,
        account_name: str,
        phone: str,
        session_string: str,
    ):

        async with SessionLocal() as session:

            account = Account(
                user_id=user_id,
                account_name=account_name,
                phone=phone,
                session_string=session_string,
                active=True,
            )

            session.add(account)

            await session.commit()

            return account



    @staticmethod
    async def delete_account(account_id: int):

        async with SessionLocal() as session:

            await session.execute(
                delete(Account)
                .where(Account.id == account_id)
            )

            await session.commit()



    @staticmethod
    async def update_status(
        account_id: int,
        status: bool
    ):

        async with SessionLocal() as session:

            account = await session.get(
                Account,
                account_id
            )

            if account:

                account.active = status

                await session.commit()


    @staticmethod
    async def get_active_accounts():

        async with SessionLocal() as session:

            result = await session.execute(
                select(Account).where(
                    Account.active == True
                )
            )

            return result.scalars().all()