import pandas as pd
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-read-private"
))


playlists = {
    "Most Played Songs 2025": "6IoAdfkxFwfTY4Ug7TVRMY",
    "Pop Playlist 2025": "2UZk7JjJnbTut1w8fqs3JL",
    "Rap Playlist 2025": "4nZo2X8iHrwhYBYdKvysgI",
    "Calm": "0ldH4ltKERLCOH3zsEcQm0",
    "Rock": "4aQsjBuSIy3yUs8w6I2OQr",
    "Indie Folk Feel": "6je4qaBiNqjgxYdq6g1ABc"
}


def get_playlist_tracks(sp, playlist_name, playlist_id):
    print(f"📥 Extracting from: {playlist_name}")
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

# Save JSON

with open("data/raw/playlists_raw.json", "w") as f:
    json.dump(all_tracks, f, indent=4)

# Save CSV
df = pd.DataFrame(all_tracks)
if not df.empty:
    df.to_csv("data/raw/tracks.csv", index=False)
    print("✅ All playlist tracks saved.")