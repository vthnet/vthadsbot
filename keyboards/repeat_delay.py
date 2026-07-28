from aiogram.utils.keyboard import InlineKeyboardBuilder


def repeat_delay_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🔴 1 Minute",
        callback_data="repeat_60"
    )

    kb.button(
        text="🟠 10 Minutes",
        callback_data="repeat_600"
    )

    kb.button(
        text="🟡 20 Minutes",
        callback_data="repeat_1200"
    )

    kb.button(
        text="🟢 30 Minutes",
        callback_data="repeat_1800"
    )

    kb.button(
        text="🛡 60 Minutes",
        callback_data="repeat_3600"
    )

    kb.button(
        text="⭐ Custom Interval",
        callback_data="repeat_custom"
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
        2
    )

    return kb.as_markup()