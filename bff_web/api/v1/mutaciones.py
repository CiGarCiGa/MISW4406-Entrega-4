import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    # TODO Agregue objeto de itinerarios o reserva
    @strawberry.mutation
    async def crear_compra(self, id_usuario: str, productos: str, domicilio: str, info: Info) -> CompraRespuesta:
        print(f"ID Usuario: {id_usuario}, productos: {productos},domicilio: {domicilio}")
        payload = dict(
            id_usuario = id_usuario,
            productos = productos,
            domicilio = domicilio
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoCompra",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-gestor-compra", "public/default/comandos-gestor-compra")
        
        return CompraRespuesta(mensaje="Procesando Mensaje", codigo=203)