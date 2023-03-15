from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class OrdenCreadaPayload(Record):
    id_orden = String()
    id_compra = String()

class EventoOrdenCreada(EventoIntegracion):
    data = OrdenCreadaPayload()