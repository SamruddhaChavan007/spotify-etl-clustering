import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# ---------- Load Datasets ----------
kaggle_df = pd.read_csv("data/external/tracks_features.csv")
spotify_df = pd.read_csv("data/processed data/enriched_tracks.csv")
output_directory = "data/processed data"

# ---------- Drop Unnecessary Columns ----------
kaggle_df = kaggle_df.drop(columns=['mode', 'key', 'time_signature'], errors='ignore')
spotify_df = spotify_df.drop(columns=['mode', 'key', 'time_signature'], errors='ignore')

# ---------- Define Audio Features to Normalize ----------
audio_features = [
    'danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
    'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms'
]

# ---------- Normalize Kaggle Dataset ----------
kaggle_scaled = kaggle_df.copy()
kaggle_scaled[audio_features] = MinMaxScaler().fit_transform(kaggle_scaled[audio_features])

# ---------- Normalize Spotify Dataset ----------
spotify_scaled = spotify_df.copy()
available_features = [col for col in audio_features if col in spotify_df.columns]
spotify_scaled[available_features] = MinMaxScaler().fit_transform(spotify_scaled[available_features])

# ---------- Save Outputs ----------
kaggle_scaled.to_csv(f'{output_directory}/kaggle_processed.csv', index=False)
spotify_scaled.to_csv(f'{output_directory}/spotify_processed.csv', index=False)

print("Normalization complete. Files saved as 'kaggle_processed.csv' and 'spotify_processed.csv'")