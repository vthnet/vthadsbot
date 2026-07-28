from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Integer,
    Boolean,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.session import Base


class BioRotation(Base):

    __tablename__ = "bio_rotations"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey(
            "accounts.id",
            ondelete="CASCADE"
        )
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    interval: Mapped[int] = mapped_column(
        Integer,
        default=3600
    )

    current_index: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    last_changed: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )