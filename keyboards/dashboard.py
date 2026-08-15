from aiogram.utils.keyboard import InlineKeyboardBuilder


def dashboard_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Back",
        callback_data="home",
        style="danger",
        icon_custom_emoji_id="5409284148491726576"
    )

    kb.adjust(1)

    return kb.as_markup()