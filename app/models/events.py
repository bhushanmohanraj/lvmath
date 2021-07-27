from sqlalchemy import (
    Column,
    String,
    DateTime,
    Enum,
)

import enum

from .base import Model


class Event(Model):
    name = Column(
        String(100),
        unique=True,
        nullable=False,
    )

    start = Column(
        DateTime,
        nullable=False,
    )

    end = Column(
        DateTime,
        nullable=False,
    )

    class Category(enum.Enum):
        meeting = 1
        contest = 2

    category = Column(
        Enum(Category),
        nullable=False,
    )
