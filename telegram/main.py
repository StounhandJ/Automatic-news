import asyncio
import json

from data.Article import Article
from data.ArticleFactory import ArticleFactory
from data.config import CHANNEL_ID, TELEGRAM_TOKEN

from aiogram import Bot, types

from flask import Flask, request

app = Flask(__name__)
bot = Bot(token=TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)


async def send_message(channel_id: int, text: str, photo=""):
    if photo:
        await bot.send_photo(channel_id, caption=text, photo=photo)
    else:
        await bot.send_message(channel_id, text)


def create_message(article: Article):
    return "<a href='{src}'>{title}</a>".format(src=article.src, title=article.title)


async def main_send_telegram(articles: [Article]):
    for article in articles:
        await send_message(CHANNEL_ID, create_message(article), article.img_src)


@app.route('/', methods=['GET'])
def index():
    articles = []
    for articleJSON in json.loads(request.get_data()):
        articles.append(ArticleFactory.create(articleJSON))
    asyncio.run(main_send_telegram(articles))
    return "Good"


if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0')

# if __name__ == '__main__':
#     asyncio.run(main())
