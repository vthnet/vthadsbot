from aiogram.utils.keyboard import InlineKeyboardBuilder


def target_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📂 All Joined Groups",
        callback_data="target_all_groups"
    )

    kb.button(
        text="➕ Add Group Manually",
        callback_data="target_manual"
    )

    kb.button(
        text="🔍 Search Group",
        callback_data="search_group"
    )

    kb.button(
        text="📥 Import Group List",
        callback_data="import_groups"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.button(
        text="🔙 Back",
        callback_data="create_campaign"
    )

    kb.adjust(
        1,
        1,
        1,
        1,
        2
    )

    return kb.as_markup()