from aeroalpes.seedwork.aplicacion.comandos import Comando
from src.modulos.inventario.aplicacion.dto import OrdenDTO
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.vuelos.dominio.entidades import Reserva
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva
from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas

@dataclass
class ValidarInventario(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    productos_orden: list[OrdenDTO]


class ValidarInventarioHandler():
    
    def handle(self, comando: ValidarInventario):
        print('Comando Validar Inventario')


@comando.register(ValidarInventario)
def ejecutar_comando_validar_inventario(comando: ValidarInventario):
    handler = ValidarInventarioHandler()
    handler.handle(comando)
    