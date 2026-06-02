from fastapi import APIRouter, HTTPException, status
from repositories.compra_repository import CompraRepository
from DTO.response.ver_compra_response import VerCompraResponse


router_compras = APIRouter(prefix="/api/v1/compras", tags=["Compras"])

@router_compras.get("/{id_compra}", response_model=VerCompraResponse)
def ver_compra(id_compra: int):
    compra = CompraRepository.obtener_por_id(id_compra)
    if compra is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Compra no encontrada")
    return VerCompraResponse(id=compra.id, fecha_visita=compra.fecha_visita, forma_pago=compra.forma_pago, total=compra.total)