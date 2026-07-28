from aiogram.utils.keyboard import InlineKeyboardBuilder


def delay_keyboard(is_premium: bool = False):

    kb = InlineKeyboardBuilder()

    kb.button(text="60 Sec", callback_data="delay_60")
    kb.button(text="5 Min", callback_data="delay_300")

    kb.button(text="10 Min", callback_data="delay_600")
    kb.button(text="20 Min", callback_data="delay_1200")

    kb.button(text="30 Min", callback_data="delay_1800")
    kb.button(text="60 Min", callback_data="delay_3600")

    kb.button(text="180 Min", callback_data="delay_10800")
    kb.button(text="24 Hours", callback_data="delay_86400")

    if is_premium:

        kb.button(
            text="✏️ Custom Delay",
            callback_data="delay_custom"
        )

    else:

        kb.button(
            text="⭐ Custom Delay",
            callback_data="premium_delay"
        )

    kb.button(
        text="⚠️ Lower delay = Higher spam risk",
        callback_data="ignore"
    )

    kb.button(
        text="🔙 Back",
        callback_data="back_loop"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(
        2,
        2,
        2,
        2,
        1,
        1,
        2
    )

    return kb.as_markup()