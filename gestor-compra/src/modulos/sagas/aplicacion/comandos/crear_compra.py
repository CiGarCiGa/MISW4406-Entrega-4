from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.sagas.infraestructura.despachadores import Despachador

@dataclass
class CrearCompra(Comando):
    ...

class CrearCompraHandler():
    def handle(self, comando: CrearCompra):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-compra')


@comando.register(CrearCompra)
def ejecutar_comando_crear_compra(comando: CrearCompra):
    handler = CrearCompraHandler()
    handler.handle(comando)