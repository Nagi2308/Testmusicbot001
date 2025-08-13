import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = (getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Database to save your chats and stats... Get MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# You'll need a Private Group ID for this.
LOGGER_ID = (getenv("LOGGER_ID", None))

# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Testmusicbot001")

# Your User ID.
OWNER_ID = list(map(int, getenv("OWNER_ID", "6840435225").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6840435225").split()))

# Fill your group and channel username (without @)
GROUP_USERNAME = getenv("GROUP_USERNAME")
CHANNEL_USERNAME = getenv("CHANNEL_USERNAME")

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Enter your Heroku App name.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

# Repository
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Nagi2308/Knightsxbots/blob/main/README.md")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# GIT TOKEN (if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Only Links formats are accepted for this Var value.
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/KnightsXbots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Knightxbotsupport")  # ✅ FIXED

# Custom max audio duration for voice chat (in minutes)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "5000"))

# Download duration limits
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1000"))

# Auto-leave options
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))

# Downloads clean-up
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

# Private bot mode
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Sleep duration for edits
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

# Spotify credentials
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Video stream limit
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "300"))

# Playlist limits
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

# Cleanmode delete time
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "60"))

# File size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

# String sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Do not edit below this line
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/ff3d94744211c796cf5bb.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/07b109ac650e5f4fec9e5.jpg")

PLAYLIST_IMG_URL = "https://files.catbox.moe/vvvlte.jpg"
GLOBAL_IMG_URL = "https://files.catbox.moe/vvvlte.jpg"
STATS_IMG_URL = "https://files.catbox.moe/vvvlte.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/g1x308.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/g1x308.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/g1x308.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/g1x308.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/g1x308.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/g1x308.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/g1x308.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/g1x308.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL validation
if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):  # ✅ FIXED
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
