from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import Base


class MyTable(Base):
    __tablename__ = 'my_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column()