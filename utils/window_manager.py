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
    for playlist in sorted(playlists, key=lambda playlist: len(playlists[playlist]), reverse=True):
        if playlist in DEFAULT_GENRES:
            print(f"[{i}] DEFAULT - {playlist} - {len(playlists[playlist])} song")
        else:
            print(f"[{i}] {playlist} - {len(playlists[playlist])} song")
        i+=1
    