from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.session import Base


class Bio(Base):

    __tablename__ = "bios"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        )
    )

    text: Mapped[str] = mapped_column(
        String(70)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )