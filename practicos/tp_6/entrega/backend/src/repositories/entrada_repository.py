from src.database.db import obtener_conexion

class EntradaRepository:
    @staticmethod
    def guardar(entrada):
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