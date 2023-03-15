import pulsar
from pulsar.schema import *

from src.seedwork.infraestructura import utils

class Despachador:
    def __init__(self):
        ...

    def publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(mensaje.__class__))
        publicador.send(mensaje)
        cliente.close()

"""     def publicar_evento(self, evento, topico):
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
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoReservarProducto)) """