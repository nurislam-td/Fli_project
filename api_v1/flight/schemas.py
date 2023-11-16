from pydantic import BaseModel, ConfigDict
from datetime import datetime


class FlightBase(BaseModel):
    flight_number: int
    departure_id: int
    arrival_id: int
    departure_time: datetime
    arrival_time: datetime
    aircraft_id: int
    num_bsns_sts: int
    num_stndrt_sts: int


class FlightCreate(FlightBase):
    pass


class FlightUpdate(FlightBase):
    pass


class FlightUpdatePartial(FlightBase):
    flight_number: int | None = None
    departure_id: int | None = None
    arrival_id: int | None = None
    departure_time: datetime | None = None
    arrival_time: datetime | None = None
    aircraft_id: int | None = None
    num_bsns_sts: int | None = None
    num_stndrt_sts: int | None = None


class Flight(FlightBase):
    model_config = ConfigDict(from_attributes=True)
    flight_id: int
