import pulsar
from pulsar.schema import *
import logging

from src.modulos.gestorCompra.infraestructura.schema.v1.eventos import EventoProductoReservado, ProductoReservadoPayload
from src.modulos.gestorCompra.infraestructura.schema.v1.comandos import ComandoReservarProducto, ComandoReservarProductoPayload
from src.seedwork.infraestructura import utils

#from src.modulos.gestorCompra.infraestructura.mapeadores import MapadeadorEventosProducto

class Despachador:
    def __init__(self):
        self.mapper = None #MapadeadorEventosProducto()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoReservarProducto))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        print('pub productos_Cantidades:' + comando.productos_cantidades, flush=True)
        print('pub id_compra:' + comando.id_compra, flush=True)
        payload = ComandoReservarProductoPayload(
            id_compra=str(comando.id_compra),
            productos_cantidades=str(comando.productos_cantidades)
            # agregar itinerarios
        )
        comando_integracion = ComandoReservarProducto(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoReservarProducto))
