from sqlalchemy import (
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from database.session import Base


class BioRotationItem(Base):

    __tablename__ = "bio_rotation_items"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    rotation_id: Mapped[int] = mapped_column(
        ForeignKey(
            "bio_rotations.id",
            ondelete="CASCADE"
        )
    )

    bio_id: Mapped[int] = mapped_column(
        ForeignKey(
            "bios.id",
            ondelete="CASCADE"
        )
    )