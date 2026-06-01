from datetime import datetime

from compra_entradas import comprar_entradas
from models.compra import Compra
from repositories.compra_repository import CompraRepository
from repositories.tipo_pase_repository import TipoPaseRepository
from services.service_usuarios import comprobar_usuario

def comprar_entrada(email_usuario: str,
                    fecha_visita: str,
                    cantidad_entradas: int,
                    edades: list[int],
                    metodo_pago: str,
                    id_tipo_pase: int
                    ):

    usuario_registrado, user_data = comprobar_usuario(email_usuario)

    tipo_pase = TipoPaseRepository().obtener_por_id(id_tipo_pase)

    resultado = comprar_entradas(
        usuario_registrado=usuario_registrado,
        fecha_visita=fecha_visita,
        cantidad_entradas=cantidad_entradas,
        edades=edades,
        metodo_pago=metodo_pago
    )

    total = tipo_pase.precio * cantidad_entradas


    if resultado["estado"] == "ok":
        compra_actual = Compra(None, user_data.id, str(datetime.now().date()), fecha_visita, metodo_pago, total)
        CompraRepository().guardar(compra_actual)

    #TODO MÁS O MENOS POR ACÁ SE DEBERÍA ENVIAR UN MAIL DE CONFIRMACIÓN AL USUARIO, TENÉMOS QUE HACER ESO?
    # O QUEDA FUERA DEL ALCANCE QUE ESTAMOS PROGRAMANDO?

    return resultado