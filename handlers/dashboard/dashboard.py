from aiogram import Router, F
from aiogram.types import CallbackQuery

from database.repository.user_repo import UserRepository
from database.repository.dashboard_repo import DashboardRepository

from keyboards.dashboard import dashboard_keyboard
from utils.smart_edit import smart_edit

router = Router()


@router.callback_query(F.data == "dashboard")
async def dashboard(callback: CallbackQuery):

    user = await UserRepository.get_user(
        callback.from_user.id
    )

    stats = await DashboardRepository.get(
        user
    )

    membership = (
        "👑 Premium ⭐"
        if stats["premium"]
        else "🆓 Free"
    )

    rotation = (
        "🟢 Enabled"
        if stats["rotation_enabled"]
        else "🔴 Disabled"
    )

    await smart_edit(
        callback,
        f"""
📊 <b>Your Dashboard</b>
-------------------------
<blockquote>👤 <b>Accounts</b></blockquote>
🟢 Active :<b>{stats["active_accounts"]}</b>
🔴 Expired :<b>{stats["expired_accounts"]}</b>
📱 Total :<b>{stats["total_accounts"]}/{stats["account_limit"]}</b>
-------------------------
<blockquote>📢 <b>Campaigns</b></blockquote>
📂 Total :<b>{stats["total_campaigns"]}</b>
🟢 Running :<b>{stats["running_campaigns"]}</b>
⏸ Stopped :<b>{stats["stopped_campaigns"]}</b>
✅ Completed :<b>{stats["completed_campaigns"]}</b>
-------------------------
<blockquote>🤖 <b>Auto Bio</b></blockquote>
📝 Saved Bios :<b>{stats["saved_bios"]}/5</b>
🔄 Rotation :<b>{rotation}</b>
-------------------------
<blockquote>📨 <b>Messages</b></blockquote>
✅ Sent :<b>{stats["total_sent"]}</b>
❌ Failed :<b>{stats["failed_sent"]}</b>
-------------------------
{membership}
""",
        dashboard_keyboard()
    )