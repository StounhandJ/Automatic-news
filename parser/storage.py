from pymongo import MongoClient
from data.config import mongodbHost, dataBase, collection
from Logger import logger


def connectionErrorHandling(func):
    def wrapper(self, data=None):
        try:
            func(self, data)
        except Exception:
            logger.error("Error connect DB")
            return []
    return wrapper


class MongodbService(object):
    _instance = None
    _client = None
    _db = None
    _articlesСollection = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.__init__(cls._instance, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._client = MongoClient(mongodbHost, 27017)
        self._db = self._client.get_database(dataBase)
        self._articlesСollection = self._db.get_collection(collection)

    @connectionErrorHandling
    def get_data(self):
        return list(self._articlesСollection.find())

    @connectionErrorHandling
    def getLastArticleParser(self, parser):
        return self._articlesСollection.find_one({"parser": parser})

    @connectionErrorHandling
    def save_data(self, dto):
        return self._articlesСollection.insert_one(dto)

    @connectionErrorHandling
    def delete_all_data(self):
        self._articlesСollection.drop()
