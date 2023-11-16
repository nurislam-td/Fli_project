from typing import Annotated
from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.aircraft import crud
from database.databaseConnection import db_helper
from database.models import Aircraft


async def aircraft_by_id(
    aircraft_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Aircraft:
    aircraft = await crud.get_aircraft(session=session, aircraft_id=aircraft_id)
    if aircraft:
        return aircraft
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Aircraft {aircraft_id} not found",
    )
