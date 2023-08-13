from AnonX.core.bot import AnonXBot
from AnonX.core.dir import dirr
from AnonX.core.git import git
from AnonX.core.userbot import Userbot
from AnonX.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = AnonXBot()

userbot = Userbot()


### Assistant Info
ASSID = 0
ASSNAME = ""
ASSUSERNAME = ""
ASSMENTION = ""


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()


def init_db():
    global db_mem
    db_mem = {}


init_db()
