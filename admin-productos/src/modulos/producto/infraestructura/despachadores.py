import pulsar
from pulsar.schema import *

from src.modulos.producto.infraestructura.schema.v1.eventos import EventoProductoCreado, ProductoCreadoPayload
from src.modulos.producto.infraestructura.schema.v1.comandos import ComandoCrearProducto, ComandoCrearProductoPayload
from src.seedwork.infraestructura import utils

#from src.modulos.producto.infraestructura.mapeadores import MapadeadorEventosProducto

class Despachador:
    def __init__(self):
        self.mapper = None #MapadeadorEventosProducto()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoProductoCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearProductoPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearProducto(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearProducto))
