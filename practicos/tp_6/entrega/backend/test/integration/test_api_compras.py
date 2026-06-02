from fastapi.testclient import TestClient

from src.start.main import app


client = TestClient(app)


def test_get_compra_ok(seed_base_data):
    payload = {
        "email_usuario": "user@test.com",
        "fecha_visita": "03/06/2026",
        "cantidad_entradas": 1,
        "edades": [20],
        "metodo_pago": "tarjeta",
        "ids_tipo_pase": [1],
    }

    post_response = client.post("/api/v1/entradas/", json=payload)

    assert post_response.status_code == 200
    compra_id = post_response.json()["id_compra"]

    get_response = client.get(f"/api/v1/compras/{compra_id}")

    assert get_response.status_code == 200
    data = get_response.json()
    assert data == {
        "id": compra_id,
        "fecha_visita": "03/06/2026",
        "forma_pago": "tarjeta",
        "total": 10000.0,
    }


def test_get_compra_no_encontrada(seed_base_data):
    response = client.get("/api/v1/compras/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Compra no encontrada"

