from src.seedwork.aplicacion.dto import Mapeador as AppMap
from src.seedwork.dominio.repositorios import Mapeador as RepMap
from src.modulos.gestorCompra.dominio.entidades import ReservaProducto
from src.modulos.gestorCompra.dominio.objetos_valor import ProductoReserva
from .dto import ProductoDTO, ReservarProductoDTO
from abc import ABC

class MapeadorProductoDTOJson(AppMap):
    def _procesar_reserva(self, reserva: dict) -> ProductoReserva:
        productos_cantidades_dto='='.join([(w.get('id_producto') + ":" + str(w.get('cantidad', int))) for w in reserva.get('productos', list())])
        return ProductoReserva(productos_cantidades=productos_cantidades_dto, id_compra=reserva.get('id_compra'))

    def externo_a_dto(self, externo: dict) -> ProductoReserva:
        producto_reserva_dto = ProductoReserva()
        producto_reserva_dto.id_compra = externo.get('id_compra')
        for producto in externo.get('productos', list()):
            producto_reserva_dto.productos.append(self._procesar_orden(producto))

        return producto_reserva_dto

    def dto_a_externo(self, dto: ProductoReserva) -> dict:
        return dto.__dict__
"""
class MapeadorProducto(ABC):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_producto_orden(self, productos_reservados_dto: ReservarProductoDTO) -> ProductoReserva:
        productos = list()

        for producto_dto in productos_reservados_dto.productos:
            id_producto = str(producto_dto.get('id_producto'))
            cantidad = producto_dto.get('cantidad')

            producto: Producto(id_producto,cantidad)

            productos.append(producto)

        return ProductoReserva(productos, productos_reservados_dto.id_compra)

    def obtener_tipo(self) -> type:
        return ProductoReserva.__class__

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden()
        orden.productos = list()

        productos_orden_dto: list[ProductoDTO] = dto.productos

        for producto in productos_orden_dto:
            orden.productos.append(self._procesar_producto_orden(producto))

        return orden
"""