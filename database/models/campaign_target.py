from datetime import datetime

from sqlalchemy import (
    Integer,
    BigInteger,
    String,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import Mapped, mapped_column

from database.session import Base


class CampaignTarget(Base):

    __tablename__ = "campaign_targets"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    campaign_id: Mapped[int] = mapped_column(
        ForeignKey(
            "campaigns.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )


    chat_id: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )


    chat_username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )


    chat_title: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )