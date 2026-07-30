from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from loader import bot
from config import config
from keyboards.inline import force_join_keyboard

from database.repository.user_repo import UserRepository


async def check_force_join(user_id: int) -> bool:

    channels = [
        config.FORCE_JOIN_1,
        config.FORCE_JOIN_2,
    ]

    for channel in channels:

        if not channel:
            continue

        try:

            member = await bot.get_chat_member(
                chat_id=channel,
                user_id=user_id,
            )

            if member.status in (
                "left",
                "kicked",
            ):
                return False

        except TelegramBadRequest:
            return False

    return True


async def force_join_message(message: Message):

    await message.answer(
        "<b>🚫 Join both channels first.</b>\n\n"
        "After joining press ✅ Verify.",
        reply_markup=force_join_keyboard(),
    )


async def force_join_callback(callback: CallbackQuery):

    joined = await check_force_join(
        callback.from_user.id
    )

    if not joined:

        await callback.answer(
            "⚠️ Please join both required channels first, then tap '✅ Verify' again.",
            show_alert=True,
        )

        try:
            await callback.message.edit_reply_markup(
                reply_markup=force_join_keyboard()
            )
        except TelegramBadRequest:
            pass

        return

    from handlers.user.start import send_home

    user = await UserRepository.get_user(
        callback.from_user.id
    )

    if not user:
        await callback.answer(
            "User not found.",
            show_alert=True,
        )
        return

    await send_home(
        callback,
        user,
        edit=True,
    )