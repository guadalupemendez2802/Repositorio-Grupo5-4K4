from datetime import datetime

from compra_entradas import comprar_entradas
from models.compra import Compra
from repositories.compra_repository import CompraRepository
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
            case _ if 16 < edades[i] < 60:
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
        CompraRepository().guardar(compra_actual)

    # TODO MÁS O MENOS POR ACÁ SE DEBERÍA ENVIAR UN MAIL DE CONFIRMACIÓN AL USUARIO, TENÉMOS QUE HACER ESO?
    # O QUEDA FUERA DEL ALCANCE QUE ESTAMOS PROGRAMANDO?

    resultado["total"] = total

    return resultado
