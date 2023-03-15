from src.seedwork.aplicacion.handlers import Handler
from src.modulos.orden.infraestructura.despachadores import Despachador

class HandlerOrdenIntegracion(Handler):

    @staticmethod
    def handle_orden_creada(evento):
        print('handle orden creada', flush=True)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden')