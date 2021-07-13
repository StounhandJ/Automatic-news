from data.Article import Article
from Logger import Logger
from parsers.StopGameParser import StopGameParser
from storage import MongodbService
import time
import asyncio
import logging
storage = MongodbService.get_instance()
logger = Logger()
stopGameParser = StopGameParser()


def saveArticles(articles):
    """
    :param data: [Article]
    :return:
    """
    for article in articles:
        storage.save_data(article.toArray())


async def main():
    while True:
        stopGameArticles = await stopGameParser.parse()
        DtfArticles = []

        articles = stopGameArticles + DtfArticles
        saveArticles(articles)

        logger.log("{} articles added".format(len(articles)))
        time.sleep(60 * 10)

    # for data in storage.get_data(): Вывод всех статей
    #     print(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    # storage.delete_all_data() # удаление всего из базы
