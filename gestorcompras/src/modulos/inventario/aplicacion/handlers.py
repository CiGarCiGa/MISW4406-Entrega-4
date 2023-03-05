from src.seedwork.aplicacion.handlers import Handler
from src.modulos.inventario.infraestructura.despachadores import Despachador

class HandlerInventarioIntegracion(Handler):

    @staticmethod
    def handle_inventario_validado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-inventario')