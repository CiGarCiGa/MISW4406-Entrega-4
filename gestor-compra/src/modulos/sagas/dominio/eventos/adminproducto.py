from __future__ import annotations
from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoReservaProducto(EventoDominio):
    ...

@dataclass
class ProductoReservado(EventoReservaProducto):
    ...

@dataclass
class ReservaProductoFallida(EventoReservaProducto):
    ...
