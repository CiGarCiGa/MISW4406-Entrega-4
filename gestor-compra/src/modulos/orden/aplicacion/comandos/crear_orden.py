from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.orden.infraestructura.despachadores import Despachador
import random

@dataclass
class CrearOrden(Comando):
    id_compra: str

class CrearOrdenHandler():
    
    def handle(self, comando: CrearOrden):
        print('Crear orden handler')
        generar_id_orden = random.randint(1,50)
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-orden')

@comando.register(CrearOrden)
def ejecutar_comando_crear_orden(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
    