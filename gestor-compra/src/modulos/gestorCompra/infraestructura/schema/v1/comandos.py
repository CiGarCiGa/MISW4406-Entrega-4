from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoReservarProductoPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoReservarProducto(ComandoIntegracion):
    data = ComandoReservarProductoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)