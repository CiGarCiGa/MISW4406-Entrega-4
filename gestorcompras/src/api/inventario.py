import src.seedwork.presentacion.api as api
import json
from src.modulos.inventario.aplicacion.servicios import ServicioReserva
from src.modulos.inventario.aplicacion.dto import ReservaDTO
from src.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request, Response

from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrdenDTOJson
from src.modulos.inventario.aplicacion.comandos.validar_inventario import ValidarInventario
from src.modulos.inventario.aplicacion.queries.obtener_reserva import ObtenerReserva
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('inventario', '/inventario')

@bp.route('/check-inventario', methods=('POST',))
def validar_inventario(id=None):
    try:
        orden_dict = request.json

        map_orden = MapeadorOrdenDTOJson()
        orden_dto = map_orden.externo_a_dto(orden_dict)

        comando = CrearReserva(reserva_dto.fecha_creacion, reserva_dto.fecha_actualizacion, reserva_dto.id, reserva_dto.itinerarios)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')