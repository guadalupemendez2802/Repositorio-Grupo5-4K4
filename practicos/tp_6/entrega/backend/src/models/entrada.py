class Entrada:
    
    def __init__(
        self,
        id: int,
        compra_id: int,
        tipo_pase_id: int,
        nombre_visitante: str,   
        edad_visitante: int,
    ):
        self.id = id
        self.compra_id = compra_id
        self.tipo_pase_id = tipo_pase_id
        self.nombre_visitante = nombre_visitante
        self.edad_visitante = edad_visitante
    