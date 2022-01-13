from Table import Direction

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Duomenu bazes uzklausos

engine = create_engine('sqlite:///flights.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_direction(direction, range, price):
    flight_route = Direction(direction, range, price)
    session.add(flight_route)
    session.commit()


def update_direction(record_id, newdirection, newrange, newprice):
    flight_route = session.query(Direction).get(record_id)
    flight_route.direction = newdirection
    flight_route.range = newrange
    flight_route.price = newprice
    session.commit()

def delete_direction(record_id):
    flight_route = session.query(Direction).get(record_id)
    session.delete(flight_route)
    session.commit()

def get_all_directions():
    return session.query(Direction).all()

