from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True, index=True, autoincrement=True, comment='id')
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True, comment='email')
    password: Mapped[str] = mapped_column(String(256), comment='password')
    name: Mapped[str] = mapped_column(String(50), comment='name')
    phone: Mapped[str | None] = mapped_column(String(11), default=None, comment='phone number')
