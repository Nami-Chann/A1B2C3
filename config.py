#(©)Codeflix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler

import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647
from database.database import get_variable

# Function to retrieve configuration values with a fallback to environment variables
def get_config_value(key: str, default: str):
    return get_variable(key, os.environ.get(key, default))



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6555647930:AAG9KUdVDLLJODKEZHgNbTDqp3ZQ19vUKZg")
START_IMG = get_config_value("START_IMG", "https://envs.sh/_wI.jpg")
FSUB_IMG = get_config_value("FSUB_IMG", "https://envs.sh/_wB.jpg")
AUTO_DELETE = bool(get_config_value("AUTO_DELETE", "True"))
DELETE_TIME = int(get_config_value("DELETE_TIME", "43200"))
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28713982"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "237e15f7c006b10b4fa7c46fee7a5377")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002030889174"))

#OWNER ID
OWNER = int(os.environ.get("OWNER_ID", "7195990500"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 

#force sub channel id, if you want enable force sub


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>ʟᴏᴠᴇ ᴀɴɪᴍᴇ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀᴛᴄʜ ᴡʜᴀᴛ ʏᴏᴜ'ʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote>\n\nᴄʜᴇᴄᴋ ᴏᴜᴛ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ʙᴇʟᴏᴡ ꜰᴏʀ ᴍᴏʀᴇ!👇.</b>")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʏ {first} ʏᴏᴜ'ʀᴇ ᴍɪssɪɴɢ ᴏᴜᴛ ᴏɴ sᴏᴍᴇ sᴇʀɪᴏᴜs ᴀᴄᴛɪᴏɴ.ᴛo ᴜɴʟᴏᴄᴋ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ᴀᴄᴄᴇss ғɪʟᴇs, ᴊᴏɪɴ ᴀʟʟ of ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʙᴇʟᴏᴡ: !")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @Anime_Madness</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @LUFFY1JOYBOY"



LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
