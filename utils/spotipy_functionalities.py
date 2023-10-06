from . import *
from utils.input_manager import int_input

def get_spotify(user_token, client_manager):
    return spotipy.Spotify(auth=user_token)

def get_playlists(spotify):
    playlists={}
    playlists_meta=spotify.current_user_playlists()
    for playlist in playlists_meta["items"]:
       playlists[playlist['name']]=playlist['id']
    return playlists

def choose_playlist(playlists):
    return int_input("Choose the playlist to sort out\n> ", len(playlists))

def pre_sort(spotify, playlist_name, playlist_id):
    playlist_tracks=spotify.playlist_tracks(playlist_id, limit=LIMIT_PLAYLIST_TRACK)
    for track in playlist_tracks["items"]:
        print(f'{track["track"]["name"]}')
