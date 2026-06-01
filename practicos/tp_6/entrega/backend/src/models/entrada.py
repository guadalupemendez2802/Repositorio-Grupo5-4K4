class Entrada:
    
    def __init__(
        self,
        id: int,
        compra_id: int,
        tipo_pase_id: int,
        nombre_visitante: str,   
        edad_visitante: int,
    ):
        self.id:int = id
        self.compra_id: int = compra_id
        self.tipo_pase_id: int = tipo_pase_id
        self.nombre_visitante: str = nombre_visitante
        self.edad_visitante: int = edad_visitante
    