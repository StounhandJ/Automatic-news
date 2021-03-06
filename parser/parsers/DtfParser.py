from bs4 import BeautifulSoup, Tag
import re

from data.Article import Article
from data.ArticleFactory import ArticleFactory
from data.Abstract.ParserAbstract import ParserAbstract, parseErrorHandling


class DTFParser(ParserAbstract):
    _urlOrigin = "https://dtf.ru/games/entries/new?mode=ajax"
    _urlMore = "https://dtf.ru/games/entries/new/more"
    _lastID = 0

    @parseErrorHandling
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
            if self._getLastSrc() == "":
                break
            # Если пост был изменен и поиск улетел в бесконечность
            if len(articles) > 12 * 8:
                articles = [articles[0]]
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
                articleHTML)  # Получение поста
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
        title = articleHTML.find(class_="content-title") if articleHTML.find(class_="content-title") else articleHTML.find(class_="l-island-a")
        title = re.sub(r"\n\n\nСтатьи редакции", "", title.text.strip())

        src = articleHTML.find(class_="content-feed__link")["href"]
        text = ""  # self._parseContentArticle(src)

        imgDivs = articleHTML.find(class_="andropov_image")
        videoDivs = articleHTML.find(class_="andropov_video")
        img_src = ""
        if imgDivs:
            img_src = imgDivs["data-image-src"]
        elif videoDivs:
            img_src = videoDivs["data-video-thumbnail"]

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
        return self._getLastSrc() == article.src

    def _isGetLastArticle(self, articles, page) -> bool:
        return len(articles) == page * 12
