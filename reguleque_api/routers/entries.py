from fastapi import APIRouter, Depends

from reguleque_api.db import DatabaseManager, get_database
from bson.decimal128 import Decimal128
from odmantic.bson import ObjectId

router = APIRouter()


@router.get("/")
async def all_entries(db: DatabaseManager = Depends(get_database)):
    entries = await db.get_entries()
    return entries


@router.get("/{entry_id}")
async def one_entry(entry_id: ObjectId, db: DatabaseManager = Depends(get_database)):
    entry = await db.get_entry(entry_id=entry_id)
    return entry
