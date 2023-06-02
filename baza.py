import sqlite3
from pony.orm import Database, PrimaryKey, Required

db = Database()

class Zaposlenici(db.Entity):
    id = PrimaryKey(int, auto=True)
    ime = Required(str)
    prezime = Required(str)
    pozicija = Required(str)
    placa = Required(float)

db.bind(provider='sqlite', filename='pisprojekt.db', create_db=False)


try:
    db.generate_mapping(create_tables=False)
    print("Uspjesno povezano s bazom podataka!")
except Exception as e:
    print(f"Pogreska prilikom povezivanja s bazom podataka: {str(e)}")