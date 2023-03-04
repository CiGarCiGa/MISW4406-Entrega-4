import src.seedwork.presentacion.api as api
import pulsar
from src.utils import utils

bp = api.crear_blueprint('inventario', '/inventario')

@bp.route('/check-inventario', methods=('GET',))
def dar_inventario_usando_query(id=None):
    client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
    producer = client.create_producer('persistent://public/default/comando_validar_inventario')
    producer.send('Validar inventario'.encode('utf-8'))
    client.close()
    return "Validar inventario"