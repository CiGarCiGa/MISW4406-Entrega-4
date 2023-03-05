from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoReservarProductoPayload(ComandoIntegracion):
    id_producto = String()
    cantidad = Integer()
    id_compra= String()

class ComandoReservarProducto(ComandoIntegracion):
    data = ComandoReservarProductoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)