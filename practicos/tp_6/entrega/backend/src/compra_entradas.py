from datetime import datetime


def comprar_entradas(
    usuario_registrado,
    fecha,
    entradas,
    edades,
    metodo_pago,
    parque_abierto
):

    if not usuario_registrado:
        raise PermissionError("Debe estar registrado")

    fecha_ingresada = datetime.strptime(fecha, "%d/%m/%Y")

    if fecha_ingresada.date() < datetime.now().date():
        raise ValueError("La fecha debe ser actual o futura")

    if not parque_abierto:
        raise ValueError("No hay disponibilidad para la fecha seleccionada")

    if metodo_pago is None:
        raise ValueError("Debe seleccionar el método de pago")

    if entradas > 10:
        raise ValueError(
            "La cantidad de entradas debe ser menor o igual a 10"
        )

    if len(edades) != entradas:
        raise ValueError(
            "Debe indicar la edad de cada visitante"
        )

    return {
        "estado": "ok",
        "redirigir_a": "mercado_pago"
    }