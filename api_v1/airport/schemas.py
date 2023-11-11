from pydantic import BaseModel, ConfigDict


class AirportBase(BaseModel):
    airport_code: str
    airport_name: str
    city: str
    country: str
    latitude: float
    longitude: float


class AirportCreate(AirportBase):
    pass


class AirportUpdate(AirportBase):
    pass


class AirportUpdatePartial(AirportUpdate):
    airport_code: str | None = None
    airport_name: str | None = None
    city: str | None = None
    country: str | None = None
    latitude: float | None = None
    longitude: float | None = None


class Airport(AirportBase):
    model_config = ConfigDict(from_attributes=True)
    airport_id: int
