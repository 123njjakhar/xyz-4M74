import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCYTaDTycYqyDmgoyyNjmDPJpaUCF2k-l0dve4JBRhCk1_yzxd9rsqcyoo56i4jVgCJP--Xbg0tjGiFZpSUi0uteGYoWqwtbFXE6FHWM0UulN0tFatAi7JQN7w7B_1_SUVgLVOn-C2F2XOEYXVU_9BqAywKZK52sk6429i_J3YXMxwqXJeyOZ5KoxD4sqLxg2YWr5N9A9OqwDNAuhxlJH22wykfXlrKxp4E5w-RSVpGesB7WOZ93_rwhj2y1FbA42VS7bpm9q5QVHe_kZVyoHlJ4lYfebOiBXGY-cnKJQtFqgGBm4-WJsoqMxIKdFxd2Fiusm2UHRTpJ8onZe65VIuBAAAAATtI1AoA")
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
