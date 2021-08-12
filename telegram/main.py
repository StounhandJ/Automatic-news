import asyncio
import json
from flask import Flask, request
from redis import Redis
from rq import Queue

from data.ArticleFactory import ArticleFactory
from telegram import main_send_message
from data.config import REDIS_HOST, release

q = Queue(connection=Redis(host=REDIS_HOST))

app = Flask(__name__)
loop = asyncio.get_event_loop()


@app.route('/', methods=['POST'])
def index():
    for articleJSON in json.loads(request.get_data()):
        q.enqueue(main_send_message, ArticleFactory.create(articleJSON))
    return ""


if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0', debug=not release)
