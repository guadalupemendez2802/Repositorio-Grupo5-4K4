class Compra:
    def __init__(self,
        id: int | None,
        usuario_id: int,
        fecha_compra: str,
        fecha_visita: str,
        forma_pago: str,
        total: float,
    ):
        self.id: int | None = id
        self.usuario_id: int = usuario_id
        self.fecha_compra: str = fecha_compra
        self.fecha_visita: str = fecha_visita
        self.forma_pago: str = forma_pago
        self.total: float = total

