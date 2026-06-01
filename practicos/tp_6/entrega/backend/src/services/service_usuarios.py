from __future__ import annotations

from repositories.usuario_repository import UsuarioRepository

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.usuario import Usuario


def comprobar_usuario(email_usuario: str) -> tuple[bool, Usuario] :
    repo_users = UsuarioRepository()

    user = repo_users.obtener_por_email(email_usuario)

    return user is not None, user # si el usuario es none retorna false, sino retorna true
    # es la forma más pava que se me ocurrió de comprobar si el usuario existe
    # devuelvo también los datos del usuario porque voy a necesitar su id eventualmente cuando llamo a este método