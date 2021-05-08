from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from odmantic import AIOEngine
from reguleque_api.config import get_config
from reguleque_api.db.models import RevenueEntry

config = get_config()
db_path = config.db_path
db_name = config.db_name

client = AsyncIOMotorClient(db_path)
engine = AIOEngine(motor_client=client, database=db_name)
rev_collection: AsyncIOMotorCollection = engine.get_collection(RevenueEntry)
