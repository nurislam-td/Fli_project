from fastapi import APIRouter
from .airport.views import router as airport_router

router = APIRouter()
router.include_router(router=airport_router, prefix="/airports")
