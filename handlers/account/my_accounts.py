import asyncio

from aiogram import Router, F
from aiogram.types import CallbackQuery

from database.repository.account_repo import AccountRepository
from keyboards.account import (
    accounts_keyboard,
    account_details_keyboard
)
from utils.smart_edit import smart_edit
from services.cache.dashboard_cache import clear
from services.sessions.session_checker import check_session

router = Router()


@router.callback_query(F.data == "my_accounts")
async def my_accounts(callback: CallbackQuery):

    await callback.answer(
        """
🔄 Refreshing Accounts

Checking all Telegram accounts.

⏳ Please wait...
""",
        show_alert=True
    )

    user = await AccountRepository.get_user(
        callback.from_user.id
    )

    if not user:
        await callback.answer(
            "User not found",
            show_alert=True
        )
        return

    accounts = await AccountRepository.get_accounts(
        user.id
    )

    if not accounts:

        from aiogram.utils.keyboard import InlineKeyboardBuilder

        kb = InlineKeyboardBuilder()

        kb.button(
            text="Add Account",
            callback_data="add_account",
            style="primary",
            icon_custom_emoji_id="5287354223141342798"
        )

        kb.button(
            text="Home",
            callback_data="home",
            style="primary",
            icon_custom_emoji_id="5193119436621494267"
        )

        kb.adjust(1)

        await smart_edit(
            callback,
            """
📱 <b>My Accounts</b>
━━━━━━━━━━━━━━━━━━━━━━
❌ <b>No Telegram Accounts Found</b>

You haven't added any Telegram
accounts yet.

Click <b>➕ Add Account</b> to get started.
━━━━━━━━━━━━━━━━━━━━━━
""",
            kb.as_markup()
        )

        return

    active = 0

    text = (
        "📱 <b>My Telegram Accounts</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    for acc in accounts:

        try:
            status = await check_session(
                acc.session_string
            )

            await AccountRepository.update_status(
                acc.id,
                status
            )

            acc.active = status

        except Exception:
            status = False

        icon = "🟢 Online" if status else "🔴 Expired"

        if status:
            active += 1

        text += (
            f"👤 <b>{acc.account_name}</b>\n"
            f"📱 <code>{acc.phone}</code>\n"
            f"🚦 Status : {icon}\n\n"
        )

    text += (
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 Total Accounts : <b>{len(accounts)}</b>\n"
        f"🟢 Active : <b>{active}</b>\n"
        f"🔴 Expired : <b>{len(accounts)-active}</b>"
    )

    await smart_edit(
        callback,
        text,
        accounts_keyboard(accounts)
    )

@router.callback_query(F.data.startswith("account_"))
async def account_details(callback: CallbackQuery):

    account_id = int(
        callback.data.split("_")[1]
    )

    account = await AccountRepository.get_account(
        account_id
    )

    if not account:

        await callback.answer(
            "Account not found",
            show_alert=True
        )
        return

    status = await check_session(
        account.session_string
    )

    await AccountRepository.update_status(
        account.id,
        status
    )

    account.active = status

    await smart_edit(
        callback,
        f"""
👤 <b>{account.account_name}</b>
--------------------------------------------------
📱 Phone :<code>{account.phone}</code>

📊 Status :{"🟢 Active" if status else "🔴 Session Expired"}

🆔 Account ID :<code>{account.id}</code>
--------------------------------------------------
""",
        account_details_keyboard(
            account.id
        )
    )


@router.callback_query(
    F.data.startswith("remove_account_")
)
async def remove_account(callback: CallbackQuery):

    account_id = int(
        callback.data.split("_")[2]
    )

    await AccountRepository.delete_account(
        account_id
    )

    await asyncio.sleep(0.3)

    user = await AccountRepository.get_user(
        callback.from_user.id
    )

    clear(user.id)

    await callback.answer(
        """
✅ ACCOUNT REMOVED

The Telegram account has been
removed successfully.

You will now be redirected
to My Accounts.
""",
        show_alert=True
    )

    await my_accounts(callback)