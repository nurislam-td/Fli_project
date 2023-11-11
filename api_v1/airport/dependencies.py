from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.airport import crud
from database.databaseConnection import db_helper
from database.models import Airport


async def airport_by_id(
    airport_id: Annotated[int, Path],
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
) -> Airport:
    airport = await crud.get_airport(session, airport_id)
    if airport:
        return airport
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Airport {airport_id} not found",
    )
