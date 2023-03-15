from src.seedwork.aplicacion.comandos import Comando
from src.modulos.inventario.aplicacion.dto import OrdenDTO
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.inventario.dominio.entidades import Orden
from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrden
from src.modulos.gestorCompra.infraestructura.dto import Compra
import uuid
import datetime
from pydispatch import dispatcher

@dataclass
class ValidarInventario(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    productos_orden: str


class ValidarInventarioHandler():

    def handle(self, comando: ValidarInventario, app=None):
        print('Validar inventario handler')
        id_compra = uuid.uuid1()
        with app.app_context():
            from src.config.db import db
            productos_cantidades=comando.productos_orden
            #productos_cantidades=','.join([(w.sku + ":" + str(w.cantidad)) for w in comando.productos_orden[0].productos])
            compra = Compra(id = id_compra, fecha_creacion = datetime.datetime.now(), fecha_actualizacion=datetime.datetime.now(), productos_cantidades=productos_cantidades)
            db.session.add(compra)
            db.session.commit()

        orden_dto = OrdenDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=id_compra
            ,   productos=comando.productos_orden)
        print('antes de mapeador orden')
        mapeador = MapeadorOrden()
        orden: Orden = mapeador.dto_a_entidad(orden_dto)
        orden.validar_inventario(orden, comando)


@comando.register(ValidarInventario)
def ejecutar_comando_validar_inventario(comando: ValidarInventario, app=None):
    handler = ValidarInventarioHandler()
    handler.handle(comando=comando,app=app)
