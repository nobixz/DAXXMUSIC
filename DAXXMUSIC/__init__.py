from NOBITAMUSIC.core.bot import NOBIT
from NOBITAMUSIC.core.dir import dirr
from NOBITAMUSIC.core.git import git
from NOBITAMUSIC.core.userbot import Userbot
from NOBITAMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = NOBITA()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
