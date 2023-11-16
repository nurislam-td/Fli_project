from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.databaseConnection import db_helper
from . import crud
from .dependencies import airport_by_id
from .schemas import Airport, AirportUpdate, AirportCreate, AirportUpdatePartial

router = APIRouter(tags=["Airport"])


@router.get("/", response_model=list[Airport])
async def get_airports(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_airports(session=session)


@router.get("/{airport_id}", response_model=Airport)
async def get_airport(
    airport: Airport = Depends(airport_by_id),
):
    return airport


@router.post("/", response_model=Airport)
async def create_airport(
    airport_in: AirportCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_airport(session=session, airport_in=airport_in)


@router.patch("/{airport_id}", response_model=Airport)
async def update_airport(
    airport_update: AirportUpdate | AirportUpdatePartial,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    airport=Depends(airport_by_id),
):
    return await crud.update_airport(
        session=session,
        airport=airport,
        airport_update=airport_update,
        partial=True,
    )


@router.delete("/{airport_id}", response_model=None)
async def delete_airport(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    airport: Airport = Depends(airport_by_id),
):
    return await crud.delete_airport(session=session, airport=airport)
