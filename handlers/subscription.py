from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.repository.user_repo import UserRepository
from utils.smart_edit import smart_edit

router = Router()


@router.callback_query(F.data == "subscription")
@router.callback_query(F.data == "premium")
async def subscription(callback: CallbackQuery):

    user = await UserRepository.get_user(
        callback.from_user.id
    )

    kb = InlineKeyboardBuilder()

    if user and user.is_premium:

        kb.button(
            text="✏️ Custom Bio",
            callback_data="custom_bio"
        )

        kb.button(
            text="🔄 Bio Rotation",
            callback_data="bio_rotation"
        )

        kb.button(
            text="🏠 Home",
            callback_data="home"
        )

        kb.adjust(1)

        text = """
👑 <b>VTH PREMIUM</b>
━━━━━━━━━━━━━━━━━━━━━━━━━
🟢 <b>Status</b> :Lifetime Member
━━━━━━━━━━━━━━━━━━━━━━━━━
✅ More then 1 acc can be used to create multiple ads together .
✅ Custom looping , custom delay .
✅ Remove VTH Bio.
✅ Set Your Own custom Bio.
✅ Auto Bio Rotation (you can set custom 5 bio's , and can set time gap bot will auto change bio after fixed period of time)
✅ Priority Support and many more..
✅ Future Premium Features.
━━━━━━━━━━━━━━━━━━━━━━━━━

❤️ Thank you for supporting VTH Network.
"""

    else:

        kb.button(
            text="💳 Buy Premium",
            callback_data="buy_premium"
        )

        kb.button(
            text="🏠 Home",
            callback_data="home"
        )

        kb.adjust(1)

        text = """
👑 <b>VTH PREMIUM</b>
━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 <b>Status</b> :Free User
━━━━━━━━━━━━━━━━━━━━━━━━━
💎Unlock Premium Forever💎
↪ premium features you will get !!
✅ More then 1 acc can be used to create multiple ads together .
✅ Custom looping , custom delay .
✅ Remove VTH Bio.
✅ Set Your Own custom Bio.
✅ Auto Bio Rotation (you can set custom 5 bio's , and can set time gap bot will auto change bio after fixed period of time)
✅ Priority Support and many more..
✅ Future Premium Features.
━━━━━━━━━━━━━━━━━━━━━━━━━
♾ Lifetime Membership
💰 One-Time Payment

Click the button below to upgrade.
"""

    await smart_edit(
        callback,
        text,
        kb.as_markup()
    )