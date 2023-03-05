from __future__ import annotations
from dataclasses import dataclass, field

import src.modulos.inventario.dominio.objetos_valor as ov
from src.modulos.inventario.dominio.eventos import InventarioValidado
from src.seedwork.dominio.entidades import AgregacionRaiz
from pydispatch import dispatcher

@dataclass
class Orden(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    productos: list[ov.ProductoOrden] = field(default_factory=list[ov.ProductoOrden])

    def validar_inventario(self, orden: Orden):
        self.id_cliente = orden.id_cliente
        self.productos = orden.productos
        print('antes de agregar evento inventario validado', flush=True)
        evento=InventarioValidado(id_orden=self.id, id_cliente=self.id_cliente)
        self.agregar_evento(evento)
        dispatcher.send(signal=f'{InventarioValidado.__name__}Integracion', evento=evento)