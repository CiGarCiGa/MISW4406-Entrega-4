from src.seedwork.aplicacion.dto import Mapeador as AppMap
from src.seedwork.dominio.repositorios import Mapeador as RepMap
from src.modulos.vuelos.dominio.entidades import Reserva, Aeropuerto
from src.modulos.inventario.dominio.objetos_valor import Producto, ProductoOrden
from .dto import OrdenDTO, ProductoDTO

from datetime import datetime

class MapeadorOrdenDTOJson(AppMap):
    def _procesar_orden(self, orden: dict) -> ProductoOrden:
        producto_orden_dto: list[ProductoDTO] = list()
        for productos_orden in orden.get('productos', list()):
            producto_dto: ProductoDTO = ProductoDTO(productos_orden.get('sku'), productos_orden.get('cantidad')) 
            producto_orden_dto.append(producto_dto)  
                
        return ProductoOrden(producto_orden_dto)
    
    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        orden_dto = OrdenDTO()

        productos_orden: list[ProductoDTO] = list()
        for producto_orden in externo.get('productos', list()):
            orden_dto.productos.append(self._procesar_itinerario(producto_orden))

        return orden_dto

    def dto_a_externo(self, dto: ReservaDTO) -> dict:
        return dto.__dict__

class MapeadorOrden(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_orden(self, producto_orden_dto: OrdenDTO) -> ProductoOrden:
        productos = list()

        for producto_dto in producto_orden_dto.productos:
            sku = str(producto_dto.get('sku'))
            cantidad = producto_dto.get('cantidad')

            producto: Producto(sku,cantidad)

            productos.append(producto)

        return ProductoOrden(productos)

    def obtener_tipo(self) -> type:
        return Reserva.__class__

    def locacion_a_dict(self, locacion):
        if not locacion:
            return dict(codigo=None, nombre=None, fecha_actualizacion=None, fecha_creacion=None)
        
        return dict(
                    codigo=locacion.codigo
                ,   nombre=locacion.nombre
                ,   fecha_actualizacion=locacion.fecha_actualizacion.strftime(self._FORMATO_FECHA)
                ,   fecha_creacion=locacion.fecha_creacion.strftime(self._FORMATO_FECHA)
        )
        

    def entidad_a_dto(self, entidad: Reserva) -> ReservaDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        itinerarios = list()

        for itin in entidad.itinerarios:
            odos = list()
            for odo in itin.odos:
                segmentos = list()
                for seg in odo.segmentos:
                    legs = list()
                    for leg in seg.legs:
                        fecha_salida = leg.fecha_salida.strftime(self._FORMATO_FECHA)
                        fecha_llegada = leg.fecha_llegada.strftime(self._FORMATO_FECHA)
                        origen = self.locacion_a_dict(leg.origen)
                        destino = self.locacion_a_dict(leg.destino)
                        leg = LegDTO(fecha_salida=fecha_salida, fecha_llegada=fecha_llegada, origen=origen, destino=destino)
                        
                        legs.append(leg)

                    segmentos.append(SegmentoDTO(legs))
                odos.append(OdoDTO(segmentos))
            itinerarios.append(ItinerarioDTO(odos))
        
        return ReservaDTO(fecha_creacion, fecha_actualizacion, _id, itinerarios)

    def dto_a_entidad(self, dto: ReservaDTO) -> Reserva:
        reserva = Reserva()
        reserva.itinerarios = list()

        itinerarios_dto: list[ItinerarioDTO] = dto.itinerarios

        for itin in itinerarios_dto:
            reserva.itinerarios.append(self._procesar_itinerario(itin))
        
        return reserva



