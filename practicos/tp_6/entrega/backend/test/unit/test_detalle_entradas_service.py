from src.services.detalle_entradas_service import obtener_detalle_entradas


class DummyEntrada:
    def __init__(self, entrada_id: int, tipo_pase_id: int):
        self.id = entrada_id
        self.tipo_pase_id = tipo_pase_id


class DummyTipoPase:
    def __init__(self, nombre: str):
        self.nombre = nombre


def test_obtener_detalle_entradas_ok(monkeypatch):
    def fake_obtener_entradas(self, id_compra: int):
        assert id_compra == 55
        return [DummyEntrada(10, 1), DummyEntrada(11, 2)]

    def fake_obtener_tipo_pase(self, tipo_pase_id: int):
        return DummyTipoPase("REGULAR" if tipo_pase_id == 1 else "VIP")

    monkeypatch.setattr(
        "src.services.detalle_entradas_service.EntradaRepository.obtener_entradas_por_id_compra",
        fake_obtener_entradas,
    )
    monkeypatch.setattr(
        "src.services.detalle_entradas_service.TipoPaseRepository.obtener_por_id",
        fake_obtener_tipo_pase,
    )

    resultado = obtener_detalle_entradas(55)

    assert resultado == [
        {"entrada": resultado[0]["entrada"], "tipo_pase": "REGULAR"},
        {"entrada": resultado[1]["entrada"], "tipo_pase": "VIP"},
    ]
    assert resultado[0]["entrada"].id == 10
    assert resultado[1]["entrada"].id == 11


def test_obtener_detalle_entradas_sin_resultados(monkeypatch):
    monkeypatch.setattr(
        "src.services.detalle_entradas_service.EntradaRepository.obtener_entradas_por_id_compra",
        lambda _self, _id_compra: [],
    )

    resultado = obtener_detalle_entradas(999)

    assert resultado == []

