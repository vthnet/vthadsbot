from database.repository.user_repo import UserRepository

from locales.translator import tr


async def t(
    telegram_id: int,
    key: str
):

    user = await UserRepository.get_user(
        telegram_id
    )

    if user is None:
        return tr("en", key)

    return tr(
        user.language,
        key
    )