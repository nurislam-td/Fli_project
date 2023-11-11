from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Airport
from sqlalchemy import select
from .schemas import AirportCreate, AirportUpdate, AirportUpdatePartial


async def get_airports(session: AsyncSession) -> list[Airport]:
    stmt = select(Airport)
    result: Result = await session.execute(stmt)
    airports = result.scalars().all()
    print(type(airports))
    return list(airports)


async def get_airport(session: AsyncSession, airport_id: int) -> Airport | None:
    return await session.get(Airport, airport_id)


async def create_airport(session: AsyncSession, airport_in: AirportCreate) -> Airport:
    airport = Airport(**airport_in.model_dump())
    session.add(airport)
    await session.commit()
    return airport


async def update_airport(
    session: AsyncSession,
    airport: Airport,
    airport_update: AirportUpdate | AirportUpdatePartial,
    partial: bool = False,
) -> Airport:
    for key, value in airport_update.model_dump(exclude_unset=partial).items():
        setattr(airport, key, value)
    await session.commit()
    return airport


async def delete_airport(
    session: AsyncSession,
    airport: Airport,
) -> None:
    await session.delete(airport)
    await session.commit()
