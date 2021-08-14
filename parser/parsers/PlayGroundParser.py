import bs4
from data.Abstract.ParserAbstract import ParserAbstract, parseErrorHandling
from data.Article import Article

from data.ArticleFactory import ArticleFactory


class PlayGroundParser(ParserAbstract):
    _url = "https://www.playground.ru/news"

    @parseErrorHandling
    async def parse(self) -> [Article]:
        articles = []
        if self._getLastSrc() == "":
            articles = self._parsePage(1)
        else:
            page = 0
            while self._isGetLastArticle(articles, page):
                page += 1
                articles += self._parsePage(page)
                # Если пост был изменен и поиск улетел в бесконечность
                if len(articles) > 30 * 3:
                    articles = [articles[0]]
                    break
        return articles

    def _isGetLastArticle(self, articles, page) -> bool:
        return len(articles) == page * 30

    def _parsePage(self, page: int) -> [Article]:
        articles = []
        soup = self._createSoupFromUrl(self._url, {"p": page}, {"pg_post_sorting": "%7B%22news%22%3A%22fixed getting last title |  PGParser getting article by creation_date%22%7D"})
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
        return self._getLastSrc() == article.src

    def _articleHtmlToArticle(self, articleHTML: bs4.Tag) -> Article:
        """
        Парсинг отдельного поста
        :param articleHTML:
        :return: Article
        """
        title = articleHTML.find(class_="post-title").text.strip()
        src = articleHTML.find(class_="post-title").find("a")["href"]
        text = ""  # self._parseContentArticle(src)
        img_src = articleHTML.find("img")["src"]
        return ArticleFactory.create({
            "title": title,
            "src": src,
            "text": text,
            "img_src": img_src,
            "parser": self._getClassName()
        })

    def _parseContentArticle(self, src_post: str) -> str:
        soup = self._createSoupFromUrl(src_post)
        return soup.findAll(class_="article-content js-post-item-content")[0].text.strip()
