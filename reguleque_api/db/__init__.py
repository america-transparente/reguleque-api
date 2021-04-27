from reguleque_api.db.database_manager import DatabaseManager
from reguleque_api.db.mongo_manager import MongoManager

db = MongoManager()


async def get_database() -> DatabaseManager:
    return db
