from aiogram import Router, F
import asyncio
from aiogram.types import (
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from states.support import SupportState
from config import config
from database.repository.user_repo import UserRepository
from utils.smart_edit import smart_edit

router = Router()


@router.callback_query(F.data == "support")
async def support(callback: CallbackQuery):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📝 Report Problem",
        callback_data="report_problem"
    )

    kb.button(
        text="🏠 Back",
        callback_data="home",
        style="success",
                    icon_custom_emoji_id="5193119436621494267"
    )

    kb.adjust(1)

    await smart_edit(
        callback,
        """
🆘 <b>VTH SUPPORT</b>
--------------------------
• Thank you for choosing <b>VTH Ads Bot</b>. ❤️
• If you experience any bug, payment issue, campaign issue, or have any suggestion, please use the <b>Report Problem</b> button below.
• For direct support: @vthnetsupport
--------------------------
⚠ <b>Note</b>

• Due to our multiple VTH services, direct replies may take some time.

We highly recommend using <b>Report Problem</b>. Our team will review your request and contact you as soon as possible.
""",
        kb.as_markup(),
    )

    await callback.answer()


@router.callback_query(F.data == "report_problem")
async def report_problem(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.set_state(
        SupportState.waiting_issue
    )

    await smart_edit(
        callback,
        """
📝 <b>Describe Your Issue</b>
━━━━━━━━━━━━━━━━━━━━━━

Please describe your issue.

You may send:
• Text
• Photos
• Videos
• Documents
• Screenshots
"""
    )

    await state.update_data(
        support_message_id=callback.message.message_id
    )

    await callback.answer()


@router.message(SupportState.waiting_issue)
async def receive_issue(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()

    await state.update_data(
        issue_message_id=message.message_id,
        issue_chat_id=message.chat.id,
    )

    await state.set_state(
        SupportState.waiting_contact
    )

    await message.delete()

    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=data["support_message_id"],
        text="""
📬 <b>Contact Username</b>
━━━━━━━━━━━━━━━━━━━━━━

Please send the Telegram username
where our support team can contact you.

Example:
@yourusername
"""
    )


@router.message(SupportState.waiting_contact)
async def receive_contact(
    message: Message,
    state: FSMContext
):

    if not message.text or not message.text.startswith("@"):

        await message.answer(
            """
❌ <b>Invalid Username</b>

Please send a valid Telegram username.

Example:
@yourusername
"""
        )
        return

    data = await state.get_data()

    await message.delete()

    await message.bot.send_message(
        config.ADMINS[0],
        f"""
🚨 <b>NEW SUPPORT REQUEST</b>
-------------------------
👤 <b>Name</b> : {message.from_user.first_name}
🆔 <b>User ID</b> : <code>{message.from_user.id}</code>
📎 <b>Telegram Username</b> : @{message.from_user.username if message.from_user.username else 'None'}
📬 <b>Contact Username</b> : {message.text}

⬇️ Issue attached below.
""",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="💬 Reply",
                        callback_data=f"reply_support_{message.from_user.id}"
                    )
                ]
            ]
        )
    )

    await message.bot.copy_message(
        chat_id=config.ADMINS[0],
        from_chat_id=data["issue_chat_id"],
        message_id=data["issue_message_id"],
    )

    await state.clear()

    await UserRepository.get_user(
        message.from_user.id
    )

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🏠 Home",
        callback_data="home",
        style="success",
                    icon_custom_emoji_id="5193119436621494267"
    )

    await message.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=data["support_message_id"],
        text="""
✅ <b>Support Request Submitted</b>
━━━━━━━━━━━━━━━━━━━━━━

Your support request has been submitted successfully.

📞 Our support team will contact you
using the username you provided.

⏳ Please allow some time for a response.

❤️ Thank you for choosing
<b>VTH Ads Bot</b>.
━━━━━━━━━━━━━━━━━━━━━━
""",
        reply_markup=kb.as_markup()
    )