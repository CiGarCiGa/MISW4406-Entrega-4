from pydispatch import dispatcher

from .handlers import HandlerOrdenIntegracion

from src.modulos.orden.dominio.eventos import OrdenCreada

dispatcher.connect(HandlerOrdenIntegracion.handle_orden_creada, signal=f'{OrdenCreada.__name__}Integracion')
