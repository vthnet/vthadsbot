from aiogram.utils.keyboard import InlineKeyboardBuilder


def loop_keyboard(is_premium: bool = False):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🔁 1 Loop",
        callback_data="loop_1"
    )

    kb.button(
        text="🔁 2 Loops",
        callback_data="loop_2"
    )

    kb.button(
        text="🔁 5 Loops",
        callback_data="loop_5"
    )

    kb.button(
        text="🔁 10 Loops",
        callback_data="loop_10"
    )

    kb.button(
        text="🔁 20 Loops",
        callback_data="loop_20"
    )

    kb.button(
        text="♾️ Infinite Loop",
        callback_data="loop_infinite"
    )

    kb.button(
        text="⭐ Custom Loop",
        callback_data="loop_custom"
    )

    kb.button(
        text="🔙 Back",
        callback_data="continue_groups"
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
        1
    )

    return kb.as_markup()