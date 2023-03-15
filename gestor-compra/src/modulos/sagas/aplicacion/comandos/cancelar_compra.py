from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.sagas.infraestructura.despachadores import Despachador

@dataclass
class CancelarCompra(Comando):
    ...

class CancelarCompraHandler():
    def handle(self, comando: CancelarCompra):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-compra')


@comando.register(CancelarCompra)
def ejecutar_comando_cancelar_compra(comando: CancelarCompra):
    handler = CancelarCompraHandler()
    handler.handle(comando)