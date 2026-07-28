from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):

    commands = [

        BotCommand(
            command="start",
            description="🏠 Home"
        ),

        BotCommand(
            command="myaccounts",
            description="📱 My Accounts"
        ),

        BotCommand(
            command="addaccount",
            description="➕ Add Account"
        ),

        BotCommand(
            command="createcampaign",
            description="📢 Create Campaign"
        ),

        BotCommand(
            command="mycampaigns",
            description="📂 My Campaigns"
        ),

        BotCommand(
            command="statistics",
            description="📊 Statistics"
        ),

        BotCommand(
            command="wallet",
            description="💰 Wallet"
        ),

        BotCommand(
            command="subscription",
            description="💎 Premium"
        ),

        BotCommand(
            command="buytgacc",
            description="🛒 Buy Telegram Accounts"
        ),

        BotCommand(
            command="feedback",
            description="💡 Feedback"
        )

    ]

    await bot.set_my_commands(commands)