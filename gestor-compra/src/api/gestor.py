import src.seedwork.presentacion.api as api
import json

from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.modulos.gestorCompra.aplicacion.comandos.reservar_producto import ReservarProducto
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.modulos.gestorCompra.aplicacion.mapeadores import MapeadorProductoDTOJson
from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrdenDTOJson
from src.modulos.inventario.aplicacion.comandos.validar_inventario import ValidarInventario
from src.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('compras', '/compras')
# Eliminar este endpoint, esto es solo para probar la publicacion de comandos al admin-product
@bp.route('/productos', methods=('POST',))
def dar_reserva_usando_query(id=None):
    try:
        reserva_dict = request.json
        print('entrando', flush=True)
        map_reservar_producto = MapeadorProductoDTOJson()
        reservar_productos_dto = map_reservar_producto._procesar_reserva(reserva_dict)
        print('productos_Cantidades:' + reservar_productos_dto.productos_cantidades, flush=True)
        print('id_compra:' + reservar_productos_dto.id_compra, flush=True)
        comando = ReservarProducto(id_compra=reservar_productos_dto.id_compra,productos_cantidades=reservar_productos_dto.productos_cantidades)
        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
bp = api.crear_blueprint('inventario', '/inventario')
# Eliminar este endpoint, esto es solo para probar la publicacion de comandos al admin-product
@bp.route('/validar-inventario', methods=('POST',))
def validar_inventario():
    try:
        orden_dict = {
            "productos": [
                {
                    "sku": "1",
                    "cantidad": "2"
                }
            ]
        }
        print('entrando', flush=True)
        map_orden = MapeadorOrdenDTOJson()
        orden_dto = map_orden.externo_a_dto(orden_dict)
        print('despues de externo a dto', flush=True)
        comando = ValidarInventario(orden_dto.fecha_creacion, orden_dto.fecha_actualizacion, orden_dto.id, orden_dto.productos)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
