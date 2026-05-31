from datetime import datetime

def comprar_entradas(
    usuario_registrado,
    fecha,
    entradas,
    edades,
    metodo_pago,
    parque_abierto
):
    validar_usuario(usuario_registrado)
    validar_fecha(fecha)
    validar_disponibilidad(parque_abierto)
    validar_metodo_pago(metodo_pago)
    validar_cantidad_entradas(entradas)
    validar_edades(entradas, edades)

    return generar_respuesta_exitosa(
        fecha=fecha,
        cantidad=entradas,
        metodo_pago=metodo_pago
    )


def validar_usuario(usuario_registrado):
    if not usuario_registrado:
        raise PermissionError(
            "Debe estar registrado"
        )


def validar_fecha(fecha):
    fecha_ingresada = datetime.strptime(
        fecha,
        "%d/%m/%Y"
    )

    if fecha_ingresada.date() < datetime.now().date():
        raise ValueError(
            "La fecha debe ser actual o futura"
        )


def validar_disponibilidad(parque_abierto):
    if not parque_abierto:
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