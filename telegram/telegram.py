import asyncio
from aiogram import Bot, types
from aiogram.utils.exceptions import RetryAfter

from data.Article import Article
from data.config import CHANNEL_ID, TELEGRAM_TOKEN


bot = Bot(token=TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)


def reconnect_telegram():
    global bot
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


async def send_photo(channel_id: int, text: str, photo_src: str):
    try:
        await bot.send_photo(channel_id, caption=text, photo=photo_src)
    except:
        await send_message(channel_id, text)


def create_message_text(article: Article):
    return '<a href="{src}">{title}</a>'.format(src=article.src, title=article.title)


async def main_send_message(articles: [Article]):
    reconnect_telegram()
    for article in articles:
        try:
            text = create_message_text(article)
            if article.img_src:
                await send_photo(CHANNEL_ID, text, article.img_src)
            else:
                await send_message(CHANNEL_ID, text)
        except RetryAfter as e:
            await asyncio.sleep(e.timeout)
        # await asyncio.sleep(2)
