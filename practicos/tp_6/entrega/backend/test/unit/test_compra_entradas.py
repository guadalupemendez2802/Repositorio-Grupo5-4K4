import pytest
from src.compra_entradas import comprar_entradas

@pytest.fixture
def datos_validos():
    return {
        "usuario_registrado": True,
        "fecha": "03/06/2026",
        "entradas": 10,
        "edades": [17,22,55,33,75,67,69,21,16,17],
        "metodo_pago": "tarjeta",
        "parque_abierto": True
    }

#TEST 1
def test_compra_exitosa_con_tarjeta():
    resultado = comprar_entradas(
        usuario_registrado=True,
        fecha_visita="03/06/2026",
        cantidad_entradas=10,
        edades=[17,22,55,33,75,67,69,21,16,17],
        metodo_pago="tarjeta",
        ids_tipo_pase=[1] * 10,
    )

    assert resultado["estado"] == "ok"
    assert resultado["redirigir_a"] == "mercado_pago"

#TEST 2
def test_error_si_no_indica_medio_de_pago():
    with pytest.raises(ValueError,
                       match="Debe seleccionar el método de pago"):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="03/06/2026",
            cantidad_entradas=10,
            edades=[17,22,55,33,75,67,69,21,16,17],
            metodo_pago=None,
            ids_tipo_pase=[1] * 10,
        )

#TEST 3
def test_error_si_compra_mas_de_diez_entradas():
    with pytest.raises(
        ValueError,
        match="La cantidad de entradas debe ser menor o igual a 10"
    ):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="03/06/2026",
            cantidad_entradas=11,
            edades=[20] * 11,
            metodo_pago="tarjeta",
            ids_tipo_pase=[1] * 11,
        )

#TEST 4
def test_error_si_usuario_no_registrado():
    with pytest.raises(
        PermissionError,
        match="Debe estar registrado"
    ):
        comprar_entradas(
            usuario_registrado=False,
            fecha_visita="03/06/2026",
            cantidad_entradas=2,
            edades=[20, 30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )

#TEST 5
def test_error_si_parque_cerrado():
    with pytest.raises(
        ValueError,
        match="No hay disponibilidad para la fecha seleccionada"
    ):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="08/06/2026",
            cantidad_entradas=2,
            edades=[20,30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )

#TEST 6
def test_error_si_fecha_pasada():
    with pytest.raises(
        ValueError,
        match="La fecha debe ser actual o futura"
    ):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="01/01/2020",
            cantidad_entradas=2,
            edades=[20,30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )

#TEST 7
def test_error_si_faltan_edades():
    with pytest.raises(
        ValueError,
        match="Debe indicar la edad de cada visitante"
    ):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="03/06/2026",
            cantidad_entradas=3,
            edades=[20,30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )

def test_error_si_faltan_tipos_pase():
    with pytest.raises(
        ValueError,
        match="Debe indicar el tipo de pase de cada visitante",
    ):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="03/06/2026",
            cantidad_entradas=3,
            edades=[20, 30, 40],
            ids_tipo_pase=[1, 2],
            metodo_pago="tarjeta",
        )

#TEST 8
def test_error_si_no_hay_fecha():
    with pytest.raises(
        ValueError,
        match="Debe ingresar una fecha de visita"
    ):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="",
            cantidad_entradas=2,
            edades=[20,30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )

def test_error_si_25_diciembre():
    with pytest.raises(ValueError, match="No hay disponibilidad para la fecha seleccionada"):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="25/12/2026",
            cantidad_entradas=2,
            edades=[20,30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )

def test_error_si_1_enero():
    with pytest.raises(ValueError, match="No hay disponibilidad para la fecha seleccionada"):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="01/01/2027",
            cantidad_entradas=2,
            edades=[20,30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )

def test_error_si_lunes():
    with pytest.raises(ValueError, match="No hay disponibilidad para la fecha seleccionada"):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="07/12/2026",
            cantidad_entradas=2,
            edades=[20,30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )

def test_error_si_fecha_posterior_1_year():
    with pytest.raises(ValueError, match="Solo puede solicitar entradas hasta 1 año en el futuro desde la fecha actual"):
        comprar_entradas(
            usuario_registrado=True,
            fecha_visita="30/12/2027",
            cantidad_entradas=2,
            edades=[20,30],
            metodo_pago="tarjeta",
            ids_tipo_pase=[1, 1],
        )