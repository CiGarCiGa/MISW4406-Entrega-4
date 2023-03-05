from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db

@dataclass
class Producto:
    id_producto: str
    cantidad: int

@dataclass
class ReservarProducto(Comando):
    productos: list[Producto]
    id_compra: str


class ReservarProductoHandler():
    def handle(self, comando: ReservarProducto):
        print('Aqui estuvo carlos')


@comando.register(ReservarProducto)
def ejecutar_comando_crear_reserva(comando: ReservarProducto):
    handler = ReservarProductoHandler()
    handler.handle(comando)