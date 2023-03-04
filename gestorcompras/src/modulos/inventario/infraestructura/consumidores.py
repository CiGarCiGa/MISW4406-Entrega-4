import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.modulos.inventario.infraestructura.schema.v1.eventos import EventoInventarioValidado
from src.modulos.inventario.infraestructura.schema.v1.comandos import ComandoValidarInventario
from src.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://0.0.0.0:6650')
        consumidor = cliente.subscribe('eventos-inventario', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='inventario-sub-eventos', schema=AvroSchema(EventoInventarioValidado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://0.0.0.0:6650')
        consumidor = cliente.subscribe('comandos-inventario', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='inventario-sub-comandos', schema=AvroSchema(ComandoValidarInventario))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()