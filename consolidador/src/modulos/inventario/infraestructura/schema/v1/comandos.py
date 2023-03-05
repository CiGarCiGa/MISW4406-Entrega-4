from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoValidarInventarioPayload(ComandoIntegracion):
    sku_producto = String()
    cantidad_producto = int()
    id_orden = String()

class ComandoValidarInventario(ComandoIntegracion):
    data = ComandoValidarInventarioPayload()