from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest


async def smart_edit(
    callback: CallbackQuery,
    text: str,
    reply_markup=None,
):
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=reply_markup,
        )

    except TelegramBadRequest as e:
        error = str(e).lower()

        if "message is not modified" in error:
            pass

        elif (
            "there is no text in the message to edit" in error
            or "message can't be edited" in error
        ):
            try:
                await callback.message.edit_caption(
                    caption=text,
                    reply_markup=reply_markup,
                )
            except TelegramBadRequest:
                pass

        elif "message to edit not found" in error:
            return

        else:
            raise

    try:
        await callback.answer()
    except TelegramBadRequest:
        pass