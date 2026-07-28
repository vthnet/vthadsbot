from aiogram.utils.keyboard import InlineKeyboardBuilder


def support_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📝 Report Problem",
        callback_data="report_problem"
    )

    kb.button(
        text="🏠 Back",
        callback_data="home"
    )

    kb.adjust(1)

    return kb.as_markup()


def submit_report_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📨 Submit Report",
        callback_data="submit_report"
    )

    kb.button(
        text="❌ Cancel",
        callback_data="home"
    )

    kb.adjust(1)

    return kb.as_markup()