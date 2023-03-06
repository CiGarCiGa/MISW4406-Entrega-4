from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.producto.infraestructura.dto import Producto, ProductoReservado
import uuid
import datetime

@dataclass
class ReservarProducto(Comando):
    productos_cantidades: str
    id_compra: str


class ReservarProductoHandler():
    def handle(self, comando: ReservarProducto, app=None):
        with app.app_context():
            from src.config.db import db
            # Creando registro en base de datos para la reserva
            validar_existencias = True
            for item in comando.productos_cantidades.split(','):
                id_producto=item.split(':')[0]
                cantidad = int(item.split(':')[0])
                producto = Producto.query.get(id_producto)
                if producto.cantidad < cantidad :
                    validar_existencias = False
                    break;
                nueva_reserva = ProductoReservado(id=uuid.uuid1() ,id_producto=id_producto,id_compra=comando.id_compra,cantidad=cantidad,fecha_creacion=datetime.datetime.now())
                db.session.add(nueva_reserva)
            if validar_existencias :
                db.session.commit()
            else:
                db.session.rollback()

@comando.register(ReservarProducto)
def ejecutar_comando_crear_reserva(comando: ReservarProducto, app=None):
    handler = ReservarProductoHandler()
    handler.handle(comando,app)