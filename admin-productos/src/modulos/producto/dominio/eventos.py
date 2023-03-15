from __future__ import annotations
from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoProducto(EventoDominio):
    ...

@dataclass
class ProductoCreado(EventoProducto):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None


@dataclass
class ProductoCancelado(EventoProducto):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ProductoAprobado(EventoProducto):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ProductoPagado(EventoProducto):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ProductosReservados(EventoProducto):
    id_reserva: str = None
    id_compra: uuid.UUID = None
    evento = str = None