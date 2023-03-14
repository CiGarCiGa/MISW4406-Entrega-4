from __future__ import annotations
from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoValidacionInventario(EventoDominio):
    ...

@dataclass
class InventarioValidado(EventoValidacionInventario):
    ...

class ValidacionInventarioFallida(EventoValidacionInventario):
    ...
