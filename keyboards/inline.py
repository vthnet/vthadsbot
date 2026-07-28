from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import config
from utils.language import t


async def home_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text=f"📢 {await t(user_id, 'create_campaign')}",
        callback_data="create_campaign"
    )

    kb.button(
        text=f"📂 {await t(user_id, 'my_campaigns')}",
        callback_data="my_campaigns"
    )

    kb.button(
        text=f"👤 {await t(user_id, 'my_accounts')}",
        callback_data="my_accounts"
    )

    kb.button(
        text=f"🛒 {await t(user_id, 'buy_accounts')}",
        callback_data="buy_tg_acc"
    )

    kb.button(
        text=f"➕ {await t(user_id, 'add_account')}",
        callback_data="add_account"
    )

    kb.button(
       text=f"🤖 {await t(user_id, 'auto_bio')}",
        callback_data="bio_home"
    )

    kb.button(
        text=f"💎 {await t(user_id, 'subscription')}",
        callback_data="subscription"
    )

    kb.button(
        text=f"📊 {await t(user_id, 'dashboard')}",
        callback_data="dashboard"
    )

    kb.button(
        text=f"💰 {await t(user_id, 'wallet')}",
        callback_data="wallet"
    )

    kb.button(
        text=f"💡 {await t(user_id, 'feedback')}",
        callback_data="feedback"
    )

    kb.button(
        text=f"⚙ {await t(user_id, 'settings')}",
        callback_data="settings"
    )

    kb.button(
        text=f"📖 {await t(user_id, 'guide')}",
        callback_data="guide"
    )

    kb.button(
        text=f"🆘 {await t(user_id, 'support')}",
        callback_data="support"
    )

    kb.adjust(2, 2, 2, 2, 2, 2, 1)

    return kb.as_markup()


async def success_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text=f"🏠 {await t(user_id, 'home')}",
        callback_data="home"
    )

    kb.button(
        text=f"👤 {await t(user_id, 'my_accounts')}",
        callback_data="my_accounts"
    )

    kb.button(
        text=f"📢 {await t(user_id, 'create_campaign')}",
        callback_data="create_campaign"
    )

    kb.adjust(1, 2)

    return kb.as_markup()


async def back_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text=f"🏠 {await t(user_id, 'home')}",
        callback_data="home"
    )

    kb.button(
        text=f"🔙 {await t(user_id, 'back')}",
        callback_data="home"
    )

    kb.adjust(2)

    return kb.as_markup()


def force_join_keyboard():

    kb = InlineKeyboardBuilder()

    if config.FORCE_JOIN_1:
        kb.button(
            text="📢 Channel 1",
            url=f"https://t.me/{config.FORCE_JOIN_1.replace('@','')}"
        )

    if config.FORCE_JOIN_2:
        kb.button(
            text="📢 Channel 2",
            url=f"https://t.me/{config.FORCE_JOIN_2.replace('@','')}"
        )

    kb.button(
        text="✅ I've Joined",
        callback_data="home"
    )

    kb.adjust(1)

    return kb.as_markup()