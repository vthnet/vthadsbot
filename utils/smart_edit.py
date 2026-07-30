from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest


async def smart_edit(
    event,
    text: str,
    reply_markup=None,
):
    if isinstance(event, CallbackQuery):
        msg = event.message
        callback = event
    else:
        msg = event
        callback = None

    result = msg

    try:
        result = await msg.edit_text(
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
                result = await msg.edit_caption(
                    caption=text,
                    reply_markup=reply_markup,
                )

            except TelegramBadRequest:
                result = await msg.answer(
                    text=text,
                    reply_markup=reply_markup,
                )

        elif "message to edit not found" in error:

            result = await msg.answer(
                text=text,
                reply_markup=reply_markup,
            )

        else:
            raise

    if callback:
        try:
            await callback.answer()
        except TelegramBadRequest:
            pass

    return result