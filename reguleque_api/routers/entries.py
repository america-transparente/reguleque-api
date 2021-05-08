from fastapi import APIRouter

from reguleque_api.db import engine
from odmantic.bson import ObjectId
from reguleque_api.db.models import RevenueEntry

router = APIRouter(prefix="/entries")


@router.get("/")
async def all_entries():
    return await engine.find(RevenueEntry)


# TODO: UNSAFE, AUTH NEEDED
@router.put("/", response_model=RevenueEntry)
async def new_entry(entry: RevenueEntry):
    await engine.save(entry)
    return entry


@router.get("/{entry_id}", response_model=RevenueEntry)
async def get_entry(entry_id: ObjectId):
    return await engine.find_one(RevenueEntry, RevenueEntry.id == entry_id)


@router.get("/count", response_model=int)
async def count_entries():
    return await engine.count(RevenueEntry)
