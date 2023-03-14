import pulsar,_pulsar
from pulsar.schema import *
import aiopulsar
import uuid
import time
import logging
import traceback
import datetime

from src.modulos.sagas.infraestructura.schema.v1.eventos import EventoProductoReservado
from src.modulos.sagas.infraestructura.schema.v1.comandos import ComandoReservarProducto

from src.seedwork.infraestructura import utils
from src.modulos.sagas.aplicacion.iniciar_flujo import iniciar_flujo

async def suscribirse_a_topico(topico: str, suscripcion: str, schema: Record, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared):
    try:
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as cliente:
            async with cliente.subscribe(
                topico,
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion,
                schema=AvroSchema(schema)
            ) as consumidor:
                while True:
                    print(topico)
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos}')
                    await consumidor.acknowledge(mensaje)
                    # TODO pasar mensaje

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
"""
def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-gestor-compra', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aero-sub-eventos', schema=AvroSchema(EventoProductoReservado))

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
            cliente.close() """

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

##Esto es para probar el flujo de realizar-compra
def consumidor_inicio_flujo(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-inicio-flujo-realizar-compra', 'inicio-flujo')
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido, inicia flujo')

            consumidor.acknowledge(mensaje)
            iniciar_flujo()

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose a iniciar flujo!')
        traceback.print_exc()
        if cliente:
            cliente.close()