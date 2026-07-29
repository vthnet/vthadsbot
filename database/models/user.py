from datetime import datetime

from sqlalchemy import (
    BigInteger,
    String,
    Boolean,
    Integer,
    DateTime,
)

from sqlalchemy.orm import Mapped, mapped_column

from database.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        index=True,
    )

    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(255),
    )


    account_slots: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    wallet: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    is_premium: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )


    custom_bio: Mapped[str | None] = mapped_column(
         String(70),
         nullable=True,
    )




    is_banned: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )