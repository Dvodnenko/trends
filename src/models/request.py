from dataclasses import dataclass

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from ..db import Base


class Request(Base):

    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )

    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    response: Mapped[str] = mapped_column(Text, nullable=False)
