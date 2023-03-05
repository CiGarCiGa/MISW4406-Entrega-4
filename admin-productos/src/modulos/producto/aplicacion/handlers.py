from src.modulos.producto.dominio.eventos import ProductoCreado, ProductoCancelado, ProductoAprobado, ProductoPagado
from src.seedwork.aplicacion.handlers import Handler
from src.modulos.producto.infraestructura.despachadores import Despachador

class HandlerProductoIntegracion(Handler):

    @staticmethod
    def handle_producto_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-producto')

    @staticmethod
    def handle_producto_cancelado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-producto')

    @staticmethod
    def handle_producto_aprobado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-producto')

    @staticmethod
    def handle_producto_pagado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-producto')


