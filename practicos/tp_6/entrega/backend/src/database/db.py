import sqlite3 as sqlite

#db = "entradas_database.db"
db = str(__import__('pathlib').Path(__file__).resolve().parent / "entradas_database.db")

def obtener_conexion():
    conexion = sqlite.connect(db)

    conexion.row_factory = sqlite.Row

    return conexion
