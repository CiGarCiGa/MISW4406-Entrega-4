
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    compras: typing.List[EstadoCompra] = strawberry.field(resolver=obtener_compras)