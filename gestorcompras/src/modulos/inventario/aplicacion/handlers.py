from src.seedwork.aplicacion.handlers import Handler
from src.modulos.inventario.infraestructura.despachadores import Despachador

class HandlerInventarioIntegracion(Handler):

    @staticmethod
    def handle_inventario_validado(evento):
        print('handle inventario validado', flush=True)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-inventario')