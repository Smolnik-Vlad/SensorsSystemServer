import enum

from sqlalchemy import String, types, func, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

from src.core.choosing import ReactionChoose, EmergencyTelephoneNumber

Base = declarative_base()


class Sensor(Base):
    __tablename__ = 'sensor'
    id: Mapped[int] = mapped_column(
        primary_key=True, unique=True, nullable=False, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(String(100))
    reaction_type: Mapped[ReactionChoose] = mapped_column(server_default=ReactionChoose.LOGGING)
    active: Mapped[bool] = mapped_column(default=True)

    log: Mapped['Log'] = relationship(back_populates='sensor')
    calling_to_em: Mapped['CallingToEmergency'] = relationship(back_populates='sensor')


class Log(Base):
    __tablename__ = 'log'
    id: Mapped[int] = mapped_column(
        primary_key=True, unique=True, nullable=False, autoincrement=True
    )
    time: Mapped[types.DateTime] = mapped_column(types.DateTime, server_default=func.current_timestamp())
    message: Mapped[str] = mapped_column(String(250))
    sensor_id: Mapped[int] = mapped_column(ForeignKey("sensor.id", ondelete="SET NULL"))

    sensor: Mapped["Sensor"] = relationship(back_populates="log",
                                            cascade="all, delete",
                                            passive_deletes=True,
                                            lazy="joined", )


class CallingToEmergency(Base):
    __tablename__ = 'calling_to_emergency'
    id: Mapped[int] = mapped_column(
        primary_key=True, unique=True, nullable=False, autoincrement=True
    )
    emergency_telephone: Mapped[EmergencyTelephoneNumber] = mapped_column(default=EmergencyTelephoneNumber.COMMON)
    message: Mapped[str] = mapped_column(String(250))

    sensor_id: Mapped[int] = mapped_column(ForeignKey("sensor.id", ondelete="SET NULL"))
    sensor: Mapped["Sensor"] = relationship(back_populates="calling_to_em",
                                            cascade="all, delete",
                                            passive_deletes=True,
                                            lazy="joined", )
