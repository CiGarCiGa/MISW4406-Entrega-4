from src.modulos.gestorCompra.infraestructura.dto import Compra
from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.gestorCompra.infraestructura.despachadores import Despachador

@dataclass
class ReservarProducto(Comando):
    id_compra: str
    productos_cantidades: str

class ReservarProductoHandler():
    def handle(self, comando: ReservarProducto, app=None):
        with app.app_context():
            from src.config.db import db
            compra = Compra.query.get(comando.id_compra)
            comando.productos_cantidades=compra.productos_cantidades
            compra.estado='PRODUCTOS_VALIDOS'
            db.session.commit()
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-producto')

@comando.register(ReservarProducto)
def ejecutar_comando_reservar_producto(comando: ReservarProducto, app=None):
    handler = ReservarProductoHandler()
    handler.handle(comando, app=app)