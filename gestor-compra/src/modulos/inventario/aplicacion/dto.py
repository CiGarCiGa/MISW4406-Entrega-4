from dataclasses import dataclass, field
from src.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ProductoDTO(DTO):
    sku: str
    cantidad: str

@dataclass(frozen=True)
class OrdenDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id_usuario : str = field(default_factory=str)
    id: str = field(default_factory=str)
    productos: str = field(default_factory=str)