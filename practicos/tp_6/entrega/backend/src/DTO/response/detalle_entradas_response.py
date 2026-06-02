from pydantic import BaseModel

class DetalleEntradasResponse(BaseModel):
    id: int
    tipo_pase_id: int
    tipo_pase: str
    edad_visitante: int