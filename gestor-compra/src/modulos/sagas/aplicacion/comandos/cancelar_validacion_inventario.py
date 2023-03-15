from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.config.db import db
from src.modulos.sagas.infraestructura.despachadores import Despachador

@dataclass
class CancelarValidacionInventario(Comando):
    ...

class CancelarValidacionInventarioHandler():
    def handle(self, comando: CancelarValidacionInventario):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-inventario')


@comando.register(CancelarValidacionInventario)
def ejecutar_comando_cancelar_validacion_inventario(comando: CancelarValidacionInventario):
    handler = CancelarValidacionInventarioHandler()
    handler.handle(comando)