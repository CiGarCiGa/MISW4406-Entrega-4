from src.seedwork.aplicacion.comandos import Comando
from src.modulos.inventario.aplicacion.dto import OrdenDTO
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.inventario.dominio.entidades import Orden
from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrden

@dataclass
class CrearOrden(Comando):
    id_compra: str


class CrearOrdenHandler():
    
    def handle(self, comando: CrearOrden):
        print('Crear orden handler')
        orden_dto = OrdenDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   productos=comando.productos_orden)
        print('antes de mapeador orden')
        mapeador = MapeadorOrden()
        orden: Orden = mapeador.dto_a_entidad(orden_dto)
        orden.crear_orden(orden)


@comando.register(CrearOrden)
def ejecutar_comando_crear_orden(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
    