from sqlmodel import SQLModel, Field
from enum import Enum
from typing import Optional

class EstadoUsuario(str, Enum):
    activo = "activo"
    inactivo = "inactivo"
    eliminado = "eliminado"

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    estado: EstadoUsuario = EstadoUsuario.activo
    premium: bool = False
