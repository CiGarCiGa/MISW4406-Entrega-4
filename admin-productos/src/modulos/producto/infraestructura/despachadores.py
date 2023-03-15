import pulsar
from pulsar.schema import *

from src.modulos.producto.infraestructura.schema.v1.eventos import EventoProductosReservados, ProductosReservadosPayload
from src.modulos.producto.infraestructura.schema.v1.comandos import ComandoCrearProducto, ComandoCrearProductoPayload
from src.seedwork.infraestructura import utils
from src.seedwork.infraestructura.utils import unix_time_millis
#from src.modulos.producto.infraestructura.mapeadores import MapadeadorEventosProducto
import json

class Despachador:
    def __init__(self):
        self.mapper = None #None MapadeadorEventosProducto()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoProductosReservados))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        print(str(evento),flush=True)
        payload = ProductosReservadosPayload(
            id_reserva = str(evento.id_reserva),
            id_compra = str(evento.id_compra),
            evento = str(evento.evento)
        )
        new_evento=EventoProductosReservados(data=payload)
        print(str(new_evento),flush=True)
        self._publicar_mensaje(new_evento, topico, AvroSchema(EventoProductosReservados))
