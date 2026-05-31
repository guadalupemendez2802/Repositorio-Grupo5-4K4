from src.database.db import obtener_conexion
from src.models.tipo_pase import TipoPase

class TipoPaseRepository:
    @staticmethod
    def obtener_por_id(tipo_pase_id):
        con = obtener_conexion()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT *
            FROM TipoPase
            WHERE id = ?
            """,
            (tipo_pase_id,)
        )
    
        fila = cursor.fetchone()
        con.close()
        if fila is None:
            return None
        return TipoPase(
            id=fila["id"],
            nombre=fila["nombre"],
            descripcion=fila["descripcion"],
            precio=fila["precio"]
        )
    
    @staticmethod
    def obtener_todos():
        con = obtener_conexion()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT ¨
            FROM TipoPase
            """
        )

        filas = cursor.fetchall()
        con.close()
        return [TipoPase(
            id=fila["id"],
            nombre=fila["nombre"],
            descripcion=fila["descripcion"],
            precio=fila["precio"]
        )
        for fila in filas]
    