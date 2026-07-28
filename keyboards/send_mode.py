from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def send_mode_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📝 Copy",
        callback_data="send_copy"
    )

    kb.button(
        text="↪️ Forward",
        callback_data="send_forward"
    )

    kb.adjust(2)

    return kb.as_markup()