from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.account import AddAccount

from keyboards.inline import (
    back_keyboard,
    home_keyboard,
)

from services.sessions.client_manager import client_manager
from database.repository.account_repo import AccountRepository

from utils.smart_edit import smart_edit

from services.cache.dashboard_cache import clear
from services.bio.default_bio import apply_default_bio

router = Router()


@router.callback_query(F.data == "add_account")
async def add_account(
    callback: CallbackQuery,
    state: FSMContext,
):

    user = await AccountRepository.get_user(
        callback.from_user.id
    )

    accounts = await AccountRepository.get_accounts(
        user.id
    )

    limit = 10 if user.is_premium else 1

    if len(accounts) >= limit:

        if user.is_premium:

            await callback.answer(
                "❌ Maximum account limit reached.\n\nPremium users can add up to 10 Telegram accounts.",
                show_alert=True
            )

        else:

            await callback.answer(
                "👑 Premium Required\n\nFree users can add only 1 Telegram account.\n\nUpgrade to Premium to add up to 10 accounts.",
                show_alert=True
            )

        return

    await state.set_state(
        AddAccount.waiting_phone
    )

    await smart_edit(
        callback,
        """
📱 <b>Add Telegram Account</b>
--------------------------------------------------
• Send your phone number.
• Example : <code>+919876543210</code>
""",
        await back_keyboard(
            callback.from_user.id
        )
    )

    await state.update_data(
        flow_message_id=callback.message.message_id
    )


@router.message(AddAccount.waiting_phone)
async def get_phone(
    message: Message,
    state: FSMContext,
):

    phone = message.text.strip()

    await message.delete()

    data = await state.get_data()

    await message.bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data["flow_message_id"],
        caption="""
⏳ <b>Connecting to Telegram...</b>
--------------------------------------------------
Requesting OTP from Telegram.

Please wait...
"""
    )

    await state.update_data(
        phone=phone
    )

    await client_manager.send_code(
        message.from_user.id,
        phone,
    )

    await state.set_state(
        AddAccount.waiting_code
    )

    data = await state.get_data()

    await message.bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data["flow_message_id"],
        caption="""
📨 <b>OTP Sent Successfully</b>
--------------------------------------------------
Please enter the verification
code received on Telegram.
"""
    )


@router.message(AddAccount.waiting_code)
async def get_code(
    message: Message,
    state: FSMContext,
):

    await message.delete()

    data = await state.get_data()

    await message.bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data["flow_message_id"],
        caption="""
⏳ <b>Verifying OTP...</b>
--------------------------------------------------
Please wait...
"""
    )

    result = await client_manager.verify_code(
        message.from_user.id,
        data["phone"],
        message.text.strip(),
    )

    if result["status"] == "wrong_code":

        await message.bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=data["flow_message_id"],
            caption="""
❌ <b>Wrong OTP</b>
--------------------------------------------------
The verification code is incorrect.

Please enter the correct OTP.
"""
        )

        return

    if result["status"] == "password_required":

        await state.set_state(
            AddAccount.waiting_password
        )

        await message.bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=data["flow_message_id"],
            caption="""
🔐 <b>Two-Step Verification</b>
--------------------------------------------------
Your Telegram account
has Two-Step Verification.

Please send your password.
"""
        )

        return

    await save_account(
        message,
        state,
        result,
    )


@router.message(AddAccount.waiting_password)
async def get_password(
    message: Message,
    state: FSMContext,
):

    await message.delete()

    data = await state.get_data()

    await message.bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data["flow_message_id"],
        caption="""
⏳ <b>Logging In...</b>
--------------------------------------------------
Verifying your password...

Please wait...
"""
    )

    result = await client_manager.verify_password(
        message.from_user.id,
        message.text,
    )

    await save_account(
        message,
        state,
        result,
    )


async def save_account(
    message: Message,
    state: FSMContext,
    result,
):

    user = await AccountRepository.get_user(
        message.from_user.id
    )

    await AccountRepository.add_account(
        user.id,
        result["user"].first_name,
        result["user"].phone_number,
        result["session"],
    )

    if not user.is_premium:

        await apply_default_bio(
            result["session"]
        )

    clear(user.id)
    clear(user.id)

    data = await state.get_data()

    await state.clear()

    from aiogram.utils.keyboard import InlineKeyboardBuilder

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.button(
        text="👤 My Accounts",
        callback_data="my_accounts"
    )

    kb.adjust(2)

    await message.bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data["flow_message_id"],
        caption=f"""
✅ <b>Telegram Account Added Successfully</b>
--------------------------------------------------
👤 Account Name :<b>{result["user"].first_name}</b>

📱 Phone Number :<code>{result["user"].phone_number}</code>
--------------------------------------------------
🎉 Your Telegram account has been
added successfully.

You can now start creating
campaigns immediately.
""",
        reply_markup=kb.as_markup()
    )