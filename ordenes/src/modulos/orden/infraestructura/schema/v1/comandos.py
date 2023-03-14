from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class CrearOrdenPayload(ComandoIntegracion):
    id_compra = String()

class ComandoCrearOrden(ComandoIntegracion):
    data = CrearOrdenPayload()