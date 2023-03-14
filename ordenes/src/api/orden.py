import src.seedwork.presentacion.api as api
import json
from src.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request, Response

from src.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('orden', '/orden')

@bp.route('/orden-creada', methods=('POST',))
def orden_creada():
    try:
        orden_dict = request.json
        #comando = ValidarInventario(orden_dto.fecha_creacion, orden_dto.fecha_actualizacion, orden_dto.id, orden_dto.productos)

        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        #ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')