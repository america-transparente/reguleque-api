from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from odmantic.bson import Decimal128, ObjectId


class RevenueEntry(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")

    nombre: str
    organismo_nombre: str
    organismo_codigo: str

    region: str = None

    tipo_cargo: str = None
    tipo_contrato: str = None
    tipo_calificacion: Optional[str] = None
    tipo_estamento: Optional[str] = None

    fecha_publicacion: Optional[datetime] = None
    año: Optional[int] = Field(None, ge=1850)
    mes: Optional[str] = None

    grado_eus: Optional[int] = None

    tipo_contrato: str = None
    remuneracion_bruta: Optional[Decimal128] = None
    remuneracion_liquida_mensual: Optional[Decimal128] = None
    observaciones: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
