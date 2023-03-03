from __future__ import annotations
from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoProducto(EventoDominio):
    ...

@dataclass
class ProductoCreada(EventoProducto):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None

@dataclass
class ProductoCancelada(EventoProducto):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ProductoAprobada(EventoProducto):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ProductoPagada(EventoProducto):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None