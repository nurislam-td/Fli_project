from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.aircraft import crud
from api_v1.aircraft.schemas import (
    Aircraft,
    AircraftCreate,
    AircraftUpdate,
    AircraftUpdatePartial,
)
from database.databaseConnection import db_helper
from .dependencies import aircraft_by_id

router = APIRouter(tags=["Aircraft"])


@router.get("/", response_model=list[Aircraft])
async def get_aircrafts(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_aircrafts(session=session)


@router.get("/{aircraft_id}", response_model=Aircraft)
async def get_aircraft(aircraft: Aircraft = Depends(aircraft_by_id)):
    return aircraft


@router.post("/", response_model=Aircraft)
async def create_aircraft(
    aircraft_in: AircraftCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_aircraft(aircraft_in=aircraft_in, session=session)


@router.patch("/{aircraft_id}", response_model=Aircraft)
async def update_aircraft(
    aircraft_update: AircraftUpdate | AircraftUpdatePartial,
    aircraft: Aircraft = Depends(aircraft_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Aircraft:
    return await crud.update_aircraft(
        session=session,
        aircraft=aircraft,
        aircraft_update=aircraft_update,
        partial=True,
    )


@router.delete("/{aircraft_id}", response_model=None)
async def delete_aircraft(
    aircraft: Aircraft = Depends(aircraft_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_aircraft(session=session, aircraft=aircraft)
