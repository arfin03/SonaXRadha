from RadhaMusic.core.bot import Krish
from RadhaMusic.core.dir import dirr
from RadhaMusic.core.git import git
from RadhaMusic.core.userbot import Userbot
from RadhaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Krish()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
YTB = YTM()
