from __future__ import annotations
from dataclasses import dataclass, field

from src.seedwork.dominio.entidades import AgregacionRaiz
from pydispatch import dispatcher

@dataclass
class Orden(AgregacionRaiz):
    id_compra: uuid.UUID = field(hash=True, default=None)

    def crear_orden(self, orden: Orden, comando):
        self.id_compra = orden.id_compra
        dispatcher.send(signal=f'{comando.__class__.__name__}Integracion', evento=comando)