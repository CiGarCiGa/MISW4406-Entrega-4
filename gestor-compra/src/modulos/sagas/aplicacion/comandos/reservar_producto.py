from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.sagas.infraestructura.despachadores import Despachador

@dataclass
class ReservarProducto(Comando):
    ...

class ReservarProductoHandler():
    def handle(self, comando: ReservarProducto):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-reserva-producto')


@comando.register(ReservarProducto)
def ejecutar_comando_reservar_producto(comando: ReservarProducto):
    handler = ReservarProductoHandler()
    handler.handle(comando)