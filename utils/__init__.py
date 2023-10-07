import spotipy
from time import localtime
REDIRECT="http://localhost:1337"
SCOPE="playlist-modify-private playlist-modify-public playlist-read-private playlist-read-collaborative"
TOKENS_FILE="tokens.json"

AUTHOR="Retro"
VERSION=1.0
YEAR=localtime()[0]
GITHUB="https://github.com/retrohacking"

LIMIT_PLAYLIST_TRACK=100
DEFAULT_GENRES=["rock", "metal", "funk", "punk", "trap", "hip hop", "rap", "pop", "r&b", "reggae", "soul"]