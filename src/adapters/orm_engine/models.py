from sqlalchemy import String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class AvailableSensors(Base):
    __tablename__ = 'available_sensors'
    sensor_id: Mapped[int] = mapped_column(
        primary_key=True, unique=True, nullable=False, autoincrement=True
    )
    description: Mapped[str] = mapped_column(String(100))


