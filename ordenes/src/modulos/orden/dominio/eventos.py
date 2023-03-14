from __future__ import annotations
from dataclasses import dataclass
from src.seedwork.dominio.eventos import (EventoDominio)

@dataclass
class OrdenCreada(EventoDominio):
    id_orden: uuid.UUID = None
    id_compra: uuid.UUID = None