import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json
import pandas as pd
from spotipy.util import prompt_for_user_token

load_dotenv()

token = prompt_for_user_token(
    username=None,
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-read-private",
)

sp = spotipy.Spotify(auth=token)



playlists = {
    "Top 50 India": "37i9dQZEVXbLZ52XmnySJg"#,
    # "Top Songs Global": "37i9dQZEVXbNG2KDcFcKOF",
    # "Top Viral Global": "37i9dQZEVXbLiRSasKsNU9",
    # "Top 50 India": "37i9dQZEVXbLZ52XmnySJg",
    # "Top Songs India": "37i9dQZEVXbMWDif5SCBJq",
    # "Top Viral India": "37i9dQZEVXbK4NvPi6Sxit"
}


def get_playlist_tracks(sp, playlist_name, playlist_id):
    print(f"Extracting from: {playlist_name}")
    results = sp.playlist_tracks(playlist_id)
    tracks = []

    for item in results['items']:
        track = item['track']
        if track and track['id']:
            tracks.append({
                'track_id': track['id'],
                'track_name': track['name'],
                'artist': track['artists'][0]['name'],
                'playlist_name': playlist_name
            })

    return tracks


all_tracks = []

for name, pid in playlists.items():
    tracks = get_playlist_tracks(sp, name, pid)
    all_tracks.extend(tracks)

# Saving file as JSON
with open("data/raw/playlists_raw.json", "w") as f:
    json.dump(all_tracks, f, indent=4)

# Save the file as CSV
df = pd.DataFrame(all_tracks)
df.to_csv("data/raw/tracks.csv", index=False)


print("All playlists tracks saved.")