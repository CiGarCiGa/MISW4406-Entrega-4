from __future__ import annotations
from dataclasses import dataclass
from src.seedwork.dominio.eventos import (EventoDominio)

@dataclass
class InventarioValidado(EventoDominio):
    id_orden: uuid.UUID = None
    estado: str = ""