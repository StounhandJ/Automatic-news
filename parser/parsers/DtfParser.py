# https://dtf.ru/games/more?last_id=809038
import requests
from bs4 import BeautifulSoup, Tag

from data.Article import Article
from data.ArticleFactory import ArticleFactory
from data.Abstract.ParserAbstract import ParserAbstract


class DTFParser(ParserAbstract):
    _urlOrigin = "https://dtf.ru/games/entries/new?mode=ajax"
    _urlMore = "https://dtf.ru/games/entries/new/more"
    _lastID = 0

    async def parse(self) -> [Article]:
        articles = []

        html = self._createDictFromJson(self._urlOrigin)["module.ajaxify"]["html"]
        pageBS = self._createSoup(html)

        feedValue = self._getFeedLastSortingValue(pageBS)
        lastID = self._getLastID(pageBS)

        page = 0
        while self._isGetLastArticle(articles, page):
            if page != 0:
                pageBS = self._getPage(lastID, feedValue)
                lastID, feedValue = self._getLastIdAndLastSortingValue(lastID, feedValue)
            articles += self._parseData(pageBS)
            page += 1
            if self._getLastTitle() == "":
                break

        return articles

    def _getLastID(self, pageBS: BeautifulSoup) -> int:
        """
        Получить id последнего поста
        :return:
        """
        return int(pageBS.findAll("div", class_="feed")[0]["data-feed-last-id"])

    def _getFeedLastSortingValue(self, pageBS: BeautifulSoup) -> float:
        """
        Получить значения поиска, специальный обязательные параметр
        :return:
        """
        return float(pageBS.findAll("div", class_="feed")[0]["data-feed-last-sorting-value"].replace(",", "."))

    def _getPage(self, lastID: int, feedValue: float) -> BeautifulSoup:
        """
            Получить страницу после поста с lastID. Обращаясь к скрытой api сайта
            :param lastID: ID поста после которого искать
            :param feedValue: Специальный обязательные параметр
            :return:
        """
        return self._createSoup(self._createDictFromJson(self._urlMore, {
            "last_id": lastID, "last_sorting_value": feedValue
        })["data"]["items_html"])

    def _getLastIdAndLastSortingValue(self, lastID: int, feedValue: float):
        data = self._createDictFromJson(self._urlMore, {
            "last_id": lastID, "last_sorting_value": feedValue
        })["data"]
        return data["last_id"], data["last_sorting_value"]

    def _parseData(self, pageBS: BeautifulSoup) -> [Article]:
        """
        Получить все посты поста с страницы.
        :param pageBS: Страница с статьями
        :return:
        """
        articles = []

        for articleHTML in pageBS.findAll(class_="feed__item l-island-round"):
            article = self._articleHtmlToArticle(
                articleHTML)  # Получение поста и установка id последнего проверенного поста
            if self._isLastArticle(article):
                break
            articles.append(article)

        return articles

    def _articleHtmlToArticle(self, articleHTML: Tag) -> Article:
        """
        Парсинг отдельного поста.
        :param articleHTML:
        :return: Article и его ID
        """
        title = articleHTML.findAll(class_="content-title")[0].text.strip()
        src = articleHTML.findAll(class_="content-feed__link")[0]["href"]
        text = ""  # self._parseContentArticle(src)

        imgDivs = articleHTML.findAll(class_="andropov_image")
        videoDivs = articleHTML.findAll(class_="andropov_video")
        img_src = ""
        if len(imgDivs) > 0:
            img_src = imgDivs[0]["data-image-src"]
        elif len(videoDivs) > 0:
            img_src = videoDivs[0]["data-video-thumbnail"]

        id = articleHTML.findAll(class_="content-feed")[0]["data-content-id"]
        return ArticleFactory.create({
            "title": title,
            "src": src,
            "text": text,
            "img_src": img_src,
            "parser": self._getClassName()
        })

    def _isLastArticle(self, article) -> bool:
        """
        :param article: Article
        :return: bool
        """
        return self._getLastTitle() == article.title

    def _isGetLastArticle(self, articles, page) -> bool:
        return len(articles) == page * 12
