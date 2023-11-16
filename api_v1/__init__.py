from fastapi import APIRouter
from .airport.views import router as airport_router
from .aircraft.views import router as aircraft_router
from .flight.views import router as flight_router

router = APIRouter()
router.include_router(router=airport_router, prefix="/airports")
router.include_router(router=aircraft_router, prefix="/aircrafts")
router.include_router(router=flight_router, prefix="/flights")
