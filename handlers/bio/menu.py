from aiogram import Router, F
from aiogram.types import CallbackQuery

from database.repository.user_repo import UserRepository
from database.repository.bio_repo import BioRepository
from database.repository.bio_rotation_repo import BioRotationRepository
from database.repository.account_repo import AccountRepository

from keyboards.bio import bio_home_keyboard

from utils.smart_edit import smart_edit

router = Router()


@router.callback_query(F.data == "bio_home")
async def bio_home(callback: CallbackQuery):

    user = await UserRepository.get_user(
        callback.from_user.id
    )

    if not user:

        await callback.answer(
            "User not found.",
            show_alert=True
        )
        return

    if not user.is_premium:

        await callback.answer(
            """
🔒 PREMIUM FEATURE
• availableonly for Premium Members.
✨ Features :
• Store up to 5 Bios
• Automatic Bio Rotation
""",
            show_alert=True
        )
        return

    bios = await BioRepository.get_bios(
        user.id
    )

    accounts = await AccountRepository.get_accounts(
        user.id
    )

    running = 0
    current_interval = "Not Set"

    for account in accounts:

        rotation = await BioRotationRepository.get(
            account.id
        )

        if rotation and rotation.enabled:

            running += 1

            seconds = rotation.interval

            if seconds < 3600:

                current_interval = (
                    f"{seconds // 60} Minutes"
                )

            elif seconds < 86400:

                hours = seconds // 3600

                current_interval = (
                    "1 Hour"
                    if hours == 1
                    else f"{hours} Hours"
                )

            else:

                days = seconds // 86400

                current_interval = (
                    "1 Day"
                    if days == 1
                    else f"{days} Days"
                )

    available = len(accounts) - running

    await smart_edit(
        callback,
        f"""
🤖 <b>Auto Bio Manager</b>
--------------------------------------------------

📝 Saved Bios :<b>{len(bios)} / 5</b>
🟢 Active Rotations :<b>{running}</b>
⚪ Available Accounts :<b>{available}</b>
⏱ Current Interval :<b>{current_interval}</b>

--------------------------------------------------
Choose an option below.
""",
        bio_home_keyboard()
    )

    await callback.answer()