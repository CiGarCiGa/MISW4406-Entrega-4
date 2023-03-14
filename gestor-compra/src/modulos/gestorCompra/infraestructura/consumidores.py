import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from src.modulos.gestorCompra.infraestructura.schema.v1.eventos import EventoProductosReservados
from src.modulos.gestorCompra.infraestructura.schema.v1.comandos import ComandoReservarProducto, ComandoCrearCompra

from src.seedwork.infraestructura import utils
from src.modulos.gestorCompra.aplicacion.iniciar_flujo import iniciar_flujo
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.modulos.inventario.aplicacion.comandos.validar_inventario import ValidarInventario
from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrdenDTOJson

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-gestor-compra', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aero-sub-eventos', schema=AvroSchema(EventoProductosReservados))

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

def suscribirse_a_eventos_productos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-productos', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aero-sub-eventos', schema=AvroSchema(EventoProductosReservados))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido de eventos-productos: {datos}', flush=True)
            print(f'evento: {datos.evento}', flush=True)
            print(f'evento: {datos.id_compra}', flush=True)
            print(f'evento: {datos.id_reserva}', flush=True)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

##Aqui deberia iniciar la SAGA
def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-gestor-compra', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aero-sub-comandos', schema=AvroSchema(ComandoCrearCompra))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje}')
            logging.info(f'Comando recibido: {mensaje.value()}')

            map_orden = MapeadorOrdenDTOJson()
            print('mensaje :', mensaje.value(), flush=True)
            print('data :', mensaje.value().data, flush=True)
            print('type :', str(type(mensaje.value().data)), flush=True)
            print('id_usuario :', mensaje.value().data.id_usuario, flush=True)
            orden_dto = map_orden.externo_a_dto(mensaje.value().data)
            print('orden_dto ', orden_dto, flush=True)
            comando = ValidarInventario(orden_dto.fecha_creacion, orden_dto.fecha_actualizacion, orden_dto.id, orden_dto.productos)
            ejecutar_commando(comando,app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

##Esto es para probar el flujo de reservar-productos
def consumidor_inicio_flujo(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('topic-inicio-flujo-reservar-productos', 'inicio-flujo')
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