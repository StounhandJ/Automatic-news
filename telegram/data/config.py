from environs import Env

env = Env(eager=False)
env.read_env()

release = env.bool("DOCKER")
CHANNEL_ID = env.str("CHANNEL_ID")
TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN")
REDIS_HOST = env.str("REDIS_HOST")
POST_ARTICLE_EVERY_SECONDS = env.int("POST_ARTICLE_EVERY_SECONDS")
