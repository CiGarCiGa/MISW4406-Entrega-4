from __future__ import annotations
from dataclasses import dataclass, field
import random
from src.seedwork.dominio.entidades import AgregacionRaiz
from src.modulos.orden.dominio.eventos import OrdenCreada
from pydispatch import dispatcher

@dataclass
class Orden(AgregacionRaiz):
    id_compra: uuid.UUID = field(hash=True, default=None)

    def crear_orden(self, orden: Orden, comando):
        self.id_compra = orden.id_compra
        generar_id_orden = random.randint(1,50)
        evento=OrdenCreada(id_orden=generar_id_orden, id_compra=self.id_compra)
        self.agregar_evento(evento)
        dispatcher.send(signal=f'{OrdenCreada.__class__.__name__}Integracion', evento=comando)