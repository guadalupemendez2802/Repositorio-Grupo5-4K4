from datetime import datetime

from fastapi import APIRouter
from services.comprar_entrada_service import comprar_entrada

from DTO.request.registrar_compra_request import RegistrarCompraRequest
from DTO.response.registrar_compra_response import RegistrarCompraResponse

router = APIRouter(prefix="/api/v1/entradas", tags=["Entradas"])


@router.post("/", response_model=RegistrarCompraResponse)
def registrar_compra(req: RegistrarCompraRequest):
    compra = comprar_entrada(
        req.email_usuario,
        req.fecha_visita,
        req.cantidad_entradas,
        req.edades,
        req.metodo_pago,
        req.ids_tipo_pase,
    )

    fecha = datetime.strptime(compra["fecha_visita"], "%d/%m/%Y").date()

    return RegistrarCompraResponse(estado=compra["estado"],
                                   fecha_visita=fecha,
                                   cantidad=compra["cantidad"],
                                   redirigir=compra["redirigir_a"] if "redirigir_a" in compra else None,
                                   total = compra["total"]
                                   )