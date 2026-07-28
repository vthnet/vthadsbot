from aiogram.utils.keyboard import InlineKeyboardBuilder


def campaigns_keyboard(accounts):

    kb = InlineKeyboardBuilder()

    for acc in accounts:
        kb.button(
            text=f"📱 {acc.account_name}",
            callback_data=f"campaign_account_{acc.id}"
        )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(1)

    return kb.as_markup()


def campaign_manage_keyboard(
    campaign_id,
    running=False,
    completed=False,
    paused=False
):

    kb = InlineKeyboardBuilder()

    # ==========================
    # COMPLETED
    # ==========================

    if completed:

        kb.button(
            text="🗑 Remove Campaign",
            callback_data=f"delete_campaign_{campaign_id}"
        )

        kb.button(
            text="📂 My Campaigns",
            callback_data="my_campaigns"
        )

        kb.button(
            text="🏠 Home",
            callback_data="home"
        )

        kb.adjust(1)

        return kb.as_markup()

    # ==========================
    # RUNNING / PAUSED / STOPPED
    # ==========================

    if paused:

        kb.button(
            text="▶ Resume",
            callback_data=f"pause_campaign_{campaign_id}"
        )

        kb.button(
            text="⏹ Stop",
            callback_data=f"stop_campaign_{campaign_id}"
        )

    elif running:

        kb.button(
            text="⏸ Pause",
            callback_data=f"pause_campaign_{campaign_id}"
        )

        kb.button(
            text="⏹ Stop",
            callback_data=f"stop_campaign_{campaign_id}"
        )

    else:

        kb.button(
            text="▶ Start",
            callback_data=f"start_campaign_{campaign_id}"
        )

    kb.button(
        text="🔁 Loop",
        callback_data=f"loop_campaign_{campaign_id}"
    )

    kb.button(
        text="⏱ Interval",
        callback_data=f"interval_campaign_{campaign_id}"
    )

    kb.button(
        text="📅 Schedule",
        callback_data=f"schedule_campaign_{campaign_id}"
    )

    kb.button(
        text="📊 Statistics",
        callback_data=f"stats_campaign_{campaign_id}"
    )

    kb.button(
        text="🗑 Delete",
        callback_data=f"delete_campaign_{campaign_id}"
    )

    kb.button(
        text="➕ New Campaign",
        callback_data="create_campaign"
    )

    kb.button(
        text="📂 My Campaigns",
        callback_data="my_campaigns"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(
        2,
        2,
        2,
        1,
        2,
        1
    )

    return kb.as_markup()



def my_campaigns_keyboard(campaigns):

    kb = InlineKeyboardBuilder()

    for campaign in campaigns:
        kb.button(
            text=f"📢 Campaign #{campaign.id}",
            callback_data=f"open_campaign_{campaign.id}"
        )

    kb.button(
        text="➕ New Campaign",
        callback_data="create_campaign"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(1)

    return kb.as_markup()


def campaign_list_keyboard(campaigns=None):

    kb = InlineKeyboardBuilder()

    if campaigns:

        for campaign in campaigns:
            kb.button(
                text=f"📢 Campaign #{campaign.id}",
                callback_data=f"open_campaign_{campaign.id}"
            )

    kb.button(
        text="➕ New Campaign",
        callback_data="create_campaign"
    )

    kb.button(
        text="🏠 Home",
        callback_data="home"
    )

    kb.adjust(1)

    return kb.as_markup()