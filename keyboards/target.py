from aiogram.utils.keyboard import InlineKeyboardBuilder


def target_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📂 All Joined Groups",
        callback_data="target_all_groups"
    )


    kb.button(
        text="🔙 Back",
        callback_data="create_campaign"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(
        1,
        2
    )

    return kb.as_markup()