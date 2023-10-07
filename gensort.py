from utils.authorization_manager import have_tokens,configure_tokens, read_tokens, generate_user_token, get_client_manager
from utils.gensort_functionalities import get_spotify, get_playlists, choose_playlist, pre_sort, playlist_sorting
from utils.window_manager import print_banner, print_playlists_name, print_sorted_playlists

def retrieve_tokens():
    if not have_tokens():
        return configure_tokens()
    else:
        return read_tokens()
        
def authorization(client_tokens):
    return generate_user_token(client_tokens["username"], client_tokens["client_id"], client_tokens["client_secret"])

def load_gensort():
    client_tokens=retrieve_tokens()
    user_token=authorization(client_tokens)
    return get_client_manager(client_tokens), user_token
 
def run_gensort(client, token):
    print_banner()
    spotify=get_spotify(token, client)
    playlists=get_playlists(spotify)
    playlists_name=list(playlists.keys())
    print_playlists_name(playlists_name)
    target_playlist=choose_playlist(playlists_name)
    tracks_details=pre_sort(spotify, playlists[playlists_name[target_playlist]])  
    sorted_playlists=playlist_sorting(tracks_details)
    print_sorted_playlists(sorted_playlists)
    #get the choice of the playlists (parser) -> gensort_functionalities -> input_manager
    #create the playlists -> gensort_functionalities and get the IDs


    