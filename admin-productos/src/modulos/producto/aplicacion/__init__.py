from pydispatch import dispatcher

from .handlers import HandlerProductoIntegracion

from src.modulos.producto.dominio.eventos import ProductoCreado, ProductoCancelado, ProductoAprobado, ProductoPagado

dispatcher.connect(HandlerProductoIntegracion.handle_producto_creado, signal=f'{ProductoCreado.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_producto_cancelado, signal=f'{ProductoCancelado.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_producto_pagado, signal=f'{ProductoPagado.__name__}Integracion')
dispatcher.connect(HandlerProductoIntegracion.handle_producto_aprobado, signal=f'{ProductoAprobado.__name__}Integracion')