from src.seedwork.aplicacion.comandos import Comando
from src.modulos.inventario.aplicacion.dto import OrdenDTO
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.inventario.dominio.entidades import Orden
from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrden

@dataclass
class ValidarInventario(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    productos_orden: list[OrdenDTO]


class ValidarInventarioHandler():
    
    def handle(self, comando: ValidarInventario):
        print('Validar inventario handler')
        orden_dto = OrdenDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   productos=comando.productos_orden)
        print('antes de mapeador orden')
        mapeador = MapeadorOrden()
        orden: Orden = mapeador.dto_a_entidad(orden_dto)
        orden.validar_inventario(orden)


@comando.register(ValidarInventario)
def ejecutar_comando_validar_inventario(comando: ValidarInventario):
    handler = ValidarInventarioHandler()
    handler.handle(comando)
    