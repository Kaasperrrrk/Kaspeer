import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6893876630:AAFrHDirQd6PoYjG8Xzm7uDjtBh-zDVO6UA")

    APP_ID = int(os.environ.get("APP_ID", 19057678))

    API_HASH = os.environ.get("API_HASH", "4b03c0ec8408f3c29c41c88188a38446")
