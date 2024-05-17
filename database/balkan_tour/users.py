import sqlite3

# Sukuriame prisijungimo objektą
connection = sqlite3.connect("balkan_bike_tours.db")
cursor = connection.cursor()

# Sukuriame sąrašą su naujais vartotojais
new_users = [
    ("john_doe", "john@example.com", "password1"),
    ("jane_smith", "jane@example.com", "password2"),
    ("alice_wonderland", "alice@example.com", "password3"),
    ("bob_marley", "bob@example.com", "password4"),
    ("emma_jones", "emma@example.com", "password5"),
    ("michael_scott", "michael@example.com", "password6"),
    ("pam_beesly", "pam@example.com", "password7"),
    ("dwight_schrute", "dwight@example.com", "password8"),
    ("jim_halpert", "jim@example.com", "password9"),
    ("andy_bernard", "andy@example.com", "password10")
]

# Įterpiame naujus vartotojus į duomenų bazę
cursor.executemany("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", new_users)

# Patvirtiname pakeitimus
connection.commit()