import pulsar
from pulsar.schema import *

from src.modulos.inventario.infraestructura.schema.v1.eventos import EventoInventarioValidado, InventarioValidadoPayload
from src.modulos.inventario.infraestructura.schema.v1.comandos import ComandoValidarInventario, ComandoValidarInventarioPayload
from src.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = InventarioValidadoPayload(
            id_orden=str(evento.id_orden), 
            evento=str(evento.evento), 
        )
        evento_integracion = EventoInventarioValidado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoInventarioValidado))

    def publicar_comando(self, comando, topico):
        payload = ComandoValidarInventarioPayload(
            productos_orden=str(comando.productos_orden),
            id_orden=str(comando.id)
        )
        comando_integracion = ComandoValidarInventario(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoValidarInventario))
