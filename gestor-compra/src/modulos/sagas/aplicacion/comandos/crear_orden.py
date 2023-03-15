from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.sagas.infraestructura.despachadores import Despachador

@dataclass
class CrearOrden(Comando):
    ...

class CrearOrdenHandler():
    def handle(self, comando: CrearOrden):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-orden')


@comando.register(CrearOrden)
def ejecutar_comando_crear_orden(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)