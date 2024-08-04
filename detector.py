import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys


scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

limit = 1
results = sp.current_user_recently_played(limit=limit)

# Should check to see if it's an album or single
album_id = results['items'][0]['track']['album']['id']
album_or_not = results['items'][0]['track']['album']['album_type']


# Need a way to extract the rest of the tracks in the album in question, will work on this

if album_or_not != 'album':
    print("The most recently listened track is not on an album! No need to remind you of anything")
else:
    # print("It is an album!")
    check_n_last_tracks = results['items'][0]['track']['album']['total_tracks']
    n_last_results = sp.current_user_recently_played(limit=check_n_last_tracks)
    album_tracks = sp.album_tracks(album_id)
    album_cover = sp.album(album_id)

    album_cover = album_cover['images'][0]['url']
    album_track_titles = []
    recently_listened_track_titles = []

    n_last_results_to_remove = []
    album_tracks_to_remove = []

    for item in n_last_results['items']:
        recently_listened_track_titles.append(item['track']['name'])
        n_last_results_to_remove.append(item['track']['name'])

    for track in album_tracks['items']:
        album_track_titles.append(track['name'])
        album_tracks_to_remove.append(track['name'])

    for listened_track in recently_listened_track_titles:
        if listened_track in album_tracks_to_remove:
            n_last_results_to_remove.remove(listened_track)
            album_tracks_to_remove.remove(listened_track)
        else:
            continue


    if len(n_last_results_to_remove) == 0 and len(album_tracks_to_remove) == 0:
        # These print messages are here to help debug, in case something isn't working as intended
        # print("Did listen to an entire album")
        # To avoid having to split a string in a batch file which looks confusing, I will just be writing the link of the album directly to the file
        sys.stdout.write(album_cover)
    else:
        tracks_listened_to = len(album_tracks['items']) - len(album_tracks_to_remove)
        sys.stdout.write('false')
        # Same case for this print statement as above
        # print("Did not listen to an entire album. Only listened to " + str(tracks_listened_to) + " out of " + str(len(album_track_titles)) + " tracks")

    sys.exit(0)
