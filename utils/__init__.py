import spotipy
from time import localtime, sleep
REDIRECT="http://localhost:1337"
SCOPE="playlist-modify-private playlist-modify-public playlist-read-private playlist-read-collaborative"
TOKENS_FILE="tokens.json"

AUTHOR="Retro"
VERSION=1.0
YEAR=localtime()[0]
GITHUB="https://github.com/retrohacking"

RATE_LIMIT=100
LIMIT_PLAYLIST_TRACK=100
DEFAULT_GENRES=["rock", "metal", "funk", "punk", "trap", "hip hop", "rap", "pop", "r&b", "reggae", "soul"]
PLAYLISTS_PREFIX="GENSORT_"
PLAYLISTS_DESCRIPTION="A playlist automatically generated by Gensort :D"