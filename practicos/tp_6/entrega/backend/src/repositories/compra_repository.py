from models.compra import Compra
from src.database.db import obtener_conexion

class CompraRepository:
    @staticmethod
    def obtener_por_id(id_compra: int):
        con = obtener_conexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Compra WHERE id = ?", (id_compra,))
        fila = cursor.fetchone()
        con.close()
        if fila is None:
            return None
        return Compra(**fila)

    @staticmethod
    def guardar(compra):
        con = obtener_conexion()
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO Compra
            (
                usuario_id,
                fecha_compra,
                fecha_visita,
                forma_pago,
                total
            )
            VALUES(?, ?, ?, ?, ?)
            """,
            (compra.usuario_id,
            compra.fecha_compra,
            compra.fecha_visita,
            compra.forma_pago,
            compra.total)
        )
        con.commit()
        compra_id = cursor.lastrowid
        compra.id = compra_id
        con.close()
        return compra_id