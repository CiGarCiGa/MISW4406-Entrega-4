from __future__ import annotations
from dataclasses import dataclass, field

import src.modulos.inventario.dominio.objetos_valor as ov
from src.seedwork.dominio.entidades import AgregacionRaiz
from pydispatch import dispatcher

@dataclass
class Orden(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    productos: str = field(default_factory=str)

    def validar_inventario(self, orden: Orden, comando):
        self.id = orden.id
        self.productos = orden.productos
        print('antes de agregar evento inventario validado', flush=True)
        dispatcher.send(signal=f'{comando.__class__.__name__}Integracion', evento=comando)