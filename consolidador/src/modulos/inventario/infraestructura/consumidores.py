import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.modulos.inventario.infraestructura.schema.v1.eventos import EventoInventarioValidado
from src.modulos.inventario.infraestructura.schema.v1.comandos import ComandoValidarInventario
from src.seedwork.infraestructura import utils
from src.modulos.inventario.aplicacion.iniciar_flujo import iniciar_flujo
from src.modulos.inventario.aplicacion.comandos.validar_inventario import ValidarInventario
from src.seedwork.aplicacion.comandos import ejecutar_commando
"""
def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-inventario', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='inventario-sub-eventos', schema=AvroSchema(EventoInventarioValidado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}',flush=True)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
"""
def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-inventario', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='inventario-sub-comandos', schema=AvroSchema(ComandoValidarInventario))

        while True:
            mensaje = consumidor.receive()
            data = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}',flush=True)
            validar_inventario=ValidarInventario(id=data.id_orden, productos_orden=data.productos_orden,fecha_creacion="", fecha_actualizacion="")
            ejecutar_commando(validar_inventario, app=app)
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def consumidor_inicio_flujo(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-inicio-flujo-consolidador', 'inicio-flujo')
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido, inicia flujo',flush=True)

            consumidor.acknowledge(mensaje)
            iniciar_flujo()

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose a iniciar flujo!')
        traceback.print_exc()
        if cliente:
            cliente.close()