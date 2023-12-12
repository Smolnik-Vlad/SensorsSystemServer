from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.core.choosing import ReactionChoose, EmergencyTelephoneNumber
from src.dataclasses.dataclasses import SensorDataClass, EmergencySettings, LogDataClass


class SensorCreate(BaseModel):
    name: str
    description: str | None
    reaction_type: ReactionChoose = ReactionChoose.LOGGING
    active: bool | None = True

    def to_entity(self):
        return SensorDataClass(
            name=self.name,
            description=self.description,
            reaction_type=self.reaction_type,
            active=self.active
        )


class SensorUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    reaction_type: ReactionChoose | None = None

    def to_entity(self):
        return SensorDataClass(
            name=self.name,
            description=self.description,
            reaction_type=self.reaction_type,
        )


class SensorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None
    reaction_type: ReactionChoose
    active: bool


class CallingToEmergencyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    emergency_telephone: str | None
    message: str | None


class SensorOnOffResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    active: bool


class SensorsResponse(BaseModel):
    sensors: list[SensorResponse] | None


class CallingEmergencyUpdate(BaseModel):
    emergency_telephone: EmergencyTelephoneNumber | None = None
    message: str | None = None

    def to_entity(self):
        return EmergencySettings(emergency_telephone=self.emergency_telephone,
                                 message=self.message)


class LogCreate(BaseModel):
    message: str = "Something is going wrong"

    def to_entity(self):
        return LogDataClass(
            message=self.message
        )


class LogResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    message: str
    time: datetime
