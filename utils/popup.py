from aiogram.types import CallbackQuery


async def info(
    callback: CallbackQuery,
    text: str,
):
    await callback.answer(
        text,
        show_alert=True
    )


async def success(
    callback: CallbackQuery,
    text: str,
):
    await callback.answer(
        f"✅ SUCCESS\n\n{text}",
        show_alert=True
    )


async def error(
    callback: CallbackQuery,
    text: str,
):
    await callback.answer(
        f"❌ ERROR\n\n{text}",
        show_alert=True
    )


async def warning(
    callback: CallbackQuery,
    text: str,
):
    await callback.answer(
        f"⚠ WARNING\n\n{text}",
        show_alert=True
    )


async def loading(
    callback: CallbackQuery,
    title: str,
    seconds: str = "1–3 seconds",
):
    await callback.answer(
        f"""
⏳ {title}

Please wait...

This usually takes {seconds}.
""",
        show_alert=True
    )


async def premium(
    callback: CallbackQuery,
):
    await callback.answer(
        """
👑 PREMIUM FEATURE

This feature is available only
for Premium Members.

Upgrade to unlock all premium
features of VTH Ads Bot.
""",
        show_alert=True
    )


async def maintenance(
    callback: CallbackQuery,
):
    await callback.answer(
        """
🛠 UNDER MAINTENANCE

This feature is temporarily unavailable.

Please try again later.
""",
        show_alert=True
    )


async def coming_soon(
    callback: CallbackQuery,
):
    await callback.answer(
        """
🚀 COMING SOON

This feature is currently under development.

Stay tuned for future updates.
""",
        show_alert=True
    )


async def permission(
    callback: CallbackQuery,
):
    await callback.answer(
        """
🚫 ACCESS DENIED

You don't have permission
to perform this action.
""",
        show_alert=True
    )


async def campaign_risk(
    callback: CallbackQuery,
    level: str,
    message: str,
):
    await callback.answer(
        f"{level}\n\n{message}",
        show_alert=True
    )