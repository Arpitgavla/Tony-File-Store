# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz


import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz
      
# Owner Information
API_ID = int(environ.get("API_ID", "29236719"))
API_HASH = environ.get("API_HASH", "1ccf1bd0a86af974e3210a55f662c062")
ADMINS = int(environ.get("ADMINS", "893383574"))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "clonetonystark")
DB_URI = environ.get("DB_URI", "mongodb+srv://keshavptdr98:D8lbdQUW4euV07l4@cluster0.dok926y.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "tonystarkbotz")

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz

# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "7450654387:AAGuBPZxTv3CFABjVnoi_wlzAkL6RhwJLbs")
BOT_USERNAME = environ.get("BOT_USERNAME", "") # your bot username without @
PICS = (environ.get('PICS', 'https://graph.org/file/82ef767ffebe3a948e476.jpg https://graph.org/file/82ef767ffebe3a948e476.jpg')).split() # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002168613049"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz

# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filetolinkvjbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', ''))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = ""
    else:
        URL = ""



# Don't Remove Credit Tg - @TonyStark_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@TonyStarkBotz
# Ask Doubt on telegram @TonyStarkBotzXBotz
    
