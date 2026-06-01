from datetime import datetime

from src.services import comprar_entrada_service


class DummyUser:
    def __init__(self, user_id: int):
        self.id = user_id


class DummyTipoPase:
    def __init__(self, precio: float):
        self.precio = precio


def test_comprar_entrada_ok_guarda_compra(monkeypatch):
    guardadas = []

    def fake_comprobar_usuario(email):
        return True, DummyUser(7)

    def fake_obtener_por_id(self, tipo_pase_id):
        return DummyTipoPase(100.0)

    def fake_comprar_entradas(**kwargs):
        return {
            "estado": "ok",
            "fecha_visita": kwargs["fecha_visita"],
            "cantidad": kwargs["cantidad_entradas"],
        }

    def fake_guardar(self, compra):
        guardadas.append(compra)
        compra.id = 123
        return compra.id

    monkeypatch.setattr(
        "src.services.comprar_entrada_service.comprobar_usuario",
        fake_comprobar_usuario,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.TipoPaseRepository.obtener_por_id",
        fake_obtener_por_id,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.comprar_entradas",
        fake_comprar_entradas,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.CompraRepository.guardar",
        fake_guardar,
    )

    resultado = comprar_entrada_service.comprar_entrada(
        email_usuario="user@test.com",
        fecha_visita="03/06/2026",
        cantidad_entradas=2,
        edades=[20, 30],
        metodo_pago="tarjeta",
        ids_tipo_pase=[1, 1],
    )

    assert resultado["estado"] == "ok"
    assert len(guardadas) == 1
    compra = guardadas[0]
    assert compra.usuario_id == 7
    assert compra.fecha_visita == "03/06/2026"
    assert compra.forma_pago == "tarjeta"
    assert compra.total == 200.0
    assert datetime.strptime(compra.fecha_compra, "%Y-%m-%d")


def test_comprar_entrada_error_no_guarda(monkeypatch):
    guardadas = []

    def fake_comprobar_usuario(email):
        return True, DummyUser(7)

    def fake_obtener_por_id(self, tipo_pase_id):
        return DummyTipoPase(100.0)

    def fake_comprar_entradas(**kwargs):
        return {
            "estado": "error",
            "fecha_visita": kwargs["fecha_visita"],
            "cantidad": kwargs["cantidad_entradas"],
        }

    def fake_guardar(self, compra):
        guardadas.append(compra)
        return 123

    monkeypatch.setattr(
        "src.services.comprar_entrada_service.comprobar_usuario",
        fake_comprobar_usuario,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.TipoPaseRepository.obtener_por_id",
        fake_obtener_por_id,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.comprar_entradas",
        fake_comprar_entradas,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.CompraRepository.guardar",
        fake_guardar,
    )

    resultado = comprar_entrada_service.comprar_entrada(
        email_usuario="user@test.com",
        fecha_visita="03/06/2026",
        cantidad_entradas=2,
        edades=[20, 30],
        metodo_pago="tarjeta",
        ids_tipo_pase=[1, 1],
    )

    assert resultado["estado"] == "error"
    assert guardadas == []


def test_calculo_total_con_descuentos_por_edad(monkeypatch):
    def fake_comprobar_usuario(email):
        return True, DummyUser(9)

    def fake_obtener_por_id(self, tipo_pase_id):
        assert tipo_pase_id == 1
        return DummyTipoPase(10000.0)

    def fake_comprar_entradas(**kwargs):
        return {
            "estado": "ok",
            "fecha_visita": kwargs["fecha_visita"],
            "cantidad": kwargs["cantidad_entradas"],
        }

    monkeypatch.setattr(
        "src.services.comprar_entrada_service.comprobar_usuario",
        fake_comprobar_usuario,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.TipoPaseRepository.obtener_por_id",
        fake_obtener_por_id,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.comprar_entradas",
        fake_comprar_entradas,
    )

    resultado = comprar_entrada_service.comprar_entrada(
        email_usuario="user@test.com",
        fecha_visita="03/06/2026",
        cantidad_entradas=3,
        edades=[3, 12, 25],
        metodo_pago="tarjeta",
        ids_tipo_pase=[1, 1, 1],
    )

    assert resultado["total"] == 15000.0
