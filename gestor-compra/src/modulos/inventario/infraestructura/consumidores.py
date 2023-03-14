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
from src.modulos.gestorCompra.aplicacion.comandos.reservar_producto_concat import ReservarProducto
from src.seedwork.aplicacion.comandos import ejecutar_commando
#from src.modulos.gestorCompra.infraestructura.dto import Compra

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-inventario', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='inventario-sub-eventos', schema=AvroSchema(EventoInventarioValidado))

        while True:
            mensaje = consumidor.receive()
            data = mensaje.value().data
            print(f'Evento recibido: {data}', flush=True)
            """"
            with app.app_context():
                from src.config.db import db
                compra = Compra.query.get(data.id_orden)
                reservar_producto=ReservarProducto(productos_cantidades=compra.productos_cantidades, id_compra=data.id_compra )
                ejecutar_commando(comando=reservar_producto,app=app)
            """
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

def consumidor_inicio_flujo(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-inicio-flujo-gestor-inventario', 'inicio-flujo')
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