import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from src.modulos.gestorCompra.infraestructura.schema.v1.eventos import EventoProductoReservado
from src.modulos.gestorCompra.infraestructura.schema.v1.comandos import ComandoReservarProducto

from src.seedwork.infraestructura import utils

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-gestor-compra', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aero-sub-eventos', schema=AvroSchema(EventoProductoCreado))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido: {datos}')

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-gestor-compra', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aero-sub-comandos', schema=AvroSchema(ComandoReservarProducto))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje}')
            logging.error(f'Comando recibido: {mensaje.value()}')

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()