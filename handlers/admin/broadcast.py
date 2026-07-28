from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from loader import bot
from config import config
from database.session import SessionLocal
from database.models.user import User

from sqlalchemy import select

router = Router()


@router.message(Command("broadcast"))
async def broadcast(message: Message):

    if message.from_user.id not in config.ADMINS:
        return

    if not message.reply_to_message:

        await message.answer(
            "Reply to any message with /broadcast"
        )
        return

    sent = 0
    failed = 0

    async with SessionLocal() as session:

        result = await session.execute(
            select(User.telegram_id)
        )

        users = result.scalars().all()

    status = await message.answer(
        f"📢 Broadcasting...\n\n0/{len(users)}"
    )

    for i, user_id in enumerate(users, start=1):

        try:

            await bot.copy_message(
                chat_id=user_id,
                from_chat_id=message.chat.id,
                message_id=message.reply_to_message.message_id,
            )

            sent += 1

        except Exception:

            failed += 1

        if i % 20 == 0 or i == len(users):

            try:

                await status.edit_text(
                    f"""
📢 Broadcasting...

Progress: {i}/{len(users)}

✅ Sent : {sent}
❌ Failed : {failed}
"""
                )

            except Exception:
                pass

    await status.edit_text(
        f"""
✅ Broadcast Completed

👥 Total Users : {len(users)}

📤 Sent : {sent}

❌ Failed : {failed}
"""
    )