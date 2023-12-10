from sqlalchemy import select, exc
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.orm_engine.models import Sensor
from src.core.exceptions import DatabaseException
from src.dataclasses.dataclasses import SensorDataClass
from src.ports.sensor_rep import SensorRepository


class SQLAlchemySensorRepository(SensorRepository):

    def __init__(self, db: AsyncSession):
        self.db_session = db

    @staticmethod
    def __from_model_to_dataclass(db_sensor: Sensor | None) -> SensorDataClass | None:
        if db_sensor is None:
            return None
        sensor = SensorDataClass(
            id=db_sensor.id,
            name=db_sensor.name,
            description=db_sensor.description,
            active=db_sensor.active,
            reaction_type=db_sensor.reaction_type
        )

        return sensor

    async def get_all_sensors(self) -> list[SensorDataClass]:
        # try:
        query = select(Sensor)
        users = await self.db_session.scalars(query)

        user_result = [self.__from_model_to_dataclass(user) for user in users.all()]
        return user_result
    # except exc.SQLAlchemyError:
    #     raise DatabaseException
