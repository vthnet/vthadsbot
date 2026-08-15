from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import config



async def home_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Create Campaign",
        callback_data="create_campaign",
        style="primary",
        icon_custom_emoji_id="5399967660052081305"
    )

    kb.button(
        text="My Campaigns",
        callback_data="my_campaigns",
        style="primary",
        icon_custom_emoji_id="5409111052719767901"
    )

    kb.button(
        text="My Accounts",
        callback_data="my_accounts",
        style="primary",
        icon_custom_emoji_id="5346136537123801643"
    )

    kb.button(
        text="Buy Accounts",
        callback_data="buy_tg_acc",
        style="primary",
        icon_custom_emoji_id="6296218646284863141"
    )

    kb.button(
        text="Add Account",
        callback_data="add_account",
        style="primary",
        icon_custom_emoji_id="5287354223141342798"
    )

    kb.button(
      text="Auto Bio",
        callback_data="bio_home",
        style="primary",
        icon_custom_emoji_id="5296447931627352804"
    )

    kb.button(
        text="Subscription",
        callback_data="subscription",
        style="primary",
        icon_custom_emoji_id="6276092098823327414"
    )

    kb.button(
        text="Dashboard",
        callback_data="dashboard",
        style="primary",
        icon_custom_emoji_id="6084477132254218612"
    )

    kb.button(
        text="Wallet",
        callback_data="wallet",
        style="primary",
        icon_custom_emoji_id="5417924076503062111"
    )

    kb.button(
        text="Feedback",
        callback_data="feedback",
        style="primary",
        icon_custom_emoji_id="5193127592764394874"
    )

    kb.button(
        text="Guide",
        callback_data="guide",
        style="primary",
        icon_custom_emoji_id="5237714391293520323"
    )

    kb.button(
       text="Support",
        callback_data="support",
        style="primary",
        icon_custom_emoji_id="5866185084427572234"
    )

    kb.adjust(2, 2, 2, 2, 2, 1)

    return kb.as_markup()


async def success_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Home",
        callback_data="home",
        style="success",
        icon_custom_emoji_id="5193119436621494267"
    )

    kb.button(
       text="My Accounts",
     callback_data="my_accounts",
     style="primary",
     icon_custom_emoji_id="5346136537123801643"
   )

    kb.button(
      text="Create Campaign",
      callback_data="create_campaign",
      style="primary",
      icon_custom_emoji_id="5287354223141342798"
   )

    kb.adjust(1, 2)

    return kb.as_markup()


async def back_keyboard(user_id: int):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="home",
        callback_data="home",
        style="success",
        icon_custom_emoji_id="5193119436621494267"
    )

    kb.button(
        text="back",
        callback_data="home",
        style="danger",
        icon_custom_emoji_id="5409284148491726576"
    )

    kb.adjust(2)

    return kb.as_markup()


def force_join_keyboard():

    kb = InlineKeyboardBuilder()

    if config.FORCE_JOIN_1:
        kb.button(
            text="Channel 1",
            url=f"https://t.me/{config.FORCE_JOIN_1.replace('@','')}",
            style="primary",
            icon_custom_emoji_id="6129650743575060215"
        )

    if config.FORCE_JOIN_2:
        kb.button(
            text="Channel 2",
            url=f"https://t.me/{config.FORCE_JOIN_2.replace('@','')}",
            style="primary",
            icon_custom_emoji_id="6129650743575060215"
        )

    kb.button(
    text="I've Joined",
    url=f"https://t.me/{config.BOT_USERNAME}?start=verify",
    style="success",
    icon_custom_emoji_id="4987757216040747796"
)
    

    kb.adjust(1)

    return kb.as_markup()