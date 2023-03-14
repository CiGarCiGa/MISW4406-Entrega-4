
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    compras: typing.List[Compra] = strawberry.field(resolver=obtener_compras)