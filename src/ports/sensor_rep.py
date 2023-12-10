from abc import ABC, abstractmethod

from src.dataclasses.dataclasses import SensorDataClass


class SensorRepository(ABC):

    @abstractmethod
    async def get_all_sensors(self) -> list[SensorDataClass]:
        pass

    @abstractmethod
    async def add_new_sensor(self, sensor):
        pass
