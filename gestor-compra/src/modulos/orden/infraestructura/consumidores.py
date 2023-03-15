import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.modulos.orden.infraestructura.schema.v1.eventos import EventoOrdenCreada
from src.seedwork.infraestructura import utils
from src.modulos.orden.aplicacion.iniciar_flujo import iniciar_flujo
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.modulos.gestorCompra.infraestructura.dto import Compra

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-orden', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='ordenes-sub-eventos', schema=AvroSchema(EventoOrdenCreada))

        while True:
            mensaje = consumidor.receive()
            data = mensaje.value().data
            print(f'Evento recibido: {data}', flush=True)
            with app.app_context():
                from src.config.db import db
                compra = Compra.query.get(data.id_compra)
                compra.id_orden = data.id_orden
                compra.estado='ORDEN_CREADA'
                db.session.commit()
            consumidor.acknowledge(mensaje)
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def consumidor_inicio_flujo(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-inicio-flujo-crear-orden', 'inicio-flujo')
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido, inicia flujo')

            consumidor.acknowledge(mensaje)     
            iniciar_flujo(app=app)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose a iniciar flujo!')
        traceback.print_exc()
        if cliente:
            cliente.close()