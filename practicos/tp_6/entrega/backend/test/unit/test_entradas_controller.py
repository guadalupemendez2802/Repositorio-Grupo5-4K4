from datetime import datetime

import pytest
from fastapi import HTTPException, status

from src.controller.entradas_controller import registrar_compra, detalle_entrada
from src.DTO.request.registrar_compra_request import RegistrarCompraRequest
from src.DTO.response.detalle_entradas_response import DetalleEntradasResponse


class DummyEntrada:
    def __init__(self, entrada_id: int, tipo_pase_id: int, edad_visitante: int):
        self.id = entrada_id
        self.tipo_pase_id = tipo_pase_id
        self.edad_visitante = edad_visitante


def test_registrar_compra_ok_sin_redireccion(monkeypatch):
    def fake_comprar_entrada(*args, **kwargs):
        return {
            "estado": "ok",
            "fecha_visita": "03/06/2026",
            "cantidad": 2,
            "total": 2500.0,
            "id_compra": 55,
        }

    monkeypatch.setattr(
        "src.controller.entradas_controller.comprar_entrada",
        fake_comprar_entrada,
    )

    req = RegistrarCompraRequest(
        email_usuario="user@test.com",
        fecha_visita="03/06/2026",
        cantidad_entradas=2,
        edades=[20, 30],
        metodo_pago="efectivo",
        ids_tipo_pase=[1, 1],
    )

    response = registrar_compra(req)

    assert response.model_dump() == {
        "estado": "ok",
        "fecha_visita": datetime.strptime("03/06/2026", "%d/%m/%Y").date(),
        "cantidad": 2,
        "redirigir": None,
        "total": 2500.0,
        "id_compra": 55,
    }


def test_registrar_compra_ok_con_redireccion(monkeypatch):
    def fake_comprar_entrada(*args, **kwargs):
        return {
            "estado": "ok",
            "fecha_visita": "03/06/2026",
            "cantidad": 2,
            "redirigir_a": "mercado_pago",
            "total": 3500.0,
            "id_compra": 99,
        }

    monkeypatch.setattr(
        "src.controller.entradas_controller.comprar_entrada",
        fake_comprar_entrada,
    )

    req = RegistrarCompraRequest(
        email_usuario="user@test.com",
        fecha_visita="03/06/2026",
        cantidad_entradas=2,
        edades=[20, 30],
        metodo_pago="tarjeta",
        ids_tipo_pase=[1, 1],
    )

    response = registrar_compra(req)

    assert response.redirigir == "mercado_pago"
    assert response.total == 3500.0
    assert response.id_compra == 99


def test_registrar_compra_error_value_error(monkeypatch):
    def fake_comprar_entrada(*args, **kwargs):
        raise ValueError("Tipo de pase invalido: 99")

    monkeypatch.setattr(
        "src.controller.entradas_controller.comprar_entrada",
        fake_comprar_entrada,
    )

    req = RegistrarCompraRequest(
        email_usuario="user@test.com",
        fecha_visita="03/06/2026",
        cantidad_entradas=1,
        edades=[20],
        metodo_pago="tarjeta",
        ids_tipo_pase=[99],
    )

    with pytest.raises(HTTPException) as exc:
        registrar_compra(req)

    assert exc.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc.value.detail == "Tipo de pase invalido: 99"


def test_detalle_entrada_ok(monkeypatch):
    entradas = [
        {
            "entrada": DummyEntrada(10, 1, 20),
            "tipo_pase": "REGULAR",
        },
        {
            "entrada": DummyEntrada(11, 1, 30),
            "tipo_pase": "REGULAR",
        },
    ]

    monkeypatch.setattr(
        "src.controller.entradas_controller.obtener_detalle_entradas",
        lambda _id_compra: entradas,
    )

    response = detalle_entrada(55)

    assert [item.model_dump() for item in response] == [
        DetalleEntradasResponse(id=10, tipo_pase_id=1, tipo_pase="REGULAR", edad_visitante=20).model_dump(),
        DetalleEntradasResponse(id=11, tipo_pase_id=1, tipo_pase="REGULAR", edad_visitante=30).model_dump(),
    ]


def test_detalle_entrada_error_value_error(monkeypatch):
    def fake_obtener_detalle_entradas(_id_compra: int):
        raise ValueError("Compra invalida")

    monkeypatch.setattr(
        "src.controller.entradas_controller.obtener_detalle_entradas",
        fake_obtener_detalle_entradas,
    )

    with pytest.raises(HTTPException) as exc:
        detalle_entrada(999)

    assert exc.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc.value.detail == "Compra invalida"
