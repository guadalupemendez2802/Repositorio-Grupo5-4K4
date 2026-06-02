import sqlite3
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = PROJECT_ROOT / "src"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from src.database import db as db_module


@pytest.fixture()
def db_path(tmp_path, monkeypatch):
    db_file = tmp_path / "test.db"
    monkeypatch.setattr(db_module, "db", str(db_file))

    con = sqlite3.connect(db_file)
    con.executescript(
        """
        CREATE TABLE Usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL
        );
        CREATE TABLE TipoPase (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL
        );
        CREATE TABLE Compra (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            fecha_compra TEXT NOT NULL,
            fecha_visita TEXT NOT NULL,
            forma_pago TEXT NOT NULL,
            total REAL NOT NULL
        );
        CREATE TABLE Entrada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            compra_id INTEGER NOT NULL,
            tipo_pase_id INTEGER NOT NULL,
            nombre_visitante TEXT NOT NULL,
            edad_visitante INTEGER NOT NULL
        );
        """
    )
    con.commit()
    con.close()

    return db_file


@pytest.fixture()
def seed_base_data(db_path):
    con = sqlite3.connect(db_path)
    con.execute(
        "INSERT INTO Usuario (nombre, email) VALUES (?, ?)",
        ("Usuario Test", "user@test.com"),
    )
    con.execute(
        "INSERT INTO TipoPase (nombre, descripcion, precio) VALUES (?, ?, ?)",
        ("REGULAR", "Pase Regular", 10000.0),
    )
    con.commit()
    con.close()
