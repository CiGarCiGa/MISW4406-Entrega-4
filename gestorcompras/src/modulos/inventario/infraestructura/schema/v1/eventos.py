from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class InventarioValidadoPayload(Record):
    id_orden = String()
    id_cliente = String()

class EventoInventarioValidado(EventoIntegracion):
    data = InventarioValidadoPayload()