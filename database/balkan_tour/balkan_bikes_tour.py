from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base, Tour, User, Bike, Booking

# Sukuriamas konektorius į duomenų bazę
engine = create_engine('sqlite:///balkan_bike_tours.db', echo=True)

# Sukuriamas patvirtinimas ir lentelės pagrindui
Base.metadata.create_all(engine)

# Sukuriamas sesijos kūrėjas
Session = sessionmaker(bind=engine)
session = Session()
new_tour = Tour(name='Balkan Tour', description='Discover the beauty of the Balkans', location='Balkans')

# Sukurkite sesiją
engine = create_engine('sqlite:///balkan_bike_tours.db')
Session = sessionmaker(bind=engine)
session = Session()

# Pridėkite naują įrašą į sesiją
session.add(new_tour)

# Įvykdykite komandą commit, kad įrašas būtų įrašytas į duomenų bazę
session.commit()

# Uždarykite sesiją
session.close()