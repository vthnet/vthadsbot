from aiogram.utils.keyboard import InlineKeyboardBuilder


def bio_home_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="➕ Add Bio",
        callback_data="bio_add"
    )

    kb.button(
        text="🗑 Delete Bio",
        callback_data="bio_delete"
    )

    kb.button(
        text="▶ Enable Rotation",
        callback_data="bio_enable"
    )

    kb.button(
        text="⛔ Disable Rotation",
        callback_data="bio_disable"
    )

    kb.button(
        text="⏱ Change Interval",
        callback_data="bio_change_interval"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(
        2,
        2,
        1,
        1
    )

    return kb.as_markup()


def back_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🔙 Back",
        callback_data="bio_home"
    )

    kb.adjust(1)

    return kb.as_markup()


def no_account_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="➕ Add Account",
        callback_data="add_account"
    )

    kb.button(
        text="🔙 Back",
        callback_data="bio_home"
    )

    kb.adjust(
        1,
        1
    )

    return kb.as_markup()


def continue_keyboard(
    buttons,
    selected
):

    kb = InlineKeyboardBuilder()

    for text, data in buttons:

        kb.button(
            text=text,
            callback_data=data
        )

    kb.button(
        text=f"✅ Continue ({selected})",
        callback_data="bio_continue"
    )

    kb.button(
        text="🔙 Back",
        callback_data="bio_enable"
    )

    kb.adjust(1)

    return kb.as_markup()


def minimum_bio_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="➕ Add Bio",
        callback_data="bio_add"
    )

    kb.button(
        text="🔙 Back",
        callback_data="bio_home"
    )

    kb.adjust(1)

    return kb.as_markup()