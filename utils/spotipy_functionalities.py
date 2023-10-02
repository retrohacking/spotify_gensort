from . import *

def get_spotify(user_token, client_manager):
    return spotipy.Spotify(auth=user_token)