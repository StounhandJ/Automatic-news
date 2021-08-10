from environs import Env

env = Env(eager=False)
env.read_env()

release = env.bool("DOCKER")
mongodbHost = env.str("MONGO_HOST")
dataBase = env.str("MONGO_DATABASE")
collection = env.str("MONGO_COLLECTION")
telegramHost = env.str("TELEGRAM_HOST")
