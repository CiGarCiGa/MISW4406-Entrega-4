import src.seedwork.presentacion.api as api
import json

from flask import redirect, render_template, request, session, url_for
from flask import Response

bp = api.crear_blueprint('vuelos', '/vuelos')

@bp.route('/reserva', methods=('GET',))
@bp.route('/reserva/<id>', methods=('GET',))
def dar_reserva_usando_query(id=None):
    return "prueba"