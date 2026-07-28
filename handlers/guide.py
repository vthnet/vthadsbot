from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "guide")
async def guide(callback: CallbackQuery):

    await callback.answer(
        """
📖 QUICK GUIDE
1. Add Account
2. Create Campaign
3. Select Groups
4. Start Campaign

🆘 Help: @vthnetsupport
🐧 Owner : @valriks
""",
        show_alert=True
    )