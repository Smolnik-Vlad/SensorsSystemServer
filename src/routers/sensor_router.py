from fastapi import APIRouter, Depends
from starlette import status

from src.routers.depends.use_case_dependency import get_sensor_use_case
from src.routers.schemas.sensor_schema import SensorsResponse, SensorCreate
from src.usecases.sensor_usecase import SensorUseCase

sensor_router = APIRouter()


@sensor_router.get("get_sensors", response_model=SensorsResponse, status_code=status.HTTP_200_OK)
async def get_sensors(sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    return await sensor_management.get_list_of_sensors()


@sensor_router.post("add_sensor", response_model=SensorsResponse, status_code=status.HTTP_201_CREATED)
async def add_sensor(data: SensorCreate, sensor_management: SensorUseCase = Depends(get_sensor_use_case)):
    return await sensor_management.add_new_sensor(data.to_entity())
