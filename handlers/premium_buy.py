from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from handlers.premium.state import PremiumState
from database.repository.user_repo import UserRepository

router = Router()


UPI_ID = "itsakt5@ptyes"
PRICE = "₹499"


@router.callback_query(F.data == "buy_premium")
async def buy_premium(callback: CallbackQuery):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="✅ I've Paid",
        callback_data="premium_paid"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(1)

    await callback.message.edit_text(
        f"""
👑 <b>VTH Premium Membership</b>
-------------------------
💰 Price :<b>{PRICE} / x $</b>
♾ Lifetime Membership
-------------------------
UPI ID (₹) :<code>{UPI_ID}</code>
Binance uid ($): <code></code>
-------------------------
•After payment,Click <b>I've Paid</b>

•Admin will verify your payment and activate Premium.
•Please keep your UTR / Transaction ID ready.
""",
        reply_markup=kb.as_markup()
    )

    await callback.answer()


@router.callback_query(F.data == "premium_paid")
async def premium_paid(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.set_state(
        PremiumState.waiting_details
    )

    await callback.message.edit_text(
        """
💎 <b>Premium Purchase</b>
Please send the following details in ONE message.
-------------------------
🆔 Telegram ID
👤 Sender Account Name
💳 UTR / Transaction ID
-------------------------
Example:

<code>Telegram ID :123456789
Sender Name :Rahul Sharma
UTR/ Trx id :839201847281</code>
"""
    )

    await callback.answer()

ADMIN_ID = 8021449673


@router.message(PremiumState.waiting_details)
async def receive_payment_details(
    message: Message,
    state: FSMContext
):

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Approve",
                    callback_data=f"approve_premium_{message.from_user.id}"
                ),
                InlineKeyboardButton(
                    text="❌ Reject",
                    callback_data=f"reject_premium_{message.from_user.id}"
                )
            ]
        ]
    )

    await message.bot.send_message(
        ADMIN_ID,
        f"""
💎 <b>New Premium Purchase</b>
-------------------------
👤 User :{message.from_user.first_name}
🆔 User ID :<code>{message.from_user.id}</code>
📎 Username :@{message.from_user.username or "None"}
-------------------------
{message.text}
""",
        reply_markup=kb
    )

    await message.answer(
        """
✅ Premium request submitted.

Please wait while the admin verifies your payment.
"""
    )

    await state.clear()




@router.callback_query(F.data.startswith("approve_premium_"))
async def approve_premium(callback: CallbackQuery):

    user_id = int(
        callback.data.split("_")[2]
    )

    await UserRepository.set_premium(
        user_id,
        True
    )

    await callback.bot.send_message(
        user_id,
        """
🎉 <b>Premium Activated</b>
-------------------------
Congratulations!

Your Lifetime Premium Membership
has been activated.

Thank you for supporting
VTH Network ❤️
"""
    )

    await callback.message.edit_text(
        callback.message.html_text +
        "\n\n✅ <b>APPROVED</b>"
    )

    await callback.answer(
        "Premium Activated."
    )


@router.callback_query(F.data.startswith("reject_premium_"))
async def reject_premium(callback: CallbackQuery):

    user_id = int(
        callback.data.split("_")[2]
    )

    await callback.bot.send_message(
        user_id,
        """
❌ <b>Payment Rejected</b>
-------------------------
Your payment could not be verified.
•Reason : Fake payment proofs / payment not found
•Please contact :@vthnetsupport
if you believe this is a mistake.
"""
    )

    await callback.message.edit_text(
        callback.message.html_text +
        "\n\n❌ <b>REJECTED</b>"
    )

    await callback.answer(
        "Premium Rejected."
    )