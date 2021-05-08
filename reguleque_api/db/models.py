from typing import Optional
from datetime import datetime
from odmantic import Field, Model, AIOEngine
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ASCENDING, DESCENDING


class RevenueEntry(Model):
    nombre: str
    organismo_nombre: str
    organismo_codigo: Optional[str] = None

    region: Optional[str] = None

    tipo_cargo: Optional[str] = None
    tipo_contrato: Optional[str] = None
    tipo_calificacion: Optional[str] = None
    tipo_estamento: Optional[str] = None

    fecha_publicacion: Optional[datetime] = None
    año: Optional[int] = Field(None, ge=1850)
    mes: Optional[str] = None

    grado_eus: Optional[str] = None

    tipo_contrato: Optional[str] = None
    remuneracion_bruta: Optional[int] = None
    remuneracion_liquida_mensual: Optional[int] = None
    observaciones: Optional[str] = None


async def init_db(engine: AIOEngine, collection: AsyncIOMotorCollection):
    collection.create_index(
        [
            ("nombre", ASCENDING),
        ]
    )
