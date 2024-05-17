from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Tour(Base):
    __tablename__ = 'tours'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    location = Column(String)
    bookings = relationship('Booking', back_populates='tour')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    bookings = relationship('Booking', back_populates='user')

class Bike(Base):
    __tablename__ = 'bikes'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    type = Column(String)
    bookings = relationship('Booking', back_populates='bike')

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    bike_id = Column(Integer, ForeignKey('bikes.id'))
    tour_id = Column(Integer, ForeignKey('tours.id'))
    date = Column(DateTime)

    user = relationship('User', back_populates='bookings')
    bike = relationship('Bike', back_populates='bookings')
    tour = relationship('Tour', back_populates='bookings')