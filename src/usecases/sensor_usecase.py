from src.dataclasses.dataclasses import SensorDataClass
from src.ports.sensor_rep import SensorRepository
from src.routers.schemas.sensor_schema import SensorsResponse, SensorResponse


class SensorUseCase:
    def __init__(self, sensor_repository: SensorRepository):
        self.sensor_rep = sensor_repository

    async def get_list_of_sensors(self):
        sensors = await self.sensor_rep.get_all_sensors()
        response = [SensorResponse.model_validate(sensor) for sensor in sensors]
        return SensorsResponse(sensors=response)

    async def add_new_sensor(self, sensor_data: SensorDataClass):
        result = await self.sensor_rep.add_new_sensor(sensor_data)
        pass
