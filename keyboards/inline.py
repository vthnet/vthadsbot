from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import config



async def home_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📢 Create Campaign",
        callback_data="create_campaign"
    )

    kb.button(
        text="📂 My Campaigns",
        callback_data="my_campaigns"
    )

    kb.button(
        text="👤 My Accounts",
        callback_data="my_accounts"
    )

    kb.button(
        text="🛒 Buy Accounts",
        callback_data="buy_tg_acc"
    )

    kb.button(
        text="➕ Add Account",
        callback_data="add_account"
    )

    kb.button(
      text="🤖 Auto Bio",
        callback_data="bio_home"
    )

    kb.button(
        text="💎 Subscription",
        callback_data="subscription"
    )

    kb.button(
        text="📊 Dashboard",
        callback_data="dashboard"
    )

    kb.button(
        text="💰 Wallet",
        callback_data="wallet"
    )

    kb.button(
        text="💡 Feedback",
        callback_data="feedback"
    )

    kb.button(
        text="📖 Guide",
        callback_data="guide"
    )

    kb.button(
       text="🆘 Support",
        callback_data="support"
    )

    kb.adjust(2, 2, 2, 2, 2, 1)

    return kb.as_markup()


async def success_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.button(
       text="👤 My Accounts",
     callback_data="my_accounts"
   )

    kb.button(
      text="📢 Create Campaign",
      callback_data="create_campaign"
   )

    kb.adjust(1, 2)

    return kb.as_markup()


async def back_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🏠 home",
        callback_data="home"
    )

    kb.button(
        text="🔙 back",
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
    url=f"https://t.me/{config.BOT_USERNAME}?start=verify"
)
    

    kb.adjust(1)

    return kb.as_markup()