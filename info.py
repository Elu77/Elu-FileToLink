import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '26726938'))
API_HASH = environ.get('API_HASH', 'da0fca2d5ed2da029835a2f2cdf3a411')
BOT_TOKEN = environ.get('BOT_TOKEN', "7538301821:AAFWX_ChYI_-QHFiOIsJlWmkUIaVsVlrDvY")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1007538301821'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7831382420').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://codali6429:codali6429@cluster0.gmgqq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "techvjautobot")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', True)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'modijiurl.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '35840a51e5e3ed3e1c8cbe4fb194c7b9db18c3c8')
