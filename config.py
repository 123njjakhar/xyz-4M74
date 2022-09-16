import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBDBWGfjPaLENJCnG-47c360Z7vWdgm5xushOLm7aPpzxSohRmxINbLBq7DodPAJem8bg2QdSI-IoDqY0F7nIkPdE2MnKU0EGI0-rDs6CI1RBVuK9s3hMpZVSZdgJ5gPn7diNhfK3ABDWjSs5GJtmhRIfe-jW3XLn0MIjQ1UWgLB3HG825qzm37p4wtKhxATdjz_vpVg6kolrzGvecFpdQKH2Ru8lMjXXYkfUC20VTYpBR4WjYHDAB9WQbzB9FfeUGXK9F5zg0-AxjSYzcW-coUxhIypYdeCVRmDrF8YJfRGDbczIFNMb29dZ03G04h9rffptdtx9zhDsndujKtuVYXAAAAATtI1AoA")
BOT_TOKEN = getenv("BOT_TOKEN", "5468931327:AAHohcUuNDpEAiOMZ8WPg581PqGy2jwlRsA")
BOT_NAME = getenv("BOT_NAME", "Romeo_RJ_music_1bot")
API_ID = int(getenv("API_ID", "13917726"))
API_HASH = getenv("API_HASH", "f19ec06116df6531489db0d6daebbc03")
OWNER_NAME = getenv("OWNER_NAME", "5289595914")
OWNER_USERNAME = getenv("OWNER_USERNAME", "5289595914")
ALIVE_NAME = getenv("ALIVE_NAME", "5289595914")
BOT_USERNAME = getenv("BOT_USERNAME", "Romeo_RJ_music_1bot")
OWNER_ID = getenv("OWNER_ID", "5289595914")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "5289595914")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ROMEOBOT_OP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ROMEO_OP")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5289595914").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fe9833deebd3ae950f4c9.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fe9833deebd3ae950f4c9.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "54000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Romeo-RJ/Romeo-musicBot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/fe9833deebd3ae950f4c9.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/fe9833deebd3ae950f4c9.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/fe9833deebd3ae950f4c9.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/fe9833deebd3ae950f4c9.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/fe9833deebd3ae950f4c9.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/fe9833deebd3ae950f4c9.jpg")
