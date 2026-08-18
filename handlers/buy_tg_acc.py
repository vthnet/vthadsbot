from custom_emojis import button_emoji_id
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.smart_edit import smart_edit

router = Router()


@router.callback_query(F.data == "buy_tg_acc")
async def buy_tg_acc(callback: CallbackQuery):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Buy Tg Accounts",
        url="https://t.me/Quickcodes_bot",
        style="success",
        icon_custom_emoji_id=button_emoji_id("6296218646284863141")
    )

    kb.button(
        text="Support",
        url="https://t.me/vthnetsupport",
        style="success",
        icon_custom_emoji_id=button_emoji_id("5866185084427572234")
    )

    kb.button(
        text="Developer",
        url="https://t.me/valriks",
        style="danger",
        icon_custom_emoji_id=button_emoji_id("5819109854861595641")
    )

    kb.button(
        text="Home",
        callback_data="home",
        style="primary",
        icon_custom_emoji_id=button_emoji_id("5193119436621494267"),
        

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