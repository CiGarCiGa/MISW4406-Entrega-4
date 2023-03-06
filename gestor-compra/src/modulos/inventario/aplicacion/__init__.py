from pydispatch import dispatcher

from .handlers import HandlerInventarioIntegracion

from src.modulos.inventario.aplicacion.comandos.validar_inventario import ValidarInventario

dispatcher.connect(HandlerInventarioIntegracion.handle_validar_inventario, signal=f'{ValidarInventario.__name__}Integracion')
