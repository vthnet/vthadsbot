from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.inline import home_keyboard

from database.repository.user_repo import UserRepository
from services.logger.logger import send_log

from handlers.user.force_join import (
    check_force_join,
    force_join_message,
    force_join_callback,
)

from handlers.admin.maintenance import maintenance_enabled

router = Router()

from services.cache.dashboard_cache import (
    get as dashboard_get,
    set as dashboard_set,
)
from aiogram.fsm.context import FSMContext
from utils.smart_edit import smart_edit
from database.repository.bot_setting_repo import BotSettingRepository
from utils.language import t



async def dashboard_text(user):

    cached = dashboard_get(user.id)

    if cached:
        return cached

    text = f"""
👋 <b>{await t(user.telegram_id, "welcome_user")}</b>

{await t(user.telegram_id, "choose_option")}
""".replace(
        "{name}",
        user.first_name
    )

    dashboard_set(
        user.id,
        text
    )

    return text


async def send_home(
    target,
    user,
    edit: bool = False
):

    keyboard = await home_keyboard(
        user.telegram_id
    )

    setting = await BotSettingRepository.get(
        "home"
    )

    if setting and setting.text:

        text = (
            setting.text
            .replace("{name}", user.first_name)
            .replace("{username}", user.username or "None")
            .replace("{userid}", str(user.telegram_id))
        )

    else:

        text = await dashboard_text(
            user
        )

    if edit:

        await target.edit_text(
            text,
            reply_markup=keyboard
        )

    else:

        await target.answer(
            text,
            reply_markup=keyboard
        )

@router.message(CommandStart())
async def start(message: Message):

    if maintenance_enabled():

        await message.answer(
            """
🛠 <b>Maintenance</b>

The bot is currently under maintenance.

Please try again later.
"""
        )
        return

    if not await check_force_join(
        message.from_user.id
    ):
        return await force_join_message(message)

    user = await UserRepository.get_user(
        message.from_user.id
    )

    if user is None:

        user = await UserRepository.create_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
        )

        await send_log(
            f"""
🆕 <b>New User</b>

👤 {message.from_user.first_name}

🆔 <code>{message.from_user.id}</code>

📎 @{message.from_user.username or "None"}
"""
        )

    await send_home(
        message,
        user
    )




@router.callback_query(F.data == "home")
async def home_callback(
    callback: CallbackQuery,
    state: FSMContext
):

    if maintenance_enabled():

        await callback.answer(
            "🛠 Bot is under maintenance.",
            show_alert=True
        )
        return

    if not await check_force_join(
        callback.from_user.id
    ):
        return await force_join_callback(callback)

    await state.clear()

    user = await UserRepository.get_user(
        callback.from_user.id
    )

    if not user:

        await callback.answer(
            "User not found.",
            show_alert=True
        )
        return

    await send_home(
        callback.message,
        user,
        edit=True
    )

    await callback.answer()