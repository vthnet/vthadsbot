from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from sqlalchemy import select, func

from config import config
from database.session import SessionLocal
from database.models.user import User
from database.models.account import Account
from database.models.campaign import Campaign

router = Router()


@router.message(Command("status"))
async def bot_status(message: Message):

    if message.from_user.id not in config.ADMINS:
        return

    async with SessionLocal() as session:

        total_users = await session.scalar(
            select(func.count(User.id))
        )

        premium_users = await session.scalar(
            select(func.count(User.id)).where(
                User.is_premium.is_(True)
            )
        )

        banned_users = await session.scalar(
            select(func.count(User.id)).where(
                User.is_banned.is_(True)
            )
        )

        total_accounts = await session.scalar(
            select(func.count(Account.id))
        )

        active_accounts = await session.scalar(
            select(func.count(Account.id)).where(
                Account.active.is_(True)
            )
        )

        dead_accounts = (total_accounts or 0) - (active_accounts or 0)

        total_campaigns = await session.scalar(
            select(func.count(Campaign.id))
        )

        running_campaigns = await session.scalar(
            select(func.count(Campaign.id)).where(
                Campaign.running.is_(True)
            )
        )

        paused_campaigns = await session.scalar(
            select(func.count(Campaign.id)).where(
                Campaign.paused.is_(True)
            )
        )

        completed_campaigns = await session.scalar(
            select(func.count(Campaign.id)).where(
                Campaign.completed.is_(True)
            )
        )

        total_sent = (
            await session.scalar(
                select(func.sum(Campaign.total_sent))
            )
        ) or 0

        total_failed = (
            await session.scalar(
                select(func.sum(Campaign.failed_sent))
            )
        ) or 0

    await message.answer(
        f"""
📊 <b>VTH ADS BOT STATUS</b>

━━━━━━━━━━━━━━

👥 Users : <b>{total_users}</b>
💎 Premium : <b>{premium_users}</b>
🚫 Banned : <b>{banned_users}</b>

━━━━━━━━━━━━━━

📱 Accounts : <b>{total_accounts}</b>
🟢 Active : <b>{active_accounts}</b>
🔴 Dead : <b>{dead_accounts}</b>

━━━━━━━━━━━━━━

📢 Campaigns : <b>{total_campaigns}</b>
🟢 Running : <b>{running_campaigns}</b>
⏸ Paused : <b>{paused_campaigns}</b>
✅ Completed : <b>{completed_campaigns}</b>

━━━━━━━━━━━━━━

📤 Messages Sent : <b>{total_sent}</b>
❌ Failed : <b>{total_failed}</b>
"""
    )