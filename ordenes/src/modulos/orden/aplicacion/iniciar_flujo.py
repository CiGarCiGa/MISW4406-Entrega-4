from src.modulos.orden.aplicacion.comandos.crear_orden import CrearOrden
from src.seedwork.aplicacion.comandos import ejecutar_commando

def iniciar_flujo(app=None, id_compra="1"):
    comando = CrearOrden(id_compra)

    ejecutar_commando(comando)