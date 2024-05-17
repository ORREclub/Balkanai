import sqlite3

# Sukuriame prisijungimo objektą
connection = sqlite3.connect("balkan_bike_tours.db")
cursor = connection.cursor()

# Sukuriame naują įrašą
new_tours = [
    ("Bulgaria Tour", "Discover the beauty of Bulgaria", "Bulgaria"),
    ("Albania Tour", "Discover the beauty of Albania", "Albania"),
    ("Macedonia Tour", "Discover the beauty of Macedonia", "Macedonia")
    ]
cursor.executemany("INSERT INTO tours (name, description, location) VALUES (?, ?, ?)", new_tours)

# Patvirtiname pakeitimus
connection.commit()

# Uždarome prisijungimą
connection.close()