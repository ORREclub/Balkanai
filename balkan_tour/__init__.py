from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/balkan_bike_tours.db'

db = SQLAlchemy(app)

from . import routes

# Čia aš pradžioje importuoju Flask ir SQLAlchemy,
# tada sukuriu Flask app  ir nustatau duomenų bazės URI.
# Toliau sukuriu SQLAlchemy objektą ir perduodu jam Flask app, kad būtų sukurtas ryšys tarp jų.
# po to is balkan_tours importuoju routes modulį, kad būtų galima įtraukti maršrutus į programą.