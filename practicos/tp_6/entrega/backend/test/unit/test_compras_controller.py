import pytest
from fastapi import HTTPException, status

from src.controller.compras_controller import ver_compra


class DummyCompra:
    def __init__(self, compra_id: int):
        self.id = compra_id
        self.fecha_visita = "03/06/2026"
        self.forma_pago = "tarjeta"
        self.total = 4500.0


def test_ver_compra_ok(monkeypatch):
    def fake_obtener_por_id(compra_id):
        return DummyCompra(compra_id)

    monkeypatch.setattr(
        "src.controller.compras_controller.CompraRepository.obtener_por_id",
        fake_obtener_por_id,
    )

    response = ver_compra(10)

    assert response.model_dump() == {
        "id": 10,
        "fecha_visita": "03/06/2026",
        "forma_pago": "tarjeta",
        "total": 4500.0,
    }


def test_ver_compra_no_encontrada(monkeypatch):
    def fake_obtener_por_id(compra_id):
        return None

    monkeypatch.setattr(
        "src.controller.compras_controller.CompraRepository.obtener_por_id",
        fake_obtener_por_id,
    )

    with pytest.raises(HTTPException) as exc:
        ver_compra(99)

    assert exc.value.status_code == status.HTTP_404_NOT_FOUND
    assert exc.value.detail == "Compra no encontrada"

