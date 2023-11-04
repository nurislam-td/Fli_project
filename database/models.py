from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    DateTime,
    Date,
    ForeignKey,
)

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Airport(Base):
  __tablename__ = "airport"

  airport_id = Column(Integer, primary_key=True)
  airport_code = Column(String(3), unique=True)
  airport_name = Column(String(255))
  city = Column(String(255))
  country = Column(String(255))
  latitude = Column(Numeric(9, 6))
  longitude = Column(Numeric(9, 6))


class DimPosition(Base):
  __tablename__ = "dim_position"

  id = Column(Integer, primary_key=True)
  position_name = Column(String(255))


class Passenger(Base):
  __tablename__ = "passenger"

  passenger_id = Column(Integer, primary_key=True)
  name = Column(String(255))
  last_name = Column(String(255))
  date_of_birth = Column(Date)
  passport = Column(Integer, unique=True)
  contact_info = Column(String(50))


class Aircraft(Base):
  __tablename__ = "aircraft"

  aircraft_id = Column(Integer, primary_key=True)
  manufacturer = Column(String(255))
  model = Column(String(255))
  registration_number = Column(String(20), unique=True)
  year_of_manufacturer = Column(Integer)
  capacity = Column(Integer)
  cnt_of_seats = Column(Integer)
  type = Column(String(255))
  fuel_capacity = Column(Numeric(10, 2))
  engine_type = Column(String(100))
  current_location = Column(Integer, ForeignKey("airport.airport_id"))
  location = relationship("Airport")


class Employee(Base):
  __tablename__ = "employee"

  tabelnum = Column(Integer, primary_key=True)
  name = Column(String(255))
  last_name = Column(String(255))
  position_id = Column(Integer, ForeignKey("dim_position.id"))
  salary = Column(Integer)
  hire_date = Column(Date)
  position = relationship("DimPosition")


class Flight(Base):
  __tablename__ = "flight"

  flight_id = Column(Integer, primary_key=True)
  flight_number = Column(Integer)
  departure_id = Column(Integer, ForeignKey("airport.airport_id"))
  arrival_id = Column(Integer, ForeignKey("airport.airport_id"))
  departure_time = Column(DateTime)
  arrival_time = Column(DateTime)
  aircraft_id = Column(Integer, ForeignKey("aircraft.aircraft_id"))
  num_bsns_sts = Column(Integer)
  num_stndrt_sts = Column(Integer)
  aircraft = relationship("Aircraft")
  departure = relationship("Airport", foreign_keys=[departure_id])
  arrival = relationship("Airport", foreign_keys=[arrival_id])


class Tickets(Base):
  __tablename__ = "tickets"

  tickets_id = Column(Integer, primary_key=True)
  flight_id = Column(Integer, ForeignKey("flight.flight_id"))
  ticket_price = Column(Integer)
  ticket_status = Column(String(100))
  owner_id = Column(Integer, ForeignKey("passenger.passenger_id"))
  class_type = Column(String(10))
  date = Column(DateTime)
  passenger = relationship("Passenger")
  flight = relationship("Flight")


class PurchaseTicket(Base):
  __tablename__ = "purchase_ticket"

  purchase_id = Column(Integer, primary_key=True)
  ticket_id = Column(Integer, ForeignKey("tickets.tickets_id"))
  owner_id = Column(Integer, ForeignKey("passenger.passenger_id"))
  ticket = relationship("Tickets")
  owner = relationship("Passenger")


class WorkSchedule(Base):
  __tablename__ = "work_schedule"

  schedule_id = Column(Integer, primary_key=True)
  employee_tabelnum = Column(Integer, ForeignKey("employee.tabelnum"))
  flight_id = Column(Integer, ForeignKey("flight.flight_id"))
  start_time = Column(DateTime)
  end_time = Column(DateTime)
  employee = relationship("Employee")
  flight = relationship("Flight")
