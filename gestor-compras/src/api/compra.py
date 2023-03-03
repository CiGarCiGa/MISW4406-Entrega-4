import src.seedwork.presentacion.api as api
import json
import pulsar

from flask import redirect, render_template, request, session, url_for
from flask import Response

bp = api.crear_blueprint('compras', '/compras')



@bp.route('/reserva', methods=('GET',))
def dar_reserva_usando_query(id=None):
    client = pulsar.Client('pulsar://broker:6650')
    producer = client.create_producer('persistent://public/default/comando_reservar_producto')
    producer.send('Hello Pulsar'.encode('utf-8'))
    client.close()
    return "prueba"