from __future__ import annotations
from dataclasses import dataclass, field
from src.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoCompra(EventoDominio):
    ...

class EventoReserva(EventoDominio):
    ...

@dataclass
class CompraCreada(EventoCompra):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None

@dataclass
class CreacionCompraFallida(EventoCompra):
    ...

@dataclass
class CompraCancelada(EventoCompra):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class CompraAprobada(EventoCompra):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class CompraPagada(EventoCompra):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class Producto(EventoCompra):
    cantidad: int = 0
    id_producto: uuid.UUID = None

@dataclass
class ReservarProducto(EventoReserva):
    productos : list[Producto] = None
    id_compra : uuid.UUID = None