class Usuario:
    def __init__(
        self,
        id: int,
        nombre: str,
        email: str
    ):
        self.id: int = id
        self.nombre: str = nombre
        self.email: str = email