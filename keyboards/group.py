from aiogram.utils.keyboard import InlineKeyboardBuilder


def groups_keyboard(groups, selected=None):

    kb = InlineKeyboardBuilder()

    selected = selected or []

    selected_count = 0

    for group in groups:

        group_id = group["id"]

        if group_id in selected:
            text = f"✅ {group['title']}"
            selected_count += 1
        else:
            text = f"⬜ {group['title']}"

        kb.button(
            text=text,
            callback_data=f"select_group_{group_id}"
        )

    kb.button(
        text="☑ Select All",
        callback_data="select_all_groups"
    )

    kb.button(
        text="❌ Unselect All",
        callback_data="unselect_all_groups"
    )

    kb.button(
        text=f"📊 Selected ({selected_count})",
        callback_data="selected_count"
    )

    kb.button(
        text="🔄 Refresh",
        callback_data="refresh_groups"
    )

    kb.button(
        text="➡ Continue",
        callback_data="continue_groups"
    )

    kb.button(
        text="🔙 Back",
        callback_data="target_all_groups"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(
        1,
        2,
        2,
        2
    )

    return kb.as_markup()