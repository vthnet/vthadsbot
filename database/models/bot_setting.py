from datetime import datetime

from sqlalchemy import (
    BigInteger,
    String,
    Text,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.session import Base


class BotSetting(Base):

    __tablename__ = "bot_settings"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    page: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )

    text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    media_type: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    file_id: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    updated_by: Mapped[int | None] = mapped_column(
    BigInteger,
    nullable=True,
)

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )