from datetime import datetime

def comprar_entradas(
    usuario_registrado: bool,
    fecha_visita: str,
    cantidad_entradas: int,
    edades: list[int],
    metodo_pago: str,
):
    validar_usuario(usuario_registrado)
    validar_fecha(fecha_visita)
    validar_disponibilidad(fecha_visita)
    validar_metodo_pago(metodo_pago)
    validar_cantidad_entradas(cantidad_entradas)
    validar_edades(cantidad_entradas, edades)

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


def validar_disponibilidad(fecha_visita: str):
    if not fecha_visita:
        raise ValueError(
            "Debe ingresar una fecha de visita"
        )

    if isinstance(fecha_visita, str):
        fecha_visita = datetime.strptime(
            fecha_visita,
            "%d/%m/%Y"
        )

    # si la fecha es sábado (5) o domingo (6) no hay disponibilidad
    # funciona tanto para datetime.datetime como datetime.date
    #TODO CORREGIR ESTO CUANDO SEPAMOS CUALES SON LAS FECHAS DONDE ESTÁ CERRADO
    if fecha_visita.weekday() in (5, 6):
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