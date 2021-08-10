from environs import Env

env = Env(eager=False)
env.read_env()

release = env.bool("DOCKER")
CHANNEL_ID = env.str("CHANNEL_ID")
TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN")
