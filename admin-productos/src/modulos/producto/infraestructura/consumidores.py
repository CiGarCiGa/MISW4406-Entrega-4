import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from src.modulos.producto.infraestructura.schema.v1.eventos import EventoProductoCreado
from src.modulos.producto.infraestructura.schema.v1.comandos import ComandoCrearProducto
from src.modulos.producto.aplicacion.comandos.reservar_productos import ReservarProducto
from src.seedwork.aplicacion.comandos import ejecutar_commando

from src.seedwork.infraestructura import utils

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-producto', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aero-sub-eventos', schema=AvroSchema(EventoProductoCreado))

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
        consumidor = cliente.subscribe('comandos-producto', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aero-sub-comandos-producto', schema=AvroSchema(ComandoReservarProducto))

        while True:
            mensaje = consumidor.receive()
            #TODO: Dependiendo del comnado debeira a ir a una operación especifica. Asumimos que esta cola solo utiliza un comando:
            data = mensaje.value().data
            reservar_producto=ReservarProducto(productos_cantidades=data.productos_cantidades, id_compra=data.id_compra )
            try:
                ejecutar_commando(reservar_producto,app=app)
                consumidor.acknowledge(mensaje)
            except:
                logging.error('ERROR: Erro al ejecutar el comando!')
                traceback.print_exc()
                consumidor.negative_acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

import uuid
import time
import os

def time_millis():
    return int(time.time() * 1000)

class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class ComandoReservarProductoPayload(Record):
    productos_cantidades = String()
    id_compra = String()

class ComandoReservarProducto(EventoIntegracion):
    data = ComandoReservarProductoPayload()

