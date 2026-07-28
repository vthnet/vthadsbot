from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from database.repository.user_repo import UserRepository
from utils.language import t
from utils.smart_edit import smart_edit
from utils.loading import loading

router = Router()


@router.callback_query(F.data == "settings")
async def settings(callback: CallbackQuery):

    await loading(
        callback,
        "⚙ Loading Settings..."
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🌐 Language",
                    callback_data="language"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏠 Home",
                    callback_data="home"
                )
            ]
        ]
    )

    await smart_edit(
        callback,
        await t(
            callback.from_user.id,
            "settings"
        ),
        kb
    )


@router.callback_query(F.data == "language")
async def language(callback: CallbackQuery):

    await loading(
        callback,
        "🌐 Loading Languages..."
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🇺🇸 English",
                    callback_data="lang_en"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🇷🇺 Русский",
                    callback_data="lang_ru"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🇨🇳 中文",
                    callback_data="lang_zh"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏠 Home",
                    callback_data="home"
                )
            ]
        ]
    )

    await smart_edit(
        callback,
        "🌐 <b>Select Language</b>",
        kb
    )


@router.callback_query(F.data.startswith("lang_"))
async def change_language(callback: CallbackQuery):

    language = callback.data.split("_")[1]

    await UserRepository.update_language(
        callback.from_user.id,
        language
    )

    await callback.answer(
        "✅ Language Updated",
        show_alert=True
    )

    await settings(callback)