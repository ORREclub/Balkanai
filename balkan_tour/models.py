from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()  #declarative base funkcija sukuria bazinę klasę, iš kurios bus paveldimos visosmano modelių klasės.

class Tour(Base):
    __tablename__ = 'tours' #nurodo, kad šis modelis yra susietas su "tours" lentelės struktūra duomenų bazėje.

    id = Column(Integer, primary_key=True) #nurodo, kad stulpelis yra pirminis raktas
    name = Column(String)
    description = Column(String)
    location = Column(String)
    bookings = relationship('Booking', back_populates='tour')#cia visur apsirašau atgalinį ryšį
    clients = relationship('Client', back_populates='tour')

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

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    tour_id = Column(Integer, ForeignKey('tours.id'))
    tour_name = Column(String)

    tour = relationship('Tour', back_populates='clients')
