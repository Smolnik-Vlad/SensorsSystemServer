from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.repositories.sqlalchemy_sensor_repository import SQLAlchemySensorRepository
from src.ports.sensor_rep import SensorRepository
from src.routers.depends.database_depends import get_db
from src.usecases.sensor_usecase import SensorUseCase


def get_sensor_repository(db: AsyncSession = Depends(get_db)) -> SensorRepository:
    return SQLAlchemySensorRepository(db)


def get_sensor_use_case(sensor_repository: SensorRepository = Depends(get_sensor_repository)) -> SensorUseCase:
    return SensorUseCase(sensor_repository=sensor_repository)
