from pydantic import BaseModel, ConfigDict

from src.core.choosing import ReactionChoose
from src.dataclasses.dataclasses import SensorDataClass


class SensorCreate(BaseModel):
    name: str
    description: str | None
    reaction_type: ReactionChoose
    active: bool | None

    def to_entity(self):
        return SensorDataClass(
            name=self.name,
            description=self.description,
            reaction_type=self.reaction_type,
            active=self.active
        )


class SensorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None
    reaction_type: ReactionChoose
    active: bool


class SensorsResponse(BaseModel):
    sensors: list[SensorResponse] | None