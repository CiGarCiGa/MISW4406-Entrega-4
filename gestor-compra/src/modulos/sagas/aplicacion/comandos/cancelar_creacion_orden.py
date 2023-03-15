from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.sagas.infraestructura.despachadores import Despachador

@dataclass
class CancelarCreacionOrden(Comando):
    ...

class CancelarCreacionOrdenHandler():
    def handle(self, comando: CancelarCreacionOrden):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-orden')


@comando.register(CancelarCreacionOrden)
def ejecutar_comando_cancelar_creacion_orden(comando: CancelarCreacionOrden):
    handler = CancelarCreacionOrdenHandler()
    handler.handle(comando)