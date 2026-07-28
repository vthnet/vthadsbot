from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

MAINTENANCE = False


def maintenance_enabled():
    return MAINTENANCE


@router.message(Command("maintenance"))
async def maintenance(message: Message):

    global MAINTENANCE

    args = message.text.split()

    if len(args) != 2:

        await message.answer(
            "Usage:\n/maintenance on\n/maintenance off"
        )

        return

    if args[1].lower() == "on":

        MAINTENANCE = True

        await message.answer(
            "✅ Maintenance Mode Enabled."
        )

    elif args[1].lower() == "off":

        MAINTENANCE = False

        await message.answer(
            "✅ Maintenance Mode Disabled."
        )

    else:

        await message.answer(
            "Use only:\n/maintenance on\n/maintenance off"
        )