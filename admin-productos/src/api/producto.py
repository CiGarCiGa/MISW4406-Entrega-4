import src.seedwork.presentacion.api as api
import json

from flask import redirect, render_template, request, session, url_for
from flask import Response

bp = api.crear_blueprint('productos', '/productos')

@bp.route('/producto', methods=('GET',))
def dar_reserva_usando_query(id=None):
    return "prueba"