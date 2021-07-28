import bs4
from data.Abstract.ParserAbstract import ParserAbstract
from data.Article import Article
from bs4 import BeautifulSoup
import requests

from data.ArticleFactory import ArticleFactory


class PlayGroundParser(ParserAbstract):
    _url = "https://www.playground.ru/news"
    _lastTitle = ""
    _className = ""

    def __init__(self):
        self._lastTitle = super().getLastTitle()
        self._className = self.__module__.split(".")[-1]

    async def parse(self) -> [Article]:
        articles = []
        if self._lastTitle == "":
            articles = self._parsePage(1)
        else:
            page = 0
            while self._isGetLastArticle(articles, page):
                page += 1
                articles += self._parsePage(page)
        self._setLastArticle(articles[0]) if len(articles) > 0 else 0
        return articles

    def _isGetLastArticle(self, articles, page) -> bool:
        return len(articles) == page * 30

    def _parsePage(self, page: int) -> [Article]:
        articles = []
        soup = self._createSoupFromUrl(self._url, {"p": page})
        allArticlesHTML = soup.findAll('div', class_='post')
        for articleHTML in allArticlesHTML:
            article = self._articleHtmlToArticle(articleHTML)
            if self._isLastArticle(article):
                break
            articles.append(article)
        return articles

    def _isLastArticle(self, article) -> bool:
        """
        :param article: Article
        :return: bool
        """
        return self._lastTitle == article.title

    def _articleHtmlToArticle(self, articleHTML: bs4.Tag) -> Article:
        """
        Парсинг отдельного поста
        :param articleHTML:
        :return: Article
        """
        title = articleHTML.findAll(class_="post-title")[0].text.strip()
        src = articleHTML.findAll(class_="post-title")[0].findAll("a")[0]["href"]
        text = ""  # self._parseContentArticle(src)
        img_src = articleHTML.findAll("img")[0]["src"]
        return ArticleFactory.create({
            "title": title,
            "src": src,
            "text": text,
            "img_src": img_src,
            "parser": self._className
        })

    def _parseContentArticle(self, src_post: str) -> str:
        soup = self._createSoupFromUrl(src_post)
        return soup.findAll(class_="article-content js-post-item-content")[0].text.strip()

    def _setLastArticle(self, article: Article):
        self._lastTitle = article.title
