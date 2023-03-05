import src.seedwork.presentacion.api as api
import json

from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.modulos.gestorCompra.aplicacion.comandos.reservar_producto import ReservarProducto
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.modulos.gestorCompra.aplicacion.mapeadores import MapeadorProductoDTOJson
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