from pydantic import BaseModel, Field


class RegistrarCompraRequest(BaseModel):
    email_usuario: str = Field(..., description="Email del usuario que realiza la compra")
    fecha_visita: str = Field(..., description="Fecha para la cual se compra el boleto")
    cantidad_entradas: int = Field(..., description="Cantidad de entradas a comprar")
    edades: list[int] = Field(..., description="Lista con las edades de los visitantes "
                                               "correspondientes a cada entrada comprada")
    ids_tipo_pase: list[int] = Field(
        ...,
        description="Lista con el id del tipo de pase (vip o regular) de cada entrada",
    )
    metodo_pago: str = Field(..., description="string aclarando el método de pago utilizado")