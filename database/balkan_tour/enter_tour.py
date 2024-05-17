from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Tour

# Sukuriamas konektorius į duomenų bazę
engine = create_engine('sqlite:///balkan_bike_tours.db')
Session = sessionmaker(bind=engine)
session = Session()

# Vartotojo įvestis
name = input("Enter tour name: ")
location = input("Enter tour location: ")
description = input("Enter tour description: ")

# Sukuriamas naujas turas
new_tour = Tour(name=name, location=location, description=description)

# Pridedame turą į sesiją
session.add(new_tour)

# Patvirtiname pakeitimus
session.commit()

print("Tour added successfully!")