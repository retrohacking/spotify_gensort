# Spotify Genres Sorter
Spotify Genres Sorter is an helper, completely written in Python, to sort out large playlists that contain (too) many genres of music! It will create many playlists containing all the songs from a main playlists divided by their genres.

## Setup and usage
Spotify Genres Sorter configuration is pretty easy since it is completely guided during its use. 

Prior to running it, though, it is necessary to download the required dependencies by running the following command:
>pip3 install -r requirements.txt

The main library on which Spotify Genres Sorter is based is [Spotipy](https://github.com/spotipy-dev/spotipy). It is important to notice that during the first execution of the tool it will be required the generation of user and client tokens. As already said the program will guide you through the generation of these tokens.

__In the case in which you already have the CLIENT_ID and CLIENT_SECRET, be careful to set as REDIRECT URIs the value "http://localhost/", else the generation of the token may fail.__

Once the requirements are installed you are ready to run the tool!
>python3 main.py

