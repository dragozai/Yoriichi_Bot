import json
import os


def get_user_list(config, key):
    with open("{}/Yoriichi/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = 4645306
    API_HASH = "23084ea16ef78eaa349a1e7edb597188"
    TOKEN = "5048663657:AAEY4OSqiPYKQedL6WGcc3-ol2WJEEunVEI" 
    OWNER_ID = "5069705982"
    OWNER_USERNAME = "Ryuuzai"
    BOT_USERNAME = "Yorichi_Bot"
    BOT_ID = "5048663657"
  # SUPPORT_CHAT = "TanjirouXSupport"
    DATABASE_URL = "postgresql://postgres:mnvmwbYAH79GYh6RA0dS@containers-us-west-31.railway.app:5607/railway"  # needed for any database modules
    LOAD = []
    NO_LOAD = "rss"
    WEBHOOK = False
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False
    WORKERS = (
        8
    )
    BAN_STICKER = ""
    ALLOW_EXCL = True 
    ALLOW_CHATS = True
    MONGO_DB_URI = "mongodb+srv://Tanjirou:Tanji_67@cluster0.gsfly.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    WALL_API = (
        "6950f559377140a4e1594c564cdca6a3"  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    REM_BG_API_KEY = "wZsgx3gpTYtgCRj5JHpB9bYY" 
    TEMP_DOWNLOAD_DIRECTORY = "/tmp"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
