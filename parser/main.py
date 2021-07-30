from Logger import logger
from data.config import release
from parsers.DtfParser import DTFParser
from parsers.PlayGroundParser import PlayGroundParser
from storage import MongodbService
import time
import asyncio

storage = MongodbService.get_instance()
if not release:
    storage.delete_all_data()

playGroundParser = PlayGroundParser()

dtfParser = DTFParser()


def saveArticles(articles):
    """
    :param articles: [Article]
    :return:
    """
    for article in articles:
        storage.save_data(article.toArray())


async def main():
    while True:
        stopGameArticles = await playGroundParser.parse()
        DtfArticles = await dtfParser.parse()

        articles = stopGameArticles + DtfArticles
        saveArticles(articles[::-1])

        logger.log("{} articles added".format(len(articles)))
        time.sleep(60 * 10)

    # for data in storage.get_data(): Вывод всех статей
    #     print(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    # storage.delete_all_data() # удаление всего из базы
