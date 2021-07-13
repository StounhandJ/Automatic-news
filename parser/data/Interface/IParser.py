from abc import abstractmethod

from storage import MongodbService

from data.ArticleFactory import ArticleFactory

from data.Article import Article


class IParser:

    def getLastTitle(self) -> str:
        class_name = self.__module__.split(".")[-1]
        return self._getLastArticle(class_name).title

    def _getLastArticle(self, class_name) -> Article:
        storage = MongodbService.get_instance()
        return ArticleFactory.create(storage.getLastArticleParser(class_name))

    @abstractmethod
    async def parse(self):
        """
        :return: Article[]
        """
