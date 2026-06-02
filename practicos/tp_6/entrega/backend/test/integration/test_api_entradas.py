import sqlite3

from fastapi.testclient import TestClient

from src.start.main import app


client = TestClient(app)


def test_post_entradas_compra_ok(seed_base_data):
    payload = {
        "email_usuario": "user@test.com",
        "fecha_visita": "03/06/2026",
        "cantidad_entradas": 1,
        "edades": [20],
        "metodo_pago": "tarjeta",
        "ids_tipo_pase": [1],
    }

    response = client.post("/api/v1/entradas/", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["estado"] == "ok"
    assert data["redirigir"] == "mercado_pago"
    assert data["total"] == 10000.0
    assert isinstance(data["id_compra"], int)


def test_post_entradas_error_tipo_pase_invalido(seed_base_data):
    payload = {
        "email_usuario": "user@test.com",
        "fecha_visita": "03/06/2026",
        "cantidad_entradas": 1,
        "edades": [20],
        "metodo_pago": "tarjeta",
        "ids_tipo_pase": [99],
    }

    response = client.post("/api/v1/entradas/", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Tipo de pase invalido: 99"


def test_post_entradas_error_sin_cupo(db_path, seed_base_data):
    con = sqlite3.connect(db_path)
    con.execute(
        "INSERT INTO Compra (usuario_id, fecha_compra, fecha_visita, forma_pago, total) VALUES (?, ?, ?, ?, ?)",
        (1, "2026-06-01", "03/06/2026", "tarjeta", 0.0),
    )
    compra_id = con.execute("SELECT last_insert_rowid()").fetchone()[0]
    con.executemany(
        "INSERT INTO Entrada (compra_id, tipo_pase_id, nombre_visitante, edad_visitante) VALUES (?, ?, ?, ?)",
        [(compra_id, 1, "Usuario Test", 20) for _ in range(100)],
    )
    con.commit()
    con.close()

    payload = {
        "email_usuario": "user@test.com",
        "fecha_visita": "03/06/2026",
        "cantidad_entradas": 1,
        "edades": [20],
        "metodo_pago": "tarjeta",
        "ids_tipo_pase": [1],
    }

    response = client.post("/api/v1/entradas/", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "No hay suficientes entradas disponibles para la fecha seleccionada. "
        "Solo quedan 0 entradas disponibles para el día 03/06/2026."
    )

