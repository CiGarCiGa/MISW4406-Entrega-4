from src.modulos.gestorCompra.dominio.eventos import CompraCreada, CompraCancelada, CompraAprobada, CompraPagada
from src.seedwork.aplicacion.handlers import Handler
from src.modulos.gestorCompra.infraestructura.despachadores import Despachador

class HandlerProductoIntegracion(Handler):

    @staticmethod
    def handle_compra_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compra')

    @staticmethod
    def handle_reservar_producto(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'comandos-producto')

