from datetime import datetime

from fastapi import APIRouter, HTTPException, status
from services.comprar_entrada_service import comprar_entrada
from repositories.compra_repository import CompraRepository

from DTO.request.registrar_compra_request import RegistrarCompraRequest
from DTO.response.registrar_compra_response import RegistrarCompraResponse
from DTO.response.ver_compra_response import VerCompraResponse

router = APIRouter(prefix="/api/v1/entradas", tags=["Entradas"])
router_compras = APIRouter(prefix="/api/v1/compras", tags=["Compras"])


@router.post("/", response_model=RegistrarCompraResponse)
def registrar_compra(req: RegistrarCompraRequest):
    try:
        compra = comprar_entrada(
            req.email_usuario,
            req.fecha_visita,
            req.cantidad_entradas,
            req.edades,
            req.metodo_pago,
            req.ids_tipo_pase,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    fecha = datetime.strptime(compra["fecha_visita"], "%d/%m/%Y").date()

    return RegistrarCompraResponse(
        estado=compra["estado"],
        fecha_visita=fecha,
        cantidad=compra["cantidad"],
        redirigir=compra["redirigir_a"] if "redirigir_a" in compra else None,
        total=compra["total"],
        id_compra=compra["id_compra"],
    )


@router_compras.get("/{id_compra}", response_model=VerCompraResponse)
def ver_compra(id_compra: int):
    compra = CompraRepository.obtener_por_id(id_compra)
    if compra is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Compra no encontrada")
    return compra
