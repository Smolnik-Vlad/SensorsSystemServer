from abc import ABC, abstractmethod

from src.dataclasses.dataclasses import SensorDataClass, SensorOnOff, EmergencySettings, LogDataClass


class SensorRepository(ABC):

    @abstractmethod
    async def get_all_sensors(self) -> list[SensorDataClass]:
        pass

    @abstractmethod
    async def add_new_sensor(self, data: SensorDataClass) -> SensorDataClass:
        pass

    @abstractmethod
    async def delete_sensor(self, sensor_id: int):
        pass

    @abstractmethod
    async def change_sensor_settings(self, sensor_id: int, data: SensorDataClass) -> SensorDataClass:
        pass

    @abstractmethod
    async def switch_on_off(self, data: SensorOnOff) -> SensorOnOff:
        pass

    @abstractmethod
    async def change_emergency_call_settings(self, sensor_id: int, data: EmergencySettings):
        pass

    @abstractmethod
    async def add_log(self, sensor_id: int, data: LogDataClass):
        pass

    @abstractmethod
    async def get_last_log(self, sensor_id: int):
        pass




