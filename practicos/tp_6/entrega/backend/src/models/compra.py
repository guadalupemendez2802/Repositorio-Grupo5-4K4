class Compra:
    def __init__(self,
        id: int,
        usuario_id: int,
        fecha_compra: str,
        fecha_visita: str,
        forma_pago: str,
        total: float,
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.fecha_compra = fecha_compra
        self.fecha_visita = fecha_visita
        self.forma_pago = forma_pago
        self.total = total

