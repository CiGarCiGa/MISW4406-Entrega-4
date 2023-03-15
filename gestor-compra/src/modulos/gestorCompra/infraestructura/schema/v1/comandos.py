from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoReservarProductoPayload(ComandoIntegracion):
    productos_cantidades = String()
    id_compra= String()

class ComandoReservarProducto(ComandoIntegracion):
    data = ComandoReservarProductoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoCrearCompraPayload(ComandoIntegracion):
    productos_cantidades = String()
    id_usuario= String()
    domicilio= String()

class ComandoCrearCompra(ComandoIntegracion):
    data = ComandoCrearCompraPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)