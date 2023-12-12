from fastapi import APIRouter, Depends
from starlette import status

from src.routers.depends.use_case_dependency import get_sensor_use_case
from src.routers.schemas.sensor_schema import SensorsResponse, SensorCreate, SensorResponse, SensorUpdate, \
    SensorOnOffResponse, CallingToEmergencyResponse, CallingEmergencyUpdate, LogCreate
from src.usecases.sensor_usecase import SensorUseCase

sensor_router = APIRouter()


@sensor_router.get("/get_sensors", response_model=SensorsResponse, status_code=status.HTTP_200_OK)
async def get_sensors(sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    return await sensor_management.get_list_of_sensors()


@sensor_router.post("", response_model=SensorResponse, status_code=status.HTTP_201_CREATED)
async def add_sensor(data: SensorCreate, sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    return await sensor_management.add_new_sensor(data.to_entity())


@sensor_router.delete("/{sensor_id}", status_code=status.HTTP_205_RESET_CONTENT)
async def delete_sensor(sensor_id: int, sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    return await sensor_management.delete_sensor(sensor_id)


@sensor_router.patch("/{sensor_id}", response_model=SensorResponse, status_code=status.HTTP_200_OK)
async def delete_sensor(sensor_id: int, data: SensorUpdate,
                        sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    return await sensor_management.change_sensor_settings(sensor_id, data.to_entity())


@sensor_router.post("/switch_on_off", response_model=SensorOnOffResponse, status_code=status.HTTP_200_OK)
async def switch_on_off(sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    return await sensor_management.switch_on_off()


@sensor_router.post("/{sensor_id}/configure_calling_to_emergency", response_model=CallingToEmergencyResponse,
                    status_code=status.HTTP_200_OK)
async def configure_calling_to_emergency(sensor_id: int, data: CallingEmergencyUpdate,
                                         sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    return await sensor_management.configure_calling_to_emergency(sensor_id, data.to_entity())


@sensor_router.post("/{sensor_id}/new_log", status_code=status.HTTP_201_CREATED)
async def create_log(sensor_id: int, data: LogCreate, sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    await sensor_management.create_new_log(sensor_id, data.to_entity())
