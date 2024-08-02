import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

limit = 1
results = sp.current_user_recently_played(limit=limit)

# Should check to see if it's an album or single
album_id = results['items'][0]['track']['album']['id']
album_or_not = results['items'][0]['track']['album']['album_type']

test = sp.album_tracks(album_id)

# Need a way to extract the rest of the tracks in the album in question, will work on this

if album_or_not != 'album':
    print ("The most recently listened track is not on an album! No need to remind you of anything")
else:
    print("It is an album!")
    check_n_last_tracks = results['items'][0]['track']['album']['total_tracks']
    n_last_results = sp.current_user_recently_played(limit=check_n_last_tracks)
    album_tracks = sp.album_tracks(album_id)

    for track in range(check_n_last_tracks):
        print(album_tracks['items'][track]['name'])

    # Need to check if each track in the most recently listened to tracks are in the album, but need to account for duplicates!
    # Could delete each track fromm the album list as we check them
    for listened_track in range(check_n_last_tracks):
        print(n_last_results['items'][listened_track]['track']['name'])

    # Once it's been confirmed, if I have to review it, prompt me to enter some values (should be pretty easy, just look up some Bash
    # commands.


''' TODO:
- Get the most recent track 
- If the track is part of an album, get the rest of the tracks from the album
- get the length of the album and check to see if the n (where n is the length of the album) most recent tracks are tracks from the album
- If so, prompt the user for review 
- If not, continue analyzing
'''