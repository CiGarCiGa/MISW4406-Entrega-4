import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.modulos.orden.infraestructura.schema.v1.comandos import ComandoCrearOrden
from src.seedwork.infraestructura import utils
from src.modulos.orden.aplicacion.iniciar_flujo import iniciar_flujo
from src.seedwork.aplicacion.comandos import ejecutar_commando

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-ordenes', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='ordenes-sub-comandos', schema=AvroSchema(ComandoCrearOrden))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            id_compra = "1"

            comando = ComandoCrearOrden(id_compra)

            ejecutar_commando(comando, app=app)

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
        consumidor = cliente.subscribe('topic-inicio-flujo-orden-creada', 'inicio-flujo')
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