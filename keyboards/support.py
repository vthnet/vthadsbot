from aiogram.utils.keyboard import InlineKeyboardBuilder


def support_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Report Problem",
        callback_data="report_problem",
        style="danger",
        icon_custom_emoji_id="5420323339723881652"
    )

    kb.button(
        text=" Back",
        callback_data="home",
        style="primary",
        icon_custom_emoji_id="5193119436621494267"
    )

    kb.adjust(1)

    return kb.as_markup()


def submit_report_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="Submit Report",
        callback_data="submit_report",
        style="success",
        icon_custom_emoji_id="4943195336911881191"
    )

    kb.button(
        text="Cancel",
        callback_data="home",
        style="danger",
        icon_custom_emoji_id="5846210329700217522"
    )

    kb.adjust(1)

    return kb.as_markup()