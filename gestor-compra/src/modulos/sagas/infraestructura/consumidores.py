import pulsar,_pulsar
from pulsar.schema import *
import aiopulsar
import uuid
import time
import logging
import traceback
import datetime

from src.modulos.sagas.aplicacion.coordinadores.saga_compras import oir_mensaje

from src.seedwork.infraestructura import utils

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
                    oir_mensaje(mensaje)

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()