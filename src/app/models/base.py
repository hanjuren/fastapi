from datetime import datetime

from sqlalchemy import BIGINT
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, DeclarativeBase, declared_attr


class DateTimeMixin(MappedAsDataclass):
    created_at: Mapped[datetime] = mapped_column(
        init=False,
        default_factory=datetime.now,
        sort_order=999,
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        onupdate=datetime.now,
        sort_order=999,
    )

class Base(DeclarativeBase, DateTimeMixin):
    type_annotation_map = {
        int: BIGINT,
    }

    @declared_attr.directive
    def __tablename__(self) -> str:
        return self.__name__.lower()
