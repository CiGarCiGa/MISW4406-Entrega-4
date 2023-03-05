"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass
from src.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Producto(ObjetoValor):
    sku: str
    cantidad: int

@dataclass(frozen=True)
class ProductoOrden(ObjetoValor):
    productos: list[Producto]