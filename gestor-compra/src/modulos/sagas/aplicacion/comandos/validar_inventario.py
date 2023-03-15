from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.sagas.infraestructura.despachadores import Despachador

@dataclass
class ValidarInventario(Comando):
    ...

class ValidarInventarioHandler():
    def handle(self, comando: ValidarInventario):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-inventario')


@comando.register(ValidarInventario)
def ejecutar_comando_validar_inventario(comando: ValidarInventario):
    handler = ValidarInventarioHandler()
    handler.handle(comando)