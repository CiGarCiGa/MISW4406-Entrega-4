import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


GESTOR_HOST = os.getenv("GESTOR_HOST", default="gestor-compra")
GESTOR_PORT = os.getenv("GESTOR_PORT", default="5001")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_compras(root, id_usuario: str) -> typing.List["EstadoCompra"]:
    compras_json = requests.get(f'http://{GESTOR_HOST}:{GESTOR_PORT}/usuarios/{id_usuario}/compras').json()
    compras = []

    for compra in compras_json:
        compras.append(
            EstadoCompra(
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
class EstadoCompra:
    id_usuario: str
    estado: str

@strawberry.type
class CompraRespuesta:
    mensaje: str
    codigo: int






