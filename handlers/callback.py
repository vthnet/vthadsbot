from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline import back_keyboard
from utils.smart_edit import smart_edit
from utils.loading import loading

router = Router()


PAGES = {



    "support": """
🆘 <b>Support Center</b>
━━━━━━━━━━━━━━━━━━━━
Need help?

Contact @vthnetsupport for any issue related to campaigns, accounts or payments.

━━━━━━━━━━━━━━━━━━━━
💬 Response Time
Usually within 24 hours.
"""
}


@router.callback_query(F.data.in_(PAGES.keys()))
async def pages(callback: CallbackQuery):

    await loading(
        callback,
        "📄 Loading..."
    )

    await smart_edit(
        callback,
        PAGES[callback.data],
        await back_keyboard(
            callback.from_user.id
        )
    )


@router.callback_query(F.data == "ignore")
async def ignore(callback: CallbackQuery):

    await callback.answer()