from aiogram.utils.keyboard import InlineKeyboardBuilder


def time_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="5 Minutes",
        callback_data="time_300"
    )

    kb.button(
        text="10 Minutes",
        callback_data="time_600"
    )

    kb.button(
        text="30 Minutes",
        callback_data="time_1800"
    )

    kb.button(
        text="✅ 1 Hour (Recommended)",
        callback_data="time_3600"
    )

    kb.button(
        text="2 Hours",
        callback_data="time_7200"
    )

    kb.button(
        text="6 Hours",
        callback_data="time_21600"
    )

    kb.button(
        text="12 Hours",
        callback_data="time_43200"
    )

    kb.button(
        text="⌨ Custom Minutes",
        callback_data="time_custom"
    )

    kb.button(
        text="🔙 Back",
        callback_data="bio_continue"
    )

    kb.adjust(2, 2, 2, 1, 1, 1)

    return kb.as_markup()