import src.seedwork.presentacion.api as api
import json
from src.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request, Response

from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrdenDTOJson
from src.modulos.inventario.aplicacion.comandos.validar_inventario import ValidarInventario
from src.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('inventario', '/inventario')

@bp.route('/check-inventario', methods=('POST',))
def validar_inventario():
    try:
        orden_dict = request.json
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