from __future__ import annotations
from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoCreacionOrden(EventoDominio):
    ...

@dataclass
class OrdenCreada(EventoCreacionOrden):
    ...

@dataclass
class CreacionOrdenFallida(EventoCreacionOrden):
    ...
