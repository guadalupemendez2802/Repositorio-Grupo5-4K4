class TipoPase:
    def __init__(self, 
        id: int,
        nombre: str, 
        descripcion: str, 
        precio: float
    ):    
        self.id: int = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio