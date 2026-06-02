from __future__ import annotations
from repositories.entrada_repository import EntradaRepository
from repositories.tipo_pase_repository import TipoPaseRepository

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.entrada import Entrada

def obtener_detalle_entradas(id_compra: int) -> list[dict[str, Entrada | str]]:
    repo_entrada = EntradaRepository()
    repo_tipo_pase = TipoPaseRepository()

    entradas = repo_entrada.obtener_entradas_por_id_compra(id_compra)

    entradas_list: list[dict[str, Entrada | str]] = []

    for entrada in entradas:
        tipo_pase = repo_tipo_pase.obtener_por_id(entrada.tipo_pase_id)
        entradas_list.append({
            "entrada": entrada,
            "tipo_pase": tipo_pase.nombre,
        })
    return entradas_list

