from src.seedwork.aplicacion.dto import Mapeador as AppMap
from src.seedwork.dominio.repositorios import Mapeador as RepMap
from src.modulos.inventario.dominio.entidades import Orden
from src.modulos.inventario.dominio.objetos_valor import Producto, ProductoOrden
from src.modulos.gestorCompra.infraestructura.schema.v1.comandos import ComandoCrearCompraPayload
from .dto import OrdenDTO, ProductoDTO
from abc import ABC
import json

class MapeadorOrdenDTOJson(AppMap):
    def _procesar_orden(self, orden: dict) -> ProductoOrden:
        producto_orden_dto: list[ProductoDTO] = list()
        for productos_orden in orden.get('productos', list()):
            producto_dto: ProductoDTO = ProductoDTO(productos_orden.get('sku'), productos_orden.get('cantidad')) 
            producto_orden_dto.append(producto_dto)

        return ProductoOrden(producto_orden_dto)

    def externo_a_dto(self, externo: ComandoCrearCompraPayload) -> OrdenDTO:

        orden_dto = OrdenDTO(id=externo.id_usuario,productos= externo.productos_cantidades)
        return orden_dto

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__

class MapeadorOrden(ABC):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_producto_orden(self, producto_orden_dto: OrdenDTO) -> ProductoOrden:
        productos = list()

        for producto_dto in producto_orden_dto.productos:
            sku = str(producto_dto.get('sku'))
            cantidad = producto_dto.get('cantidad')

            producto: Producto(sku,cantidad)

            productos.append(producto)

        return ProductoOrden(productos)

    def obtener_tipo(self) -> type:
        return Orden.__class__

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden()
        orden.productos = dto.productos
        orden.id=dto.id
        #productos_orden_dto: list[ProductoDTO] = dto.productos

        #for producto in productos_orden_dto:
        #    orden.productos.append(self._procesar_producto_orden(producto))

        return orden