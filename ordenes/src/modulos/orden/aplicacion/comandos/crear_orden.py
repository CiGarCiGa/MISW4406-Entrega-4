from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.orden.dominio.entidades import Orden
from src.modulos.orden.infraestructura.despachadores import Despachador
from src.modulos.orden.dominio.eventos import OrdenCreada
import random
import uuid

@dataclass
class CrearOrden(Comando):
    id_compra: str

class CrearOrdenHandler():
    
    def handle(self, comando: CrearOrden):
        print('Crear orden handler')
        generar_id_orden = uuid.uuid1()
        despachador = Despachador()
        evento=OrdenCreada(id_orden=generar_id_orden, id_compra=comando.id_compra)
        despachador.publicar_evento(evento, 'eventos-orden')

@comando.register(CrearOrden)
def ejecutar_comando_crear_orden(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
    