from aiogram import Router, F
from aiogram.types import CallbackQuery

from database.repository.account_repo import AccountRepository
from database.repository.campaign_repo import CampaignRepository
from database.repository.target_repo import TargetRepository

from keyboards.campaign import (
    campaign_list_keyboard,
    campaign_manage_keyboard,
)

from utils.smart_edit import smart_edit

router = Router()
from utils.loading import loading




@router.callback_query(F.data == "my_campaigns")
async def my_campaigns(callback: CallbackQuery):

    await loading(
    callback,
    "📢 Loading Campaigns..."
)

    user = await AccountRepository.get_user(
        callback.from_user.id
    )

    if not user:

        await callback.answer(
            "No account found.",
            show_alert=True
        )

        return

    campaigns = await CampaignRepository.get_user_campaigns(
        user.id
    )

    if not campaigns:

        await smart_edit(
            callback,
            """
📂 <b>My Campaigns</b>
--------------------------------------------------
•🤔 No campaigns found.
•Create your first campaign to start sending messages.
--------------------------------------------------
🟢 Ready to Create
""",
            campaign_list_keyboard([])
        )

        return

    total = len(campaigns)

    running = len(
        [c for c in campaigns if c.running]
    )

    paused = len(
        [c for c in campaigns if c.paused]
    )

    finished = len(
        [c for c in campaigns if c.completed]
    )

    stopped = len(
        [
            c for c in campaigns
            if (
                not c.running
                and not c.paused
                and not c.completed
            )
        ]
    )

    await smart_edit(
        callback,
        f"""
📢 <b>My Campaigns</b>
--------------------------------------------------
📦 Total Campaigns : <b>{total}</b>

🟢 Running : <b>{running}</b>

⏸ Paused : <b>{paused}</b>

✅ Completed : <b>{finished}</b>

🔴 Stopped : <b>{stopped}</b>
--------------------------------------------------
Select a campaign below.
""",
        campaign_list_keyboard(campaigns)
    )


@router.callback_query(
    F.data.startswith("open_campaign_")
)
async def open_campaign(callback: CallbackQuery):

    campaign_id = int(
        callback.data.split("_")[2]
    )

    campaign = await CampaignRepository.get_campaign(
        campaign_id
    )

    if not campaign:

        await callback.answer(
            "Campaign not found.",
            show_alert=True
        )

        return

    targets = await TargetRepository.get_targets(
        campaign.id
    )

    if campaign.completed:
        status = "✅ Finished"
    elif campaign.running:
        status = "🟢 Running"
    elif campaign.paused:
        status = "⏸ Paused"
    else:
        status = "🔴 Stopped"

    await smart_edit(
        callback,
        f"""
📢 <b>Campaign Details</b>
--------------------------------------------------
<blockquote>🆔 ID :<code>{campaign.id}</code>

📨 Message :{campaign.post_data}

👥 Targets :<b>{len(targets)}</b>

📊 Messages Sent :<b>{campaign.total_sent}</b>

⏱ Delay Between Groups :<b>{campaign.send_delay} sec</b>

🔁 Loop Delay :<b>{campaign.repeat_delay} sec</b>

📅 Created :<code>{campaign.created_at.strftime("%d-%m-%Y %H:%M")}</code>

🚦 Status :{status}</blockquote>
--------------------------------------------------
""",
        campaign_manage_keyboard(
            campaign.id,
            campaign.running,
            campaign.completed,
            campaign.paused
        )
    )