from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.producto.infraestructura.dto import Producto, ProductoReservado
import uuid
import datetime
import time
import src.seedwork.infraestructura.utils as utils
from src.modulos.producto.dominio.eventos import ProductosReservados
from src.modulos.producto.infraestructura.despachadores import Despachador
@dataclass
class ReservarProducto(Comando):
    productos_cantidades: str
    id_compra: str


class ReservarProductoHandler():
    def handle(self, comando: ReservarProducto, app=None):
        time.sleep(int(utils.get_delay()))
        with app.app_context():
            from src.config.db import db
            # Creando registro en base de datos para la reserva
            validar_existencias = True
            id_reservas=""
            for item in comando.productos_cantidades.split(','):
                id_producto=item.split(':')[0]
                cantidad = int(item.split(':')[0])
                producto = Producto.query.get(id_producto)
                if producto.cantidad < cantidad :
                    validar_existencias = False
                    break;
                producto.cantidad = producto.cantidad - cantidad
                id_reserva=uuid.uuid1()
                nueva_reserva = ProductoReservado(id=id_reserva ,id_producto=id_producto,id_compra=comando.id_compra,cantidad=cantidad,fecha_creacion=datetime.datetime.now())
                id_reservas=id_reservas+"-"+str(id_reserva)
                db.session.add(nueva_reserva)
            if validar_existencias :
                db.session.commit()
                evento = ProductosReservados(id_reserva=id_reservas,id_compra=comando.id_compra, evento= 'ProductosReservados')
                despachador = Despachador()
                despachador.publicar_evento(evento=evento, topico='eventos-productos')
                print('Evento "ProductoReservado" enviado para id_compra :'+ comando.id_compra, flush=True)
            else:
                db.session.rollback()
                evento = ProductosReservados(id_reserva=id_reservas,id_compra=comando.id_compra, evento= 'ProductosNoReservados')
                despachador = Despachador()
                despachador.publicar_evento(evento=evento, topico='eventos-productos')
                print('Evento "ProductosNoReservados" enviado para id_compra :'+ comando.id_compra, flush=True)

@comando.register(ReservarProducto)
def ejecutar_comando_crear_reserva(comando: ReservarProducto, app=None):
    handler = ReservarProductoHandler()
    handler.handle(comando,app)
