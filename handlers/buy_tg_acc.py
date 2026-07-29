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
🛒 <b>Telegram Accounts Store</b>
-------------------------
Buy high-quality Telegram accounts from our trusted VTH source
•VTH network's own selling hub 
• Fully automated , purchase good quality tg acc 24x7 
• 100+ countries available
• Trusted by 1000+ users
• Always trusted , 24x7 support team available
-------------------------
Choose an option below to continue.
""",
        kb.as_markup()
    )