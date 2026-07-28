import asyncio

from loader import bot, dp

from database.session import engine, Base
import database.models


# USER
from handlers.user.start import router as start_router


# CALLBACKS
from handlers.callback import router as callback_router


# ACCOUNTS
from handlers.account.accounts import router as account_router
from handlers.account.my_accounts import router as my_accounts_router
from handlers.account.account_manage import router as account_manage_router


# CAMPAIGNS
from handlers.campaign.create_campaign import router as campaign_router
from handlers.campaign.my_campaigns import router as my_campaigns_router
from handlers.campaign.manage_campaign import router as manage_campaign_router
from handlers.campaign.campaign_control import router as campaign_control_router


from services.campaign.campaign_worker import run_campaigns
from handlers.wallet import router as wallet_router
from handlers.dashboard.dashboard import (
    router as dashboard_router
)

from handlers.subscription import router as subscription_router
from handlers.admin.status import router as status_router
from handlers.admin.running import router as running_router

from handlers.campaign.loop_campaign import router as loop_campaign_router
from handlers.campaign.pause_campaign import router as pause_router
from handlers.admin.maintenance import router as maintenance_router
from handlers.buy_tg_acc import router as buy_tg_router

from handlers.campaign_loop import router as campaign_loop_router
from handlers.campaign_delay import router as campaign_delay_router
from handlers.campaign_confirm import router as campaign_confirm_router
from handlers.premium_buy import router as premium_buy_router
from services.bio.bio_worker import run_bio_worker
from handlers.admin.broadcast import router as broadcast_router
from handlers.set_commands import set_commands
from handlers.feedback import router as feedback_router
from handlers.admin import content_manager
from handlers.user import settings
from handlers.guide import router as guide_router
from handlers.support.support import router as support_router
from handlers.admin.support_reply import router as support_reply_router


from handlers.bio.menu import router as bio_menu_router
from handlers.bio.add import router as bio_add_router
from handlers.bio.delete import router as bio_delete_router
from handlers.bio.enable import router as bio_enable_router
from handlers.bio.disable import router as bio_disable_router
from handlers.bio.select_account import router as bio_account_router
from handlers.bio.select_bios import router as bio_bios_router
from handlers.bio.select_interval import router as bio_interval_router
from services.bio.rotation_worker import rotation_worker
import asyncio
from handlers.bio.time import router as bio_time_router
from services.bio.default_bio_worker import (
    default_bio_worker
)
from handlers.bio.change_interval import (
    router as bio_change_interval_router
)

from handlers.settings.menu import (
    router as settings_router
)

from handlers.settings.language import (
    router as language_router
)



async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )



async def main():

    await startup()
    await set_commands(bot)


    # USER
    dp.include_router(
        start_router
    )


    # CAMPAIGNS
    dp.include_router(campaign_router)
    dp.include_router(campaign_loop_router)
    dp.include_router(campaign_delay_router)
    dp.include_router(campaign_confirm_router)
    dp.include_router(my_campaigns_router)
    dp.include_router(manage_campaign_router)
    dp.include_router(campaign_control_router)


    # ACCOUNTS
    dp.include_router(
        account_router
    )

    dp.include_router(
        my_accounts_router
    )

    dp.include_router(
        account_manage_router
    )

    dp.include_router(settings.router)

    dp.include_router(
    support_router
)
    


    # CALLBACKS
    dp.include_router(
        callback_router
    )

    dp.include_router(
        wallet_router
    )

    dp.include_router(
    dashboard_router
)

    dp.include_router(
    guide_router
)



    dp.include_router(
        subscription_router
    )


    dp.include_router(status_router)
    dp.include_router(
            running_router
    )
    dp.include_router(
       maintenance_router
    )

    dp.include_router(
        buy_tg_router
    )

    dp.include_router(
        premium_buy_router
    )


    dp.include_router(
        loop_campaign_router
    )

    dp.include_router(
        pause_router
    )

    dp.include_router(
       broadcast_router
   )

    dp.include_router(
    support_reply_router
)

    dp.include_router(
        feedback_router
)


    dp.include_router(content_manager.router)



    dp.include_router(bio_menu_router)
    dp.include_router(bio_add_router)
    dp.include_router(bio_delete_router)
    dp.include_router(bio_enable_router)
    dp.include_router(bio_disable_router)
    dp.include_router(bio_account_router)
    dp.include_router(bio_bios_router)
    dp.include_router(bio_interval_router)
    dp.include_router(bio_time_router)
    dp.include_router(bio_change_interval_router)
    dp.include_router(settings_router)
    dp.include_router(language_router)

    # Start campaign worker ONLY ONCE
    asyncio.create_task(
        run_campaigns()
    )

    # Start bio worker ONLY ONCE
    asyncio.create_task(
        run_bio_worker()
    )


    print("=" * 50)
    print("🚀 VTH ADS BOT STARTED")
    print("=" * 50)


    asyncio.create_task(
    rotation_worker()
)


    asyncio.create_task(
    default_bio_worker()
)

    await dp.start_polling(bot)
    



if __name__ == "__main__":

    asyncio.run(
        main()
    )
