from __future__ import annotations
from dataclasses import dataclass, field

import src.modulos.gestorCompra.dominio.objetos_valor as ov
from src.modulos.gestorCompra.dominio.eventos import ReservarProducto
from src.seedwork.dominio.entidades import AgregacionRaiz
from pydispatch import dispatcher

@dataclass
class ReservaProducto(AgregacionRaiz):
    id_compra: uuid.UUID = field(hash=True, default=None)
    productos: list[ov.ProductoReserva] = field(default_factory=list[ov.ProductoReserva])

    def reservar_producto(self, producto: ReservarProducto):
        self.id_compra = producto.id_compra
        self.productos = producto.productos
        #print('antes de agregar evento inventario validado', flush=True)
        evento=ReservarProducto(id_compra=self.id_compra, productos=self.productos)
        self.agregar_evento(evento)
        dispatcher.send(signal=f'{ReservarProducto.__name__}Integracion', evento=evento)