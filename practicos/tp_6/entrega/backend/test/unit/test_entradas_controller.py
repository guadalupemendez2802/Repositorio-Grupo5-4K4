from datetime import datetime

import pytest
from fastapi import HTTPException, status

from src.controller.entradas_controller import registrar_compra
from src.DTO.request.registrar_compra_request import RegistrarCompraRequest


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
