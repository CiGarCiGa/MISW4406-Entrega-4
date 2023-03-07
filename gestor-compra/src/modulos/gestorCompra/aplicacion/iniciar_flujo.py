from src.modulos.gestorCompra.aplicacion.mapeadores import MapeadorProductoDTOJson
from src.modulos.gestorCompra.aplicacion.comandos.reservar_producto import ReservarProducto
from src.seedwork.aplicacion.comandos import ejecutar_commando

def iniciar_flujo():
    datos_dict = {
        "productos": [
            {
                "id_producto": "1",
                "cantidad": "2"
            },
            {
                "id_producto": "3",
                "cantidad": "4"
            }
        ],
        "id_compra":"1"
    }
    print('entrando', flush=True)
    map = MapeadorProductoDTOJson()
    dto = map._procesar_reserva(datos_dict)
    comando = ReservarProducto(id_compra=dto.id_compra,productos_cantidades=dto.productos_cantidades)
    ejecutar_commando(comando)