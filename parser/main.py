import json
import time
import asyncio
import requests
from requests.exceptions import ReadTimeout

from Logger import logger
from data.config import release, telegramHost
from parsers.DtfParser import DTFParser
from parsers.PlayGroundParser import PlayGroundParser
from storage import MongodbService

storage = MongodbService.get_instance()
if not release:
    storage.delete_all_data()

playGroundParser = PlayGroundParser()

dtfParser = DTFParser()


def saveArticles(articlesJSON):
    """
    :param articlesJSON: [Article]
    :return:
    """
    for article in articlesJSON:
        storage.save_data(article)


def sendToTelegram(articlesJSON):
    try:
        if len(articlesJSON) > 0:
            requests.post("http://" + telegramHost, data=json.dumps(articlesJSON), timeout=1)
    except ReadTimeout:
        pass


def articleToArticleJson(articles):
    articlesJSON = []
    for article in articles:
        articlesJSON.append(article.toArray())
    return articlesJSON


async def main():
    while True:
        stopGameArticles = await playGroundParser.parse()
        DtfArticles = await dtfParser.parse()

        articles = DtfArticles + stopGameArticles

        articlesJSON = articleToArticleJson(articles[::-1])

        sendToTelegram(articlesJSON)
        saveArticles(articlesJSON)

        logger.log("{} articles added".format(len(articlesJSON)))
        time.sleep(60 * 10)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    # storage.delete_all_data() # удаление всего из базы
