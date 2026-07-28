from aiogram.utils.keyboard import InlineKeyboardBuilder

def interval_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="✅ Continue",
        callback_data="bio_enable_confirm"
    )

    kb.button(
        text="⭐ Custom Time",
        callback_data="bio_custom_time"
    )

    kb.button(
        text="🔙 Back",
        callback_data="bio_enable"
    )

    kb.adjust(
        1,
        2
    )

    return kb.as_markup()