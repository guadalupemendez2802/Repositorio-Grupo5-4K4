from datetime import date, datetime

from src.database.db import obtener_conexion


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.entrada import Entrada

class EntradaRepository:
    @staticmethod
    def guardar(entrada: Entrada):
        con = obtener_conexion()
        cursor = con.cursor()
        cursor.execute(
        """
        INSERT INTO Entrada
        (
            compra_id,
            tipo_pase_id,
            nombre_visitante,
            edad_visitante
        )
        VALUES (?, ?, ?, ?)
        """, (entrada.compra_id, 
              entrada.tipo_pase_id,
              entrada.nombre_visitante,
              entrada.edad_visitante)
        )
        con.commit()
        entrada_id = cursor.lastrowid
        con.close()
        return entrada_id

    @staticmethod
    def obtener_cantidad_entradas(fecha_visita: str | date) -> int:
        con = obtener_conexion()
        cursor = con.cursor()

        if isinstance(fecha_visita, date):
            fecha_visita = fecha_visita.strftime("%d/%m/%Y")
        else:
            # Si viene "12/12/26", lo pasa a "12/12/2026"
            try:
                fecha_visita = datetime.strptime(fecha_visita, "%d/%m/%y").strftime("%d/%m/%Y")
            except ValueError:
                # Si ya viene "12/12/2026", lo deja normalizado igual
                fecha_visita = datetime.strptime(fecha_visita, "%d/%m/%Y").strftime("%d/%m/%Y")

        cursor.execute(
            """
            SELECT COUNT(e.id)
            FROM Entrada e
            INNER JOIN Compra c ON e.compra_id = c.id
            WHERE c.fecha_visita = ?
            """,
            (fecha_visita,)
        )

        cantidad = cursor.fetchone()[0]

        con.close()
        return cantidad