from sqlalchemy import select

from database.session import SessionLocal
from database.models.bot_setting import BotSetting


class BotSettingRepository:

    @staticmethod
    async def get(page: str):

        async with SessionLocal() as session:

            result = await session.execute(
                select(BotSetting).where(
                    BotSetting.page == page
                )
            )

            return result.scalar_one_or_none()


    @staticmethod
    async def save(
        page: str,
        text: str | None,
        media_type: str | None,
        file_id: str | None,
        admin_id: int,
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(BotSetting).where(
                    BotSetting.page == page
                )
            )

            setting = result.scalar_one_or_none()

            if setting is None:

                setting = BotSetting(
                    page=page
                )

                session.add(setting)

            setting.text = text
            setting.media_type = media_type
            setting.file_id = file_id
            setting.updated_by = admin_id

            await session.commit()