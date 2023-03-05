from dataclasses import dataclass, field
from src.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ProductoDTO(DTO):
    id_producto: str
    cantidad: int

@dataclass(frozen=True)
class ReservarProductoDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id_compra: str = field(default_factory=str)
    productos: list[ProductoDTO] = field(default_factory=list)