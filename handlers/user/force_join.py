from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from loader import bot
from config import config
from keyboards.inline import force_join_keyboard


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
                user_id=user_id
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


    if joined:

        await callback.message.edit_text(
            "<b>✅ Verification successful!</b>\n\n"
                  "Welcome to VTH Ads Bot.",
        )

    else:

        try:

            await callback.message.edit_text(
                "<b>🚫 You have not joined all channels yet.</b>\n\n"
                "Join them and press verify again.",
                reply_markup=force_join_keyboard(),
            )

        except TelegramBadRequest:
            pass


    await callback.answer()