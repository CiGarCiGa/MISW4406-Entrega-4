from src.seedwork.aplicacion.comandos import Comando
from src.modulos.inventario.aplicacion.dto import OrdenDTO
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.inventario.dominio.entidades import Orden
from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrden
from src.modulos.inventario.infraestructura.despachadores import Despachador
from src.modulos.inventario.dominio.eventos import InventarioValidado

@dataclass
class ValidarInventario(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    productos_orden: str


class ValidarInventarioHandler():

    def handle(self, comando: ValidarInventario, app=None):
        print('Inventario dummy validado!')
        evento=InventarioValidado(id_orden=comando.id, estado="InventarioValidado")
        despachador = Despachador()
        despachador.publicar_evento(evento=evento, topico='eventos-inventario')


@comando.register(ValidarInventario)
def ejecutar_comando_validar_inventario(comando: ValidarInventario, app=None):
    handler = ValidarInventarioHandler()
    handler.handle(comando, app=app)
