from . import *

def print_banner():
    print("""

     ██████╗ ███████╗███╗   ██╗███████╗ ██████╗ ██████╗ ████████╗
    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝
    ██║  ███╗█████╗  ██╔██╗ ██║███████╗██║   ██║██████╔╝   ██║   
    ██║   ██║██╔══╝  ██║╚██╗██║╚════██║██║   ██║██╔══██╗   ██║   
    ╚██████╔╝███████╗██║ ╚████║███████║╚██████╔╝██║  ██║   ██║   
     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

    """)
    print(f"\t\t\t\t\t{AUTHOR} - {YEAR}\tv{VERSION}")
    print(f"\t\t\t\t\t{GITHUB}")
    print("\n\n")

def print_playlists_name(playlists):
    for i in range(len(playlists)):
        print(f"[{i}] - {playlists[i]}")
    print()

def print_sorted_playlists(playlists):
    i=0
    for playlist in playlists:
        if playlist in DEFAULT_GENRES:
            print(f"[{i}] DEFAULT - {playlist} - {len(playlists[playlist])} song")
        else:
            print(f"[{i}] {playlist} - {len(playlists[playlist])} song")
        i+=1    

def print_parser_rules():
    print("\nHow to select the playlists:")
    print("\t- Every value or interval has to be delimited by a comma (,)")
    print("\t- An interval is defined by using an hyphen (-) between minimum and maximum value")
    print("\t- Create all the playlists with a dot (.)")
    print("\t- Quit with an exclamation point (!)")
    print("Examples:")
    print("\t10-100 | Generate the playlists from 10 to 100")
    print("\t1, 12, 15-18 | Generate the playlists number 1 and 12, then all the playlists from 15 to 18")
    print()

def print_chosen_playlists(chosen, playlists):
    playlists_name=list(playlists.keys())
    print("\nYou have chosen the following playlists:")
    for p in chosen:
        print(playlists_name[p])

def print_final():
    print("\nCheck the playlists on your Spotify, and if you like them Star the project, or open a issue for any problem!")
    print(f"GITHUB - {GITHUB}/spotify_gensort")
    print("\n\tSEE YOU SOON!")