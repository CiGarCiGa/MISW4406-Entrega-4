""" Mapeadores para la capa de infrastructura del dominio de producto

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from src.seedwork.dominio.repositorios import Mapeador
from src.seedwork.infraestructura.utils import unix_time_millis
#from src.modulos.producto.dominio.entidades import Producto
from src.modulos.producto.dominio.eventos import ProductoAprobada, ProductoCancelada, ProductoAprobada, ProductoPagada, ProductoCreada, EventoProducto

from .dto import EventosProducto as ProductoDTO
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion
from pulsar.schema import *

class MapadeadorEventosProducto(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            ProductoCreada: self._entidad_a_producto_creado,
            ProductoAprobada: self._entidad_a_producto_aprobado,
            ProductoCancelada: self._entidad_a_producto_cancelado,
            ProductoPagada: self._entidad_a_producto_pagado
        }

    def obtener_tipo(self) -> type:
        return EventoProducto.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_producto_creado(self, entidad: ProductoCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import ProductoCreadoPayload, EventoProductoCreado

            payload = ProductoCreadoPayload(
                id_producto=str(evento.id_producto),
                descripcion=str(evento.descripcion),
                cantidad=str(evento.cantidad),
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoProductoCreado(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'ProductoCreado'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'admin-productos'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def _entidad_a_producto_aprobado(self, entidad: ProductoAprobada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def _entidad_a_producto_cancelado(self, entidad: ProductoCancelada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def _entidad_a_producto_pagado(self, entidad: ProductoPagada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def entidad_a_dto(self, entidad: EventoProducto, version=LATEST_VERSION) -> ProductoDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    #def dto_a_entidad(self, dto: ProductoDTO, version=LATEST_VERSION) -> Producto:
    #    raise NotImplementedError
