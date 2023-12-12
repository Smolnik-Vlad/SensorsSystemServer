from datetime import datetime, timedelta

from src.dataclasses.dataclasses import SensorDataClass, SensorOnOff, EmergencySettings, LogDataClass
from src.ports.sensor_rep import SensorRepository
from src.routers.schemas.sensor_schema import SensorsResponse, SensorResponse, SensorOnOffResponse, \
    CallingToEmergencyResponse


class SensorUseCase:
    def __init__(self, sensor_repository: SensorRepository):
        self.sensor_rep = sensor_repository

    async def get_list_of_sensors(self):
        sensors = await self.sensor_rep.get_all_sensors()
        response = [SensorResponse.model_validate(sensor) for sensor in sensors]
        return SensorsResponse(sensors=response)

    async def add_new_sensor(self, sensor_data: SensorDataClass):
        result = await self.sensor_rep.add_new_sensor(sensor_data)
        return SensorResponse.model_validate(result)

    async def delete_sensor(self, sensor_id: int):
        await self.sensor_rep.delete_sensor(sensor_id)

    async def change_sensor_settings(self, sensor_id: int, sensor_data: SensorDataClass):
        result = await self.sensor_rep.change_sensor_settings(sensor_id, sensor_data)
        return SensorResponse.model_validate(result)

    async def switch_on_off(self):
        sensors = await self.sensor_rep.get_all_sensors()
        list_of_on = [sensor.active for sensor in sensors if sensor.active]
        list_of_off = [sensor.active for sensor in sensors if not sensor.active]
        sensor_on = SensorOnOff(active=True)
        sensor_off = SensorOnOff(active=False)
        if len(list_of_on) == 0:
            result = await self.sensor_rep.switch_on_off(sensor_on)
        elif len(list_of_off) == 0:
            result = await self.sensor_rep.switch_on_off(sensor_off)
        elif len(list_of_on) > len(list_of_off):
            result = await self.sensor_rep.switch_on_off(sensor_on)
        else:
            result = await self.sensor_rep.switch_on_off(sensor_off)

        print(f'res {result}')
        return SensorOnOffResponse.model_validate(result)

    async def configure_calling_to_emergency(self, sensor_id: int, data: EmergencySettings):
        result = await self.sensor_rep.change_emergency_call_settings(sensor_id, data)
        return CallingToEmergencyResponse.model_validate(result)

    async def create_new_log(self, sensor_id: int, data: LogDataClass):
        date = await self.sensor_rep.get_last_log(sensor_id)
        current_datetime = datetime.now()
        time_difference = current_datetime - date
        print(time_difference)
        if time_difference <= timedelta(minutes=1):
            await self.sensor_rep.add_log(sensor_id, data)

