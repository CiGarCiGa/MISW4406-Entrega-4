import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


AEROALPES_HOST = os.getenv("AEROALPES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
id_usuario = ''

def obtener_compras(root) -> typing.List["Compra"]:
    compras_json = requests.get(f'http://{AEROALPES_HOST}:5000/usuario/{id_usuario}/compras').json()
    compras = []

    for compra in compras_json:
        compras.append(
            Compra(
                id_usuario=compra.get('id_usuario'), 
                estado=compra.get('estado')
            )
        )

    return compras

@strawberry.type
class Compra:
    id_usuario: str
    productos: str
    domicilio: str
    #itinerarios: typing.List[Itinerario]

@strawberry.type
class CompraRespuesta:
    mensaje: str
    codigo: int






