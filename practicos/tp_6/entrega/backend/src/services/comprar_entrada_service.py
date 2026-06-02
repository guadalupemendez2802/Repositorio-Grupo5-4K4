from datetime import datetime

from compra_entradas import comprar_entradas
from models.compra import Compra
from models.entrada import Entrada
from repositories.compra_repository import CompraRepository
from repositories.entrada_repository import EntradaRepository
from repositories.tipo_pase_repository import TipoPaseRepository
from services.service_usuarios import comprobar_usuario


def comprar_entrada(
    email_usuario: str,
    fecha_visita: str,
    cantidad_entradas: int,
    edades: list[int],
    metodo_pago: str,
    ids_tipo_pase: list[int],
):

    entrada_repo: EntradaRepository = EntradaRepository()

    cantidad_entradas_registradas = entrada_repo.obtener_cantidad_entradas(fecha_visita)

    if cantidad_entradas_registradas + cantidad_entradas > 100:
        entradas_restantes = 100 - cantidad_entradas_registradas
        raise ValueError(f"No hay suficientes entradas disponibles para la fecha seleccionada."
                         f" Solo quedan {entradas_restantes} entradas disponibles para el día {fecha_visita}.")


    validar_mail(email_usuario)

    usuario_registrado, user_data = comprobar_usuario(email_usuario)

    repo_tipos = TipoPaseRepository()

    resultado = comprar_entradas(
        usuario_registrado=usuario_registrado,
        fecha_visita=fecha_visita,
        cantidad_entradas=cantidad_entradas,
        edades=edades,
        ids_tipo_pase=ids_tipo_pase,
        metodo_pago=metodo_pago,
    )

    total = 0
    for i in range(len(ids_tipo_pase)):
        tipo_pase = repo_tipos.obtener_por_id(ids_tipo_pase[i])
        if tipo_pase is None:
            raise ValueError(f"Tipo de pase invalido: {ids_tipo_pase[i]}")

        # El precio puede tener descuento dependiendo la edad del visitante.
        # Se asume que en la lista llegan paralelos las edades con los tipos pase
        # así la edad[2] corresponde al tipo_pase[2]
        precio: float = 0
        match edades[i]:
            case _ if edades[i] <= 3:
                precio = 0 # menores de 3 años no pagan
            case _ if 3 < edades[i] <= 15:
                precio = tipo_pase.precio * 0.5 # 50% off
            case _ if 15 < edades[i] < 60:
                precio = tipo_pase.precio # sin descuento
            case _ if edades[i] >= 60:
                precio = tipo_pase.precio * 0.5 # 50% off

        total += precio

    if resultado["estado"] == "ok":
        compra_actual = Compra(
            None,
            user_data.id,
            str(datetime.now().date()),
            fecha_visita,
            metodo_pago,
            total,
        )
        # obtengo y actualizo el id de la compra guardada en BD
        compra_actual.id = CompraRepository().guardar(compra_actual)
        resultado["id_compra"] = compra_actual.id

        # ahora debo actualizar en la bdd las entradas para esa fecha
        for i in range(cantidad_entradas):
            entrada_actual = Entrada(
                None,
                compra_actual.id,
                ids_tipo_pase[i],
                user_data.nombre,
                edades[i]
            )
            entrada_repo.guardar(entrada_actual)



    # TODO MÁS O MENOS POR ACÁ SE DEBERÍA ENVIAR UN MAIL DE CONFIRMACIÓN AL USUARIO, TENÉMOS QUE HACER ESO?
    # O QUEDA FUERA DEL ALCANCE QUE ESTAMOS PROGRAMANDO?

    resultado["total"] = total

    return resultado


def validar_mail(email):
    if email is None or email.strip() == "":
        raise ValueError(
            "Debe ingresar un correo electrónico"
        )
    if "@" not in email:
        raise ValueError(
            "El correo electrónico debe contener '@'"
        )
    if "." not in email.split("@")[1]:
        raise ValueError(
            "El correo electrónico debe contener un dominio válido después de '@'"
        )