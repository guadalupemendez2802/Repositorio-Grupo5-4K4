from datetime import datetime

import pytest

from src.services import comprar_entrada_service


class DummyUser:
    def __init__(self, user_id: int):
        self.id = user_id
        self.nombre = "test-user"


class DummyTipoPase:
    def __init__(self, precio: float):
        self.precio = precio


def test_comprar_entrada_ok_guarda_compra(monkeypatch):
    guardadas = []
    entradas_guardadas = []

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

    def fake_obtener_cantidad_entradas(self, fecha_visita):
        return 0

    def fake_guardar_entrada(self, entrada):
        entradas_guardadas.append(entrada)
        return 999

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
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.EntradaRepository.obtener_cantidad_entradas",
        fake_obtener_cantidad_entradas,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.EntradaRepository.guardar",
        fake_guardar_entrada,
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
    assert resultado["id_compra"] == 123
    assert len(guardadas) == 1
    compra = guardadas[0]
    assert compra.usuario_id == 7
    assert compra.fecha_visita == "03/06/2026"
    assert compra.forma_pago == "tarjeta"
    assert compra.total == 200.0
    assert datetime.strptime(compra.fecha_compra, "%Y-%m-%d")

    assert len(entradas_guardadas) == 2
    assert entradas_guardadas[0].compra_id == 123
    assert entradas_guardadas[0].tipo_pase_id == 1
    assert entradas_guardadas[0].nombre_visitante == "test-user"
    assert entradas_guardadas[0].edad_visitante == 20


def test_comprar_entrada_error_no_guarda(monkeypatch):
    guardadas = []
    entradas_guardadas = []

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

    def fake_obtener_cantidad_entradas(self, fecha_visita):
        return 0

    def fake_guardar_entrada(self, entrada):
        entradas_guardadas.append(entrada)
        return 999

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
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.EntradaRepository.obtener_cantidad_entradas",
        fake_obtener_cantidad_entradas,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.EntradaRepository.guardar",
        fake_guardar_entrada,
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
    assert "id_compra" not in resultado
    assert guardadas == []
    assert entradas_guardadas == []


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

    def fake_guardar(self, compra):
        compra.id = 321
        return compra.id

    def fake_obtener_cantidad_entradas(self, fecha_visita):
        return 0

    def fake_guardar_entrada(self, entrada):
        return 777

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
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.EntradaRepository.obtener_cantidad_entradas",
        fake_obtener_cantidad_entradas,
    )
    monkeypatch.setattr(
        "src.services.comprar_entrada_service.EntradaRepository.guardar",
        fake_guardar_entrada,
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


def test_error_si_no_hay_cupo(monkeypatch):
    def fake_obtener_cantidad_entradas(self, fecha_visita):
        return 99

    monkeypatch.setattr(
        "src.services.comprar_entrada_service.EntradaRepository.obtener_cantidad_entradas",
        fake_obtener_cantidad_entradas,
    )

    with pytest.raises(
        ValueError,
        match=(
            "No hay suficientes entradas disponibles para la fecha seleccionada\. "
            "Solo quedan 1 entradas disponibles para el día 03/06/2026\."
        ),
    ):
        comprar_entrada_service.comprar_entrada(
            email_usuario="user@test.com",
            fecha_visita="03/06/2026",
            cantidad_entradas=2,
            edades=[20, 30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )


def test_error_si_tipo_pase_invalido(monkeypatch):
    def fake_comprobar_usuario(email):
        return True, DummyUser(7)

    def fake_obtener_por_id(self, tipo_pase_id):
        return None

    def fake_comprar_entradas(**kwargs):
        return {
            "estado": "ok",
            "fecha_visita": kwargs["fecha_visita"],
            "cantidad": kwargs["cantidad_entradas"],
        }

    def fake_obtener_cantidad_entradas(self, fecha_visita):
        return 0

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
        "src.services.comprar_entrada_service.EntradaRepository.obtener_cantidad_entradas",
        fake_obtener_cantidad_entradas,
    )

    with pytest.raises(ValueError, match="Tipo de pase invalido: 99"):
        comprar_entrada_service.comprar_entrada(
            email_usuario="user@test.com",
            fecha_visita="03/06/2026",
            cantidad_entradas=1,
            edades=[20],
            metodo_pago="tarjeta",
            ids_tipo_pase=[99],
        )

