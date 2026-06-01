from src.database.db import obtener_conexion
from src.models.usuario import Usuario

class UsuarioRepository:
    def __init__(self):
        pass
    @staticmethod
    def obtener_por_id(usuario_id):
        con = obtener_conexion()
        
        cursor = con.cursor()

        cursor.execute("""
                        SELECT *
                        FROM Usuario
                        WHERE id = ?
                        """,
                        usuario_id,
                        )
        
        fila = cursor.fetchone()

        con.close()

        if fila is None:
            return None

        return Usuario(
            id=fila["id"],
            nombre=fila["nombre"],
            email=fila["email"]
        )

    @staticmethod
    def obtener_por_email(email):
        con = obtener_conexion()

        cursor = con.cursor()

        cursor.execute("""
                       SELECT *
                       FROM Usuario
                       WHERE email = ?
                       """,
                       (email,)
                       )

        fila = cursor.fetchone()

        con.close()

        if fila is None:
            return None

        return Usuario(
            id=fila["id"],
            nombre=fila["nombre"],
            email=fila["email"]
        )

    @staticmethod
    def guardar(usuario):
        con = obtener_conexion()
        cursor = con.cursor()
        cursor.execute(
            """
            INSERT INTO Usuario
            (
                nombre,
                email
            )
            VALUES (?, ?)
            """,
            (
                usuario.nombre,
                usuario.email,
            )
        )

        con.commit()

        usuario_id = cursor.lastrowid

        con.close()

        return usuario_id