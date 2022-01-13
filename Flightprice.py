from time import sleep
from Table import Flight

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Duomenu bazes uzklausos

engine = create_engine('sqlite:///flights.db')
Session = sessionmaker(bind=engine)
session2 = Session()

def add_Flight(flight, passengers, profit, distance):
    new_flight = Flight(flight, passengers, profit, distance)
    session2.add(new_flight)
    session2.commit()


def update_Flight(record_id, newflight, newpassengers, newprofit, newdistance):
    flight_route = session2.query(Flight).get(record_id)
    flight_route.flight = newflight
    flight_route.passengers = newpassengers
    flight_route.profit = newprofit
    flight_route.distance = newdistance
    session2.commit()

def delete_Flight(record_id):
    flight_route = session2.query(Flight).get(record_id)
    session2.delete(flight_route)
    session2.commit()

def get_all_Flight():
    return session2.query(Flight).all()

def get_all_profit():
    balansas = session2.query(Flight).filter(Flight.profit).all()
    pajamos = 0
    for pinigai in balansas:
        pajamos += pinigai.profit
    return pajamos
    
