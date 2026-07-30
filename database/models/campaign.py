from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.models.user import Base


class Campaign(Base):

    __tablename__ = "campaigns"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey(
            "accounts.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="New Campaign"
    )

    post_data: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # Delay between sending messages to groups (seconds)
    send_delay: Mapped[int] = mapped_column(
        Integer,
        default=3
    )

    # Delay after one completed loop (seconds)
    repeat_delay: Mapped[int] = mapped_column(
        Integer,
        default=86400
    )

    # Total successful sends
    total_sent: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    # Failed sends
    failed_sent: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    # Current target being processed
    current_target: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    # Campaign started time
    started_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    # Campaign finished time
    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    # Campaign running state
    running: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # Campaign completed
    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # Loop settings
    loop_count: Mapped[int] = mapped_column(
        Integer,
        default=1
    )

    completed_loops: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    infinite: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # Pause support
    paused: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # Scheduler
    scheduled_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    last_run: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    next_run: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

