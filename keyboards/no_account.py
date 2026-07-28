from aiogram.utils.keyboard import InlineKeyboardBuilder


def no_account_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="➕ Add Account",
        callback_data="add_account"
    )

    kb.button(
        text="🔙 Back",
        callback_data="home"
    )

    kb.adjust(1, 1)

    return kb.as_markup()