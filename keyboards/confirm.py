from aiogram.utils.keyboard import InlineKeyboardBuilder


def confirm_campaign_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🚀 Start Campaign",
        callback_data="start_campaign"
    )

    kb.button(
        text="❌ Cancel",
        callback_data="cancel_campaign"
    )

    kb.button(
        text="🔙 Back",
        callback_data="back_delay"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(
        1,
        2,
        1
    )

    return kb.as_markup()