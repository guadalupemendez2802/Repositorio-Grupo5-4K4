from src.services import service_usuarios


class DummyUser:
    def __init__(self, user_id: int):
        self.id = user_id


def test_comprobar_usuario_encontrado(monkeypatch):
    def fake_obtener_por_email(self, email):
        return DummyUser(5)

    monkeypatch.setattr(
        "src.services.service_usuarios.UsuarioRepository.obtener_por_email",
        fake_obtener_por_email,
    )

    existe, user = service_usuarios.comprobar_usuario("user@test.com")

    assert existe is True
    assert user.id == 5


def test_comprobar_usuario_no_encontrado(monkeypatch):
    def fake_obtener_por_email(self, email):
        return None

    monkeypatch.setattr(
        "src.services.service_usuarios.UsuarioRepository.obtener_por_email",
        fake_obtener_por_email,
    )

    existe, user = service_usuarios.comprobar_usuario("user@test.com")

    assert existe is False
    assert user is None

