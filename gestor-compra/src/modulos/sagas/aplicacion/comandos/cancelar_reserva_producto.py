from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.sagas.infraestructura.despachadores import Despachador

@dataclass
class CancelarReservaProducto(Comando):
    ...

class CancelarReservaProductoHandler():
    def handle(self, comando: CancelarReservaProducto):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-reserva-producto')


@comando.register(CancelarReservaProducto)
def ejecutar_comando_cancelar_reserva_producto(comando: CancelarReservaProducto):
    handler = CancelarReservaProductoHandler()
    handler.handle(comando)