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

def collect_tracks(spotify,playlist):
    tracks_raw = playlist['items']
    tracks={}

    while playlist['next']:
        playlist = spotify.next(playlist)
        tracks_raw.extend(playlist['items'])

    # FOR DEBUG PURPOSE    
    for track in tracks_raw:
        tracks[track["track"]["id"]]=track["track"]["artists"][0]["name"]
        print(f'{i} - {track["track"]["id"]} : {track["track"]["artists"][0]["name"]}')
        i+=1
    # END
    #IN REALITY WE WILL NEED THE ID OF THE SONG and its (first) genre - https://community.spotify.com/t5/Spotify-for-Developers/retrieving-genre-of-track-in-metadata/td-p/5495626

    return tracks

def pre_sort(spotify, playlist_name, playlist_id):
    playlist_tracks=spotify.playlist_tracks(playlist_id, limit=LIMIT_PLAYLIST_TRACK)
    tracks_details=collect_tracks(spotify, playlist_tracks)
    print(f"\n{len(tracks_details.keys())} elements collected.\n")


