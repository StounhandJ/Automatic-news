from abc import abstractmethod

import requests
from bs4 import BeautifulSoup

from storage import MongodbService

from data.ArticleFactory import ArticleFactory

from data.Article import Article
from Logger import logger


class ParserAbstract:
    __className = ""

    def __init__(self):
        self.__className = self.__module__.split(".")[-1]

    def _getLastSrc(self) -> str:
        class_name = self.__module__.split(".")[-1]
        return self._getLastArticle(class_name).src

    def _getLastArticle(self, class_name) -> Article:
        storage = MongodbService.get_instance()
        return ArticleFactory.create(storage.getLastArticleParser(class_name))

    def _createSoupFromUrl(self, url: str, params={}, cookies={}) -> BeautifulSoup:
        page = requests.get(url, params=params, cookies=cookies)
        return self._createSoup(page.text)

    def _createSoup(self, text: str) -> BeautifulSoup:
        return BeautifulSoup(text, "html.parser")

    def _createDictFromJson(self, url: str, params={}) -> dict:
        page = requests.get(url, params=params)
        return page.json()

    def _getClassName(self):
        return self.__className

    @abstractmethod
    async def parse(self):
        """
        :return: Article[]
        """


def parseErrorHandling(func):
    async def wrapper(self):
        try:
            return await func(self)
        except AttributeError as e:
            logger.error("Parser Error: {}".format(self._ParserAbstract__className))
            return []
        except Exception as e:
            logger.error("Unknown error: {}".format(e))
            return []

    return wrapper
