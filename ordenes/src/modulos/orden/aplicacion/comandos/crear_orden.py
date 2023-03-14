from src.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando
from src.modulos.orden.dominio.entidades import Orden

@dataclass
class CrearOrden(Comando):
    id_compra: str

class CrearOrdenHandler():
    
    def handle(self, comando: CrearOrden):
        print('Crear orden handler')
        orden: Orden(comando.id_compra)
        orden.crear_orden(orden)

@comando.register(CrearOrden)
def ejecutar_comando_crear_orden(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
    