from pydantic import BaseModel, ConfigDict


class AircraftBase(BaseModel):
    manufacturer: str
    model: str
    registration_number: str
    year_of_manufacturer: int
    capacity: int
    cnt_of_seats: int
    type: str
    fuel_capacity: float
    engine_type: str
    current_location: int


class Aircraft(AircraftBase):
    model_config = ConfigDict(from_attributes=True)
    aircraft_id: int


class AircraftCreate(AircraftBase):
    pass


class AircraftUpdate(AircraftBase):
    pass


class AircraftUpdatePartial(AircraftUpdate):
    manufacturer: str | None = None
    model: str | None = None
    registration_number: str | None = None
    year_of_manufacturer: int | None = None
    capacity: int | None = None
    cnt_of_seats: int | None = None
    type: str | None = None
    fuel_capacity: float | None = None
    engine_type: str | None = None
    current_location: int | None = None
