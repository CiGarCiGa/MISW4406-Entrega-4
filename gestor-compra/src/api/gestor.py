import src.seedwork.presentacion.api as api
import json

from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.modulos.gestorCompra.aplicacion.comandos.reservar_producto import ReservarProducto
from src.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('compras', '/compras')
# Eliminar este endpoint, esto es solo para probar la publicacion de comandos al admin-product
@bp.route('/productos', methods=('POST',))
def dar_reserva_usando_query(id=None):
    reserva_dict = request.json
    comando = ReservarProducto(reserva_dict['id_producto'],reserva_dict['cantidad'], reserva_dict['id_compra'])
    ejecutar_commando(comando)
    return "prueba"