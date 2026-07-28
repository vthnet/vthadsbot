from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()


class ReplyState(StatesGroup):
    waiting_reply = State()


@router.callback_query(F.data.startswith("reply_support_"))
async def reply_support(
    callback: CallbackQuery,
    state: FSMContext
):

    user_id = int(
        callback.data.split("_")[2]
    )

    await state.update_data(
        user_id=user_id
    )

    await state.set_state(
        ReplyState.waiting_reply
    )

    await callback.message.reply(
        f"""
💬 <b>Reply to User</b>

User ID:
<code>{user_id}</code>

━━━━━━━━━━━━━━━━━━━━━━

Send the message you want to deliver.
"""
    )

    await callback.answer()


@router.message(ReplyState.waiting_reply)
async def send_reply(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()

    user_id = data["user_id"]

    try:

        await message.bot.send_message(
            user_id,
            f"""
💬 <b>Reply From VTH Support</b>
━━━━━━━━━━━━━━━━━━━━━━
{message.text}
━━━━━━━━━━━━━━━━━━━━━━
❤️ Thank you for choosing VTH Ads Bot.
"""
        )

        await message.answer(
            "✅ Reply sent successfully."
        )

    except Exception:

        await message.answer(
            "❌ Failed to send reply."
        )

    await state.clear()