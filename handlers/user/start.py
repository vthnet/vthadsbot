from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.inline import home_keyboard
import time
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

from services.cache.home_cache import (
    get as home_get,
    set as home_set,
)
from aiogram.fsm.context import FSMContext
from utils.smart_edit import smart_edit
from database.repository.bot_setting_repo import BotSettingRepository



async def dashboard_text(user):

    cached = dashboard_get(user.id)

    if cached:
        return cached

    text = f"""
👋 <b>Welcome!</b>

Choose an option below.
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
    edit: bool = False,
):

    keyboard = await home_keyboard(user.telegram_id)

    setting = home_get("home")

    if setting is None:
        db = await BotSettingRepository.get("home")

        if db:
            setting = {
                "text": db.text,
                "media_type": db.media_type,
                "file_id": db.file_id,
            }
            home_set("home", setting)

    if setting and setting.get("text"):
        text = (
            setting["text"]
            .replace("{name}", user.first_name)
            .replace("{username}", user.username or "None")
            .replace("{userid}", str(user.telegram_id))
        )
    else:
        text = await dashboard_text(user)

    # PHOTO HOME
    if setting and setting.get("media_type") == "photo":

        if edit:
            try:
                await target.message.edit_caption(
                    caption=text,
                    reply_markup=keyboard,
                )
            except Exception:
                await target.message.answer_photo(
                    photo=setting["file_id"],
                    caption=text,
                    reply_markup=keyboard,
                )

        else:
            await target.answer_photo(
                photo=setting["file_id"],
                caption=text,
                reply_markup=keyboard,
            )

    # TEXT HOME
    else:

        if edit:
            await smart_edit(
                target,
                text,
                keyboard,
            )

        else:
            await target.answer(
                text,
                reply_markup=keyboard,
            )

@router.message(CommandStart())
async def start(message: Message):

    total_timer = time.perf_counter()

    if maintenance_enabled():

        await message.answer(
            """
🛠 <b>Maintenance</b>

The bot is currently under maintenance.

Please try again later.
"""
        )
        return

    timer = time.perf_counter()

    if not await check_force_join(
        message.from_user.id
    ):

        print(f"Force Join: {time.perf_counter() - timer:.3f}s")
        return await force_join_message(message)

    print(f"Force Join: {time.perf_counter() - timer:.3f}s")

    timer = time.perf_counter()

    user = await UserRepository.get_user(
        message.from_user.id
    )

    print(f"Get User: {time.perf_counter() - timer:.3f}s")

    if user is None:

        timer = time.perf_counter()

        user = await UserRepository.create_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
        )

        print(f"Create User: {time.perf_counter() - timer:.3f}s")

        await send_log(
            f"""
🆕 <b>New User</b>

👤 {message.from_user.first_name}

🆔 <code>{message.from_user.id}</code>

📎 @{message.from_user.username or "None"}
"""
        )

    timer = time.perf_counter()

    await send_home(
        message,
        user
    )

    print(f"Send Home: {time.perf_counter() - timer:.3f}s")
    print(f"START TOTAL: {time.perf_counter() - total_timer:.3f}s")

@router.callback_query(F.data == "home")
async def home_callback(
    callback: CallbackQuery,
    state: FSMContext
):

    total_timer = time.perf_counter()

    if maintenance_enabled():

        await callback.answer(
            "🛠 Bot is under maintenance.",
            show_alert=True
        )
        return

    timer = time.perf_counter()

    if not await check_force_join(
        callback.from_user.id
    ):
        return await force_join_callback(callback)

    print(f"Force Join: {time.perf_counter() - timer:.3f}s")

    timer = time.perf_counter()

    await state.clear()

    print(f"State Clear: {time.perf_counter() - timer:.3f}s")

    timer = time.perf_counter()

    user = await UserRepository.get_user(
        callback.from_user.id
    )

    print(f"Get User: {time.perf_counter() - timer:.3f}s")

    if not user:

        await callback.answer(
            "User not found.",
            show_alert=True
        )
        return

    timer = time.perf_counter()

    await send_home(
    callback,
    user,
    edit=True,
)

    print(f"Send Home: {time.perf_counter() - timer:.3f}s")
    print(f"HOME TOTAL: {time.perf_counter() - total_timer:.3f}s")

    await callback.answer()