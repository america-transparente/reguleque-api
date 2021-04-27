from abc import abstractmethod
from reguleque_api.db.models import RevenueEntry
from odmantic.bson import ObjectId
from typing import List


class DatabaseManager(object):
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(self, path: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass

    @abstractmethod
    async def get_entries(self) -> List[RevenueEntry]:
        pass

    @abstractmethod
    async def get_entry(self, post_id: ObjectId) -> RevenueEntry:
        pass

    @abstractmethod
    async def add_entries(self, entries: List[RevenueEntry]):
        pass

    @abstractmethod
    async def add_entry(self, entry: RevenueEntry):
        pass
