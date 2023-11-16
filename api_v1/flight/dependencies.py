from fastapi import HTTPException, status, Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from api_v1.flight import crud
from database.databaseConnection import db_helper
from database.models import Flight


async def flight_by_id(
    flight_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Flight | None:
    flight = await crud.get_flight(session=session, flight_id=flight_id)
    if flight:
        return flight
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Flight {flight_id} not found"
    )
