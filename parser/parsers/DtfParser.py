# https://dtf.ru/games/more?last_id=809038
import requests
from bs4 import BeautifulSoup, Tag

from data.Article import Article
from data.ArticleFactory import ArticleFactory
from data.Abstract.ParserAbstract import ParserAbstract


class DTFParser(ParserAbstract):
    _urlOrigin = "https://dtf.ru/games"
    _urlMore = "https://dtf.ru/games/more"
    _lastTitle = ""
    _className = ""
    _lastID = 0

    def __init__(self):
        self._lastTitle = super().getLastTitle()
        self._className = self.__module__.split(".")[-1]

    async def parse(self) -> [Article]:
        articles = []

        firstID = self._getFirstID()
        feedValue = self._getFeedLastSortingValue()

        page = 1
        articles += self._parseData(firstID, feedValue)

        while self._isGetLastArticle(articles, page) and self._lastTitle != "":
            articles += self._parseData(self._lastID, feedValue-page)
            page += 1

        self._setLastArticle(articles[0]) if len(articles) > 0 else 0
        return articles

    def _getFirstID(self) -> int:
        """
        Получить id самого первого поста
        :return:
        """
        soup = self._createSoupFromUrl(self._urlOrigin)
        firstArticle = soup.findAll(class_="feed__item l-island-round")[0]
        return firstArticle.findAll("div")[0]["data-content-id"]

    def _getFeedLastSortingValue(self) -> float:
        """
        Получить значения поиска, специальный обязательные параметр
        :return:
        """
        soup = self._createSoupFromUrl(self._urlOrigin)
        return float(soup.findAll("div", class_="feed")[0]["data-feed-last-sorting-value"].replace(",","."))

    def _parseData(self, lastID: int, feedValue: float) -> [Article]:
        """
        Получить все посты после поста с lastID. Обращаясь к скрытой api сайта
        :param lastID: ID поста после которого искать
        :param feedValue: Специальный обязательные параметр
        :return:
        """
        articles = []

        pageHTML = self._createSoup(self._createDictFromJson(self._urlMore, {
            "last_id": lastID, "last_sorting_value": feedValue
        })["data"]["items_html"])

        for articleHTML in pageHTML.findAll(class_="feed__item l-island-round"):
            article, self._lastID = self._articleHtmlToArticle(
                articleHTML)  # Получение поста и установка id последнего проверенного поста
            if self._isLastArticle(article):
                break
            articles.append(article)

        return articles

    def _articleHtmlToArticle(self, articleHTML: Tag) -> [Article, int]:
        """
        Парсинг отдельного поста.
        :param articleHTML:
        :return: Article и его ID
        """
        title = articleHTML.findAll(class_="content-title")[0].text.strip()
        src = articleHTML.findAll(class_="content-feed__link")[0]["href"]
        text = ""  # self._parseContentArticle(src)
        imgDivs = articleHTML.findAll(class_="andropov_image")
        if len(imgDivs) > 0:
            img_src = imgDivs[0]["data-image-src"]
        else:
            img_src = articleHTML.findAll(class_="andropov_video")[0]["data-video-thumbnail"]
        id = articleHTML.findAll(class_="content-feed")[0]["data-content-id"]
        return [ArticleFactory.create({
            "title": title,
            "src": src,
            "text": text,
            "img_src": img_src,
            "parser": self._className
        }), id]

    def _isLastArticle(self, article) -> bool:
        """
        :param article: Article
        :return: bool
        """
        return self._lastTitle == article.title

    def _isGetLastArticle(self, articles, page) -> bool:
        return len(articles) == page * 12

    def _setLastArticle(self, article: Article):
        self._lastTitle = article.title