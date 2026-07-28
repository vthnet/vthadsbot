from aiogram.utils.keyboard import InlineKeyboardBuilder


def dashboard_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🔙 Back",
        callback_data="home"
    )

    kb.adjust(1)

    return kb.as_markup()