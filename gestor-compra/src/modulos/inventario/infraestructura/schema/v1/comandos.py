from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
import src.modulos.inventario.dominio.objetos_valor as ov

class ComandoValidarInventarioPayload(ComandoIntegracion):
    productos_orden = String()
    id_orden = String()

class ComandoValidarInventario(ComandoIntegracion):
    data = ComandoValidarInventarioPayload()