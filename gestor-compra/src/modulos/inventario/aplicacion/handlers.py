from src.seedwork.aplicacion.handlers import Handler
from src.modulos.inventario.infraestructura.despachadores import Despachador

class HandlerInventarioIntegracion(Handler):

    @staticmethod
    def handle_validar_inventario(evento):
        print('handle validar inventario', flush=True)
        despachador = Despachador()
        despachador.publicar_comando(evento, 'comandos-inventario')