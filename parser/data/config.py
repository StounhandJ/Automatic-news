from environs import Env

env = Env()
env.read_env()
mongodbHost = env.str("MONGO_HOST")
dataBase = env.str("MONGO_DATABASE")
collection = env.str("MONGO_COLLECTION")
# mongodbHost = "localhost"
