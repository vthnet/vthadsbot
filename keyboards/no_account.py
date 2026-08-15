from aiogram.utils.keyboard import InlineKeyboardBuilder


def no_account_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Add Account",
        callback_data="add_account",
        style="primary",
        icon_custom_emoji_id="5409284148491726576"
    )

    kb.button(
        text="Back",
        callback_data="home",
        style="danger",
        icon_custom_emoji_id="5287354223141342798"
    )

    kb.adjust(1, 1)

    return kb.as_markup()