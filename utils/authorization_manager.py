from . import *
from spotipy.oauth2 import SpotifyClientCredentials
from utils.file_manager import create_json, check_json, load_json
from utils.input_manager import check_yesno
from os import system
from webbrowser import open
import glob


LOGIN_PAGE="https://accounts.spotify.com/it/login"
CREATE_APP_PAGE="https://developer.spotify.com/dashboard/create"

def get_client_manager(client_id, client_secret):
    return SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

def have_tokens():
    exists_tokens_file=check_json(TOKENS_FILE)
    if exists_tokens_file:
        if not glob.glob(".cache*"):
            print("The tokens are not valid. You need to set them up again.")
            return False
    else:
        return False
    return True


def configure_tokens():
    while True:
        tokens={}
        own_credentials=check_yesno(input("Do you already own the CLIENT ID and the CLIENT SECRET? (Y/N) "))
        if not own_credentials:
            print("This process will guide you through the configuration of your tokens.")
            system("pause")
            print("First of all register or login on Spotify\n"+
                "If the program does not automatically redirect you to the page, navigate to:\n"+
                LOGIN_PAGE)
            open(LOGIN_PAGE, new=0)
            system("pause")
            print()
            print("Now, fill the form:\n"+
                "\tApp name: Genres Sorter\n"+
                "\tApp description: Sort out your messy playlists!\n"+
                "\tWebsite: https://github.com/retrohacking/spotify_gensort \n"+
                "\tRedirect URIs: "+REDIRECT+"\n"
                "If the program does not automatically redirect you to the page, navigate to:\n"+
                CREATE_APP_PAGE)
            open(CREATE_APP_PAGE, new=0)
            system("pause")
            print()
            print("We're almost done:\n"+
                "Select the app that you have just created -> Settings\n")
        
        tokens["client_id"]=input("Insert here the Client ID: ")
        tokens["client_secret"]=input("Insert here the Client Secret: ")
        tokens["username"]=input("Insert your Spotify username (find it at https://www.spotify.com/us/account/profile/): ")
        create_json(TOKENS_FILE, tokens)
        return tokens

def read_tokens():
    client_tokens=load_json(TOKENS_FILE)
    return client_tokens

def generate_user_token(uname, c_id, c_secret):
    return spotipy.util.prompt_for_user_token(username=uname, scope=SCOPE, client_id=c_id, client_secret=c_secret, redirect_uri=REDIRECT)