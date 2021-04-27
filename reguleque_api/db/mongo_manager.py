import logging
from typing import List
from odmantic.bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from reguleque_api.db import DatabaseManager
from reguleque_api.db.models import RevenueEntry


class MongoManager(DatabaseManager):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect_to_database(self, path: str):
        logging.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(path, maxPoolSize=10, minPoolSize=10)
        self.db = self.client.entries
        logging.info("Connected to MongoDB.")

    async def close_database_connection(self):
        logging.info("Closing connection with MongoDB.")
        self.client.close()
        logging.info("Closed connection with MongoDB.")

    async def get_entry(self, entry_id: ObjectId) -> RevenueEntry:
        entry_q = await self.db.revenue.find_one({"_id": ObjectId(entry_id)})
        if entry_q:
            return RevenueEntry(**entry_q, id=entry_q["_id"])

    async def get_entries(self) -> List[RevenueEntry]:
        entries = []
        entries_q = self.db.revenue.find()
        print("Searching")
        async for entry in entries_q:
            entries.append(RevenueEntry(**entry, id=entry["_id"].to_decimal()))
        print(entries)
        return entries

    async def add_entry(self, entry: RevenueEntry):
        entry_dict = {
            k: v for k, v in entry.dict(exclude={"id"}).items() if v is not None
        }
        await self.db.revenue.insert_one(entry_dict)

    async def add_entries(self, entries: List[RevenueEntry]):
        entries_dict = []
        for entry in entries:
            entries_dict.append(
                {k: v for k, v in entry.dict(exclude={"id"}).items() if v is not None}
            )
        await self.db.revenue.insert_many(entries_dict)
