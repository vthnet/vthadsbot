from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.engine import make_url

from config import config
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.engine import make_url

from config import config
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.engine import make_url

from config import config
print(config.DATABASE_URL)


class Base(DeclarativeBase):
    pass



url = make_url(
    config.DATABASE_URL.replace(
        "postgresql://",
        "postgresql+asyncpg://",
        1
    )
)


query = dict(url.query)


# Remove unsupported asyncpg/libpq parameters
query.pop(
    "sslmode",
    None
)

query.pop(
    "channel_binding",
    None
)


url = url.set(
    query=query
)



engine = create_async_engine(

    url,

    echo=False,

    connect_args={

        "ssl": "require",

        # Fix asyncpg cached statement errors
        "statement_cache_size": 0

    }

)



SessionLocal = async_sessionmaker(

    bind=engine,

    class_=AsyncSession,

    expire_on_commit=False

)


class Base(DeclarativeBase):
    pass



url = make_url(
    config.DATABASE_URL.replace(
        "postgresql://",
        "postgresql+asyncpg://",
        1
    )
)


query = dict(url.query)


# Remove unsupported asyncpg/libpq parameters
query.pop(
    "sslmode",
    None
)

query.pop(
    "channel_binding",
    None
)


url = url.set(
    query=query
)



engine = create_async_engine(

    url,

    echo=False,

    connect_args={

        "ssl": "require",

        # Fix asyncpg cached statement errors
        "statement_cache_size": 0

    }

)



SessionLocal = async_sessionmaker(

    bind=engine,

    class_=AsyncSession,

    expire_on_commit=False

)


class Base(DeclarativeBase):
    pass



url = make_url(
    config.DATABASE_URL.replace(
        "postgresql://",
        "postgresql+asyncpg://",
        1
    )
)


query = dict(url.query)


# Remove unsupported asyncpg/libpq parameters
query.pop(
    "sslmode",
    None
)

query.pop(
    "channel_binding",
    None
)


url = url.set(
    query=query
)



engine = create_async_engine(

    url,

    echo=False,

    connect_args={

        "ssl": "require",

        # Fix asyncpg cached statement errors
        "statement_cache_size": 0

    }

)



SessionLocal = async_sessionmaker(

    bind=engine,

    class_=AsyncSession,

    expire_on_commit=False

)