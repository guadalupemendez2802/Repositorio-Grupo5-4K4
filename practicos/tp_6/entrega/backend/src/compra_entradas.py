from datetime import datetime

def comprar_entradas(
    usuario_registrado: bool,
    fecha_visita: str,
    cantidad_entradas: int,
    edades: list[int],
    ids_tipo_pase: list[int],
    metodo_pago: str,
):
    validar_usuario(usuario_registrado)
    validar_fecha(fecha_visita)
    validar_disponibilidad(fecha_visita)
    validar_metodo_pago(metodo_pago)
    validar_cantidad_entradas(cantidad_entradas)
    validar_edades(cantidad_entradas, edades)
    validar_tipos_pase(cantidad_entradas, ids_tipo_pase)

    return generar_respuesta_exitosa(
        fecha=fecha_visita,
        cantidad=cantidad_entradas,
        metodo_pago=metodo_pago
    )


def validar_usuario(usuario_registrado):
    if not usuario_registrado:
        raise PermissionError(
            "Debe estar registrado"
        )


def validar_fecha(fecha):
    if not fecha:
        raise ValueError(
            "Debe ingresar una fecha de visita"
        )
    fecha_ingresada = datetime.strptime(
        fecha,
        "%d/%m/%Y"
    )

    if fecha_ingresada.date() < datetime.now().date():
        raise ValueError(
            "La fecha debe ser actual o futura"
        )

    # Limitar a un año desde la fecha actual.
    fecha_maxima = datetime.now().date().replace(
        year=datetime.now().date().year + 1
    )
    if fecha_ingresada.date() > fecha_maxima:
        raise ValueError(
            "Solo puede solicitar entradas hasta 1 año en el futuro desde la fecha actual"
        )


def validar_disponibilidad(fecha_visita: str):
    if not fecha_visita:
        raise ValueError(
            "Debe ingresar una fecha de visita"
        )

    if isinstance(fecha_visita, str):
        fecha_visita = datetime.strptime(fecha_visita,"%d/%m/%Y")

    # lunes (0) y feriados 25 diciembre y 1ro enero no tienen disponibilidad
    if fecha_visita.weekday() == 0 or (
        fecha_visita.month == 12 and fecha_visita.day == 25
    ) or (
        fecha_visita.month == 1 and fecha_visita.day == 1
    ):
        raise ValueError(
            "No hay disponibilidad para la fecha seleccionada"
        )



def validar_metodo_pago(metodo_pago):
    if metodo_pago is None:
        raise ValueError(
            "Debe seleccionar el método de pago"
        )


def validar_cantidad_entradas(entradas):
    if entradas > 10:
        raise ValueError(
            "La cantidad de entradas debe ser menor o igual a 10"
        )


def validar_edades(entradas, edades):
    if len(edades) != entradas:
        raise ValueError(
            "Debe indicar la edad de cada visitante"
        )
    for edad in edades:
        if edad < 0:
            raise ValueError(
                "La edad no puede ser negativa"
            )


def validar_tipos_pase(entradas, ids_tipo_pase):
    if len(ids_tipo_pase) != entradas:
        raise ValueError(
            "Debe indicar el tipo de pase de cada visitante"
        )


def generar_respuesta_exitosa(
    fecha,
    cantidad,
    metodo_pago
):
    respuesta = {
        "estado": "ok",
        "fecha_visita": fecha,
        "cantidad": cantidad
    }

    if metodo_pago == "tarjeta":
        respuesta["redirigir_a"] = "mercado_pago"

    return respuesta