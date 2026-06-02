from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from DTO.response.detalle_entradas_response import DetalleEntradasResponse
from services.detalle_entradas_service import obtener_detalle_entradas
from services.comprar_entrada_service import comprar_entrada

from DTO.request.registrar_compra_request import RegistrarCompraRequest
from DTO.response.registrar_compra_response import RegistrarCompraResponse

router = APIRouter(prefix="/api/v1/entradas", tags=["Entradas"])

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
    except PermissionError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
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

@router.get("/detalle/{id_compra}", response_model=list[DetalleEntradasResponse])
def detalle_entrada(id_compra: int):
    try:
        entradas_detalle = obtener_detalle_entradas(id_compra)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    list_entradas = []

    for elemento in entradas_detalle:
        list_entradas.append(DetalleEntradasResponse(id=elemento["entrada"].id,
                                                    tipo_pase_id=elemento["entrada"].tipo_pase_id,
                                                    tipo_pase=elemento["tipo_pase"],
                                                    edad_visitante=elemento["entrada"].edad_visitante,
                                                    ))

    return list_entradas



