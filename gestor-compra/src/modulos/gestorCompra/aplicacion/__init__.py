from pydispatch import dispatcher

from .handlers import HandlerProductoIntegracion

from src.modulos.gestorCompra.dominio.eventos import CompraCreada, CompraCancelada, CompraAprobada, CompraPagada
from src.modulos.gestorCompra.dominio.eventos import ReservarProducto

"""
dispatcher.connect(HandlerProductoIntegracion.handle_compra_creada, signal=f'{CompraCreada.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_compra_cancelado, signal=f'{CompraCancelada.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_compra_pagado, signal=f'{CompraPagada.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_compra_aprobado, signal=f'{CompraAprobada.__name__}Integracion')
"""
dispatcher.connect(HandlerProductoIntegracion.handle_reservar_producto, signal=f'{ReservarProducto.__name__}Integracion')