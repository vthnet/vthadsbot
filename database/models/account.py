from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Boolean,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.session import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    account_name: Mapped[str] = mapped_column(
        String(100)
    )

    phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    session_string: Mapped[str] = mapped_column(
        String
    )

    active_campaign: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )