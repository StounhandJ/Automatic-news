from abc import abstractmethod

import requests
from bs4 import BeautifulSoup

from storage import MongodbService

from data.ArticleFactory import ArticleFactory

from data.Article import Article


class ParserAbstract:

    def getLastTitle(self) -> str:
        class_name = self.__module__.split(".")[-1]
        return self._getLastArticle(class_name).title

    def _getLastArticle(self, class_name) -> Article:
        storage = MongodbService.get_instance()
        return ArticleFactory.create(storage.getLastArticleParser(class_name))

    def _createSoupFromUrl(self, url: str, params={}) -> BeautifulSoup:
        page = requests.get(url, params=params)
        return self._createSoup(page.text)

    def _createSoup(self, text: str) -> BeautifulSoup:
        return BeautifulSoup(text, "html.parser")

    def _createDictFromJson(self, url: str, params={}) -> dict:
        page = requests.get(url, params=params)
        return page.json()

    @abstractmethod
    async def parse(self):
        """
        :return: Article[]
        """
