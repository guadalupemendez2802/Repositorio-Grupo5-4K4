import sqlite3 as sqlite

db = "entradas_database.db"

def obtener_conexion():
    conexion = sqlite.connect(db)

    conexion.row_factory = sqlite.Row

    return conexion
