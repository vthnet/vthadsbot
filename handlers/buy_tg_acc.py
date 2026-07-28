from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.smart_edit import smart_edit

router = Router()


@router.callback_query(F.data == "buy_tg_acc")
async def buy_tg_acc(callback: CallbackQuery):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🤖 Buy Telegram Accounts",
        url="https://t.me/Quickcodes_bot"
    )

    kb.button(
        text="🛟 Support",
        url="https://t.me/vthnetsupport"
    )

    kb.button(
        text="👑 Owner",
        url="https://t.me/valriks"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(1)

    await smart_edit(
        callback,
        """
🛒 <b>Telegram Accounts Marketplace</b>

━━━━━━━━━━━━━━━━━━━━

Buy high-quality Telegram accounts from our trusted marketplace.

✅ Fresh Accounts

✅ Aged Accounts

✅ Premium Accounts

✅ Bulk Orders

✅ Instant Delivery

✅ Trusted Seller

━━━━━━━━━━━━━━━━━━━━

Choose an option below to continue.
""",
        kb.as_markup()
    )