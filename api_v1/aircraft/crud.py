from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from api_v1.aircraft.schemas import (
    AircraftCreate,
    AircraftUpdate,
    AircraftUpdatePartial,
)
from database.models import Aircraft


async def get_aircraft(session: AsyncSession, aircraft_id: int) -> Aircraft | None:
    return await session.get(Aircraft, aircraft_id)


async def get_aircrafts(session: AsyncSession) -> list[Aircraft]:
    stmt = select(Aircraft)
    result: Result = await session.execute(stmt)
    aircrafts = result.scalars().all()
    return list(aircrafts)


async def create_aircraft(
    session: AsyncSession, aircraft_in: AircraftCreate
) -> Aircraft:
    aircraft = Aircraft(**aircraft_in.model_dump())
    session.add(aircraft)
    await session.commit()
    return aircraft


async def update_aircraft(
    session: AsyncSession,
    aircraft: Aircraft,
    aircraft_update: AircraftUpdate | AircraftUpdatePartial,
    partial: bool = False,
) -> Aircraft:
    for key, value in aircraft_update.model_dump(exclude_unset=partial).items():
        setattr(aircraft, key, value)
    await session.commit()
    return aircraft


async def delete_aircraft(session: AsyncSession, aircraft: Aircraft) -> None:
    await session.delete(aircraft)
    await session.commit()
