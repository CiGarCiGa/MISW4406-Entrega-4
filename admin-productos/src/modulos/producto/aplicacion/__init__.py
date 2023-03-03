from pydispatch import dispatcher

from .handlers import HandlerProductoIntegracion

from src.modulos.producto.dominio.eventos import ProductoCreada, ProductoCancelada, ProductoAprobada, ProductoPagada

dispatcher.connect(HandlerProductoIntegracion.handle_producto_creada, signal=f'{ProductoCreada.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_producto_cancelada, signal=f'{ProductoCancelada.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_producto_pagado, signal=f'{ProductoPagada.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_producto_aprobado, signal=f'{ProductoAprobada.__name__}Integracion')