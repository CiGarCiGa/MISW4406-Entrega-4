from src.modulos.inventario.aplicacion.mapeadores import MapeadorOrdenDTOJson
from src.modulos.inventario.aplicacion.comandos.validar_inventario import ValidarInventario
from src.seedwork.aplicacion.comandos import ejecutar_commando

def iniciar_flujo():
    orden_dict = {
        "productos": [
            {
                "sku": "1",
                "cantidad": "2"
            }
        ]
    }
    print('entrando', flush=True)
    map_orden = MapeadorOrdenDTOJson()
    orden_dto = map_orden.externo_a_dto(orden_dict)
    print('despues de externo a dto', flush=True)
    comando = ValidarInventario(orden_dto.fecha_creacion, orden_dto.fecha_actualizacion, orden_dto.id, orden_dto.productos)

    ejecutar_commando(comando)