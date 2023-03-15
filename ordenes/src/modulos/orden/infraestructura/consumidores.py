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
from src.modulos.orden.aplicacion.comandos.crear_orden import CrearOrden

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-orden', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='ordenes-sub-comandos', schema=AvroSchema(ComandoCrearOrden))

        while True:
            mensaje = consumidor.receive()
            data=mensaje.value().data
            print(f'Comando recibido: {data}',flush=True)
            crearOrden=CrearOrden(id_compra=data.id_compra)
            ejecutar_commando(crearOrden)
            #id_compra = "1"
            #mensaje1 = str(mensaje.value().data)
            #split_mensaje = mensaje1.split("'id_compra': '")[-1][0]
            #print(split_mensaje, flush=True)
            #iniciar_flujo(app=app, id_compra=str(split_mensaje))

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