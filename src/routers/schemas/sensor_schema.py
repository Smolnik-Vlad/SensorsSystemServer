from pydantic import BaseModel, ConfigDict

from src.core.choosing import ReactionChoose, EmergencyTelephoneNumber
from src.dataclasses.dataclasses import SensorDataClass


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
    sensor_id: int


class SensorOnOffResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    active: bool


class SensorsResponse(BaseModel):
    sensors: list[SensorResponse] | None


class CallingEmergencyUpdate(BaseModel):
    emergency_telephone: EmergencyTelephoneNumber | None = None
    message: str | None = None
