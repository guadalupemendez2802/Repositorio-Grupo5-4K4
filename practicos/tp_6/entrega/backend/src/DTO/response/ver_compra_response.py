from pydantic import BaseModel


class VerCompraResponse(BaseModel):
    id: int
    fecha_visita: str
    forma_pago: str
    total: float