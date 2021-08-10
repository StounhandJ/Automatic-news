import asyncio
import json
from flask import Flask, request

from data.ArticleFactory import ArticleFactory

from telegram import main_send_message

app = Flask(__name__)
loop = asyncio.get_event_loop()


@app.route('/', methods=['POST'])
def index():
    articles = []
    for articleJSON in json.loads(request.get_data()):
        articles.append(ArticleFactory.create(articleJSON))
    asyncio.run(main_send_message(articles))
    return ""


if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0')
