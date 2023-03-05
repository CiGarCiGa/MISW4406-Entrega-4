from pydispatch import dispatcher

from .handlers import HandlerInventarioIntegracion

from src.modulos.inventario.dominio.eventos import InventarioValidado

dispatcher.connect(HandlerInventarioIntegracion.handle_inventario_validado, signal=f'{InventarioValidado.__name__}Integracion')
