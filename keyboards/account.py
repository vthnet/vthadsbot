from aiogram.utils.keyboard import InlineKeyboardBuilder


def accounts_keyboard(accounts):

    kb = InlineKeyboardBuilder()

    for acc in accounts:

        status = "🟢" if acc.active else "🔴"

        kb.button(
            text=f"{status} {acc.account_name}",
            callback_data=f"account_{acc.id}"
        )

    kb.button(
        text="➕ Add Account",
        callback_data="add_account"
    )

    kb.button(
        text="🔄 Refresh",
        callback_data="my_accounts"
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


def account_details_keyboard(account_id):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🗑 Remove Account",
        callback_data=f"remove_account_{account_id}"
    )

    kb.button(
        text="🔙 Back",
        callback_data="my_accounts"
    )

    kb.adjust(
        1,
        1
    )

    return kb.as_markup()


def account_manage_keyboard(account_id):

    return account_details_keyboard(account_id)


def back_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.button(
        text="🔙 Back",
        callback_data="home"
    )

    kb.adjust(2)

    return kb.as_markup()