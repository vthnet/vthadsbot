from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from database.repository.user_repo import UserRepository

from keyboards.settings import language_keyboard
from utils.smart_edit import smart_edit

from handlers.user.start import home_callback

router = Router()


@router.callback_query(F.data == "language_menu")
async def language_menu(callback: CallbackQuery):

    await smart_edit(
        callback,
        """
🌐 <b>Select Language</b>

━━━━━━━━━━━━━━━━━━━━

Choose your preferred language.

The bot interface will
change instantly.
""",
        language_keyboard()
    )


@router.callback_query(F.data.startswith("lang_"))
async def change_language(
    callback: CallbackQuery,
    state: FSMContext
):

    language = callback.data.split("_")[1]

    await UserRepository.update_language(
        callback.from_user.id,
        language
    )

    await callback.answer(
        "✅ Language Updated",
        show_alert=True
    )

    await home_callback(
        callback,
        state
    )