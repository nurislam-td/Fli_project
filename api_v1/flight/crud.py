from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from api_v1.flight.schemas import FlightCreate, FlightUpdate, FlightUpdatePartial
from database.models import Flight


async def get_flight(session: AsyncSession, flight_id: int) -> Flight | None:
    return await session.get(Flight, flight_id)


async def get_flights(session: AsyncSession) -> list[Flight]:
    stmt = select(Flight)
    result: Result = await session.execute(stmt)
    flights = result.scalars().all()
    return list(flights)


async def create_flight(session: AsyncSession, flight_create: FlightCreate) -> Flight:
    flight = Flight(**flight_create.model_dump())
    session.add(flight)
    await session.commit()
    return flight


async def update_flight(
    session: AsyncSession,
    flight: Flight,
    flight_update: FlightUpdate | FlightUpdatePartial,
    partial: bool,
) -> Flight:
    for key, val in flight_update.model_dump(exclude_unset=partial).items():
        setattr(flight, key, val)
    await session.commit()
    return flight


async def delete_flight(session: AsyncSession, flight: Flight) -> None:
    await session.delete(flight)
    await session.commit()


flight_in = FlightCreate(
    flight_number=104,
    departure_id=1,
    arrival_id=2,
    departure_time="2023-10-10T08:00:00",
    arrival_time="2023-10-10T12:00:00",
    aircraft_id=1,
    num_bsns_sts=20,
    num_stndrt_sts=160,
)

# from fastapi import Depends
# from sqlalchemy.ext.asyncio import AsyncSession
#
# print(flight_in)
# asyncio.run(
#     create_flight(
#         session=Depends(db_helper.scoped_session_dependency), flight_in=flight_in
#     )
# )
