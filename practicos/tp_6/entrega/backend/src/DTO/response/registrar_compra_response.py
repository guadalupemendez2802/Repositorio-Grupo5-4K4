from datetime import date

from pydantic import BaseModel

class RegistrarCompraResponse(BaseModel):
    estado: str
    fecha_visita: date
    cantidad: int
    redirigir: str | None