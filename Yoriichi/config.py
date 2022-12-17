import json
import os


def get_user_list(config, key):
    with open("{}/Yoriichi/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    API_ID = "4645306" # integer value, dont use ""
    API_HASH = "23084ea16ef78eaa349a1e7edb597188"
    TOKEN = "5048663657:AAEY4OSqiPYKQedL6WGcc3-ol2WJEEunVEI"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly. 
    OWNER_ID = "5069705982"  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Ryuuzai"
    BOT_USERNAME = "Yorichi_Bot"
    BOT_ID = "5048663657"
  #  SUPPORT_CHAT = "TanjirouXSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        "-643271666"
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        "-1001680637786"
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    DATABASE_URL = "postgresql://postgres:mnvmwbYAH79GYh6RA0dS@containers-us-west-31.railway.app:5607/railway"  # needed for any database modules
    LOAD = []
    NO_LOAD = "rss"
    WEBHOOK = False
    INFOPIC = True
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    THUNDERS = get_user_list("elevated_users.json", "thunders")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    FLAMES = get_user_list("elevated_users.json", "flames")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WINDS = get_user_list("elevated_users.json", "winds")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WATERS = get_user_list("elevated_users.json", "waters")
    BEASTS = get_user_list("elevated_users.json", "beasts")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ALLOW_CHATS = True
 #   CASH_API_KEY = (
 #       "T4291FWANEE3R2PS"  # Get your API key from https://www.alphavantage.co/support/#api-key
#    )
   # TIME_API_KEY = "YY22O503GXDH"  # Get your API key from https://timezonedb.com/api
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
