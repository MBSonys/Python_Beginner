from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

# Sukuriamas db failas

engine = create_engine("sqlite:///flights.db")
Base = declarative_base()

# Sukuriamos lenteles duomenu bazeje

class Flight(Base):
    __tablename__= "Skrydziai"
    id = Column(Integer, primary_key=True)
    flight = Column("Kriptis", String)
    passengers = Column("Keleiviai", Integer)
    profit = Column("Pelnas", Integer)
    distance = Column("Atstumas", Integer)


    def __init__(self, flight, passengers, profit, distance):
        self.flight = flight
        self.passengers = passengers
        self.profit = profit
        self.distance = distance

    def __repr__(self):
        return f"{self.flight}, {self.passengers}, {self.profit}, {self.distance}"


class Direction(Base):
    __tablename__= "Skrydzio_info"
    id = Column(Integer, primary_key=True)
    direction = Column("Kriptis", String)
    range = Column("Atstumas", Integer)
    price = Column("Bilieto kainas", Integer)

    def __init__(self, direction, range, price):
        self.direction = direction
        self.range = range
        self.price = price

    def __repr__(self):
        return f"{self.direction}, {self.range}, {self.price}"
        


Base.metadata.create_all(engine)
    