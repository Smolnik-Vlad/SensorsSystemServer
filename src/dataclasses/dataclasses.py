from abc import ABC
from dataclasses import dataclass

from src.core.choosing import EmergencyTelephoneNumber


class DataClassFunctionality(ABC):
    def to_dict(self, exclude_none=True) -> dict:
        if exclude_none:
            return {k: v for k, v in self.__dict__.items() if v is not None}
        else:
            return self.__dict__.copy()


@dataclass
class SensorDataClass(DataClassFunctionality):
    name: str
    id: int | None = None
    description: str | None = None
    active: bool | None = None
    reaction_type: str | None = None


@dataclass
class SensorOnOff(DataClassFunctionality):
    active: bool | None = None


@dataclass
class EmergencySettings(DataClassFunctionality):
    emergency_telephone: EmergencyTelephoneNumber | None = None
    message: str | None = None
