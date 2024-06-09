from SafoneAPI import SafoneAPI

from zein.core.bot import VIP
from zein.core.dir import dirr
from zein.core.git import git
from zein.core.userbot import Userbot
from zein.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = VIP()
api = SafoneAPI()
userbot = Userbot()
HELPABLE = {}

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
APP = "tg_vc_bot"  # connect music api key "Dont change it"
