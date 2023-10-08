from . import *
from utils.file_manager import load_json
from utils.input_manager import int_input, playlist_choice_parser, check_yesno

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
  
    i=0
    for track in tracks_raw:
        sp_track=spotify.track(track["track"]["id"])
        artist=spotify.artist(sp_track["artists"][0]["id"])
        tracks[track["track"]["id"]]=artist["genres"]
        print(f'\rLoading{"."*((i%3)+1)}{" "*(3-(i%3)+1)}', end='')
        i+=1
    return tracks

def pre_sort(spotify, playlist_id):
    playlist_tracks=spotify.playlist_tracks(playlist_id, limit=LIMIT_PLAYLIST_TRACK)
    tracks_details=collect_tracks(spotify, playlist_tracks)
    print(f"\r{len(tracks_details.keys())} elements collected.\n")
    return tracks_details

def playlist_exists(playlist, genre):
    if not genre in playlist.keys():
        return False
    else:
        return True

def order_playlists_by_songs(playlists):
    ordered_playlist={}
    ordered_generes=sorted(playlists, key=lambda playlist: len(playlists[playlist]), reverse=True)
    for genre in ordered_generes:
        ordered_playlist[genre]=playlists[genre]
    return ordered_playlist
    
def playlist_sorting(tracks):
    new_playlists={}
    for id in tracks.keys():
        track_genres=tracks[id]
        for genre in track_genres:
            if not playlist_exists(new_playlists, genre):
                new_playlists[genre]=[]
            for default_genre in DEFAULT_GENRES:
                if default_genre in genre:
                    if not playlist_exists(new_playlists, default_genre):
                        new_playlists[default_genre]=[]
                    if id not in new_playlists[default_genre]:
                        new_playlists[default_genre].append(id)
            if id not in new_playlists[genre]:
                new_playlists[genre].append(id)
    new_playlists=order_playlists_by_songs(new_playlists)
    return new_playlists

def prompt_for_playlists(max_value):
    return playlist_choice_parser(max_value)

def gensort_playlists(chosen, playlists, user_playlists, spotify):
    confirm=check_yesno(input("Confirm? (Y/N)\t"))
    current_user = spotify.current_user()
    username = current_user['uri'].split(":")[2]
    if not confirm:
        exit("SEE YOU NEXT TIME!\n")
    for i in chosen:
        sorted_playlists_name=list(playlists.keys())[i]
        final_playlist_name=f"{PLAYLISTS_PREFIX}{sorted_playlists_name}"
        if final_playlist_name in list(user_playlists.keys()):
            final_playlist_id=user_playlists[final_playlist_name]
            spotify.playlist_add_items(final_playlist_id, playlists[sorted_playlists_name])
        else:
            new_playlist_id=spotify.user_playlist_create(username, final_playlist_name, public=False, collaborative=False, description=PLAYLISTS_DESCRIPTION)["id"]
            spotify.playlist_add_items(new_playlist_id, playlists[sorted_playlists_name])
        print(f"{len(playlists[sorted_playlists_name])} songs have been added to {final_playlist_name}")