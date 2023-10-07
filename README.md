# Spotify Genres Sorter
Spotify Genres Sorter is an helper, completely written in Python, to sort out large playlists that contain (too) many genres of music! It will create many playlists containing all the songs from a main playlists divided by their genres.

## Setup
Spotify Genres Sorter configuration is pretty easy since it is completely guided during its use. 

Prior to running it, though, it is necessary to download the required dependencies by running the following command:
>pip3 install -r requirements.txt

The main library on which Spotify Genres Sorter is based is [Spotipy](https://github.com/spotipy-dev/spotipy). It is important to notice that during the first execution of the tool it will be required the generation of user and client tokens. As already said the program will guide you through the generation of these tokens.

__In the case in which you already have the CLIENT_ID and CLIENT_SECRET, be careful to set as REDIRECT URIs the value "http://localhost:1337", else the generation of the token may fail.__

## Usage
Once the requirements are installed you are ready to run the tool!
>python3 main.py

If the inserted tokens are correct the program will print automatically all the user's playlists. Here you can choose the playlist to sort out.

The program will print a prospect of the many playlists that can be created on the user's account. But it is not necessary to create __ALL__ the generated playlists. You will have to insert the indexes of the playlists you actually want to generate.

### Playlists index parser
The generated playlists can be so much, but the program provides you a parser to easily include intervals instead of manually inserting all their indexes. Here it is:

- All the playlists or intervals have to be separated by a comma (,)
- The user can insert a single index for a playlist
- The user can insert an interval by separating the minimum and the maximum index with a hyphen (-)
- The user can quit at this point with an exclamation point (!)
-The user can also select to create all the playlists with a dot (.)

__And Gensort also sorts the playlists by the number of their songs!__ <sub>(guess you wouldn't like to listen to a playlist with only 2 songs, right? :wink:)</sub>

