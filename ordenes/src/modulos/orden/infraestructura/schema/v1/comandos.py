from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
import src.modulos.inventario.dominio.objetos_valor as ov

class CrearOrdenPayload(ComandoIntegracion):
    id_compra = String()

class ComandoCrearOrden(ComandoIntegracion):
    data = CrearOrdenPayload()