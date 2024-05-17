from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from tables import User, Bike, Tour, Booking

# Sukuriamas konektorius į duomenų bazę
engine = create_engine('sqlite:///balkan_bike_tours.db', echo=True)

# Sukuriamas sesijos kūrėja
Session = sessionmaker(bind=engine)
session = Session()

# Sukuriame naują rezervaciją
new_booking = Booking(user_id=1, bike_id=1, tour_id=1, date=datetime.now())


# Pridedame naują rezervaciją į sesiją
session.add(new_booking)

# Patvirtiname pakeitimus
session.commit()

# Uždarome sesiją
session.close()