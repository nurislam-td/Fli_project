from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Flight, FlightUpdate, FlightUpdatePartial, FlightCreate
from .dependencies import flight_by_id
from database.databaseConnection import db_helper

router = APIRouter(tags=["Flight"])


@router.get("/{flight_id}", response_model=Flight)
async def get_flight(
    flight: Flight = Depends(flight_by_id),
):
    return flight


@router.get("/", response_model=list[Flight])
async def get_flights(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_flights(session)


@router.post("/", response_model=Flight)
async def create_flight(
    flight_create: FlightCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_flight(session=session, flight_create=flight_create)


@router.patch("/{flight_id}", response_model=Flight)
async def update_flight(
    flight_update: FlightUpdate | FlightUpdatePartial,
    flight: Flight = Depends(flight_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_flight(
        session=session, flight=flight, flight_update=flight_update, partial=True
    )


@router.delete("/{flight_id}", response_model=None)
async def delete_flight(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    flight=Depends(flight_by_id),
):
    return await crud.delete_flight(session=session, flight=flight)
