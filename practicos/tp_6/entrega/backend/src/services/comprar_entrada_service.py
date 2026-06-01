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
    total = 0
    for tipo_pase_id in ids_tipo_pase:
        tipo_pase = repo_tipos.obtener_por_id(tipo_pase_id)
        if tipo_pase is None:
            raise ValueError(f"Tipo de pase invalido: {tipo_pase_id}")
        total += tipo_pase.precio

    resultado = comprar_entradas(
        usuario_registrado=usuario_registrado,
        fecha_visita=fecha_visita,
        cantidad_entradas=cantidad_entradas,
        edades=edades,
        ids_tipo_pase=ids_tipo_pase,
        metodo_pago=metodo_pago,
    )

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

    return resultado
