import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if not client_id or not client_secret:
    print("❌ Missing credentials in .env")
    exit()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

playlist_id = "37i9dQZEVXcMieW15LMLZ3"  # Today's Top Hits

try:
    results = sp.playlist_tracks(playlist_id, limit=5)
    print("✅ Connected successfully. Sample tracks:")
    for item in results['items']:
        track = item['track']
        print(f"- {track['name']} by {track['artists'][0]['name']}")
except Exception as e:
    print(f"❌ Error: {e}")