import pandas as pd
from matplotlib import pyplot as pt
import os
import numpy as np
from sklearn.cluster import KMeans

dataset_path = "data/processed data/spotify_features_final.csv"
output_path = "data/processed data/spotify_features_clustered.csv"
df = pd.read_csv(dataset_path)
print(list(df.columns))

# ---------- Select Audio Features ----------
audio_features = [
    'danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
    'instrumentalness', 'liveness', 'valence', 'tempo'
]
X = df[audio_features]

kmeans = KMeans(n_clusters=4, random_state=42)
y_predicted = kmeans.fit_predict(X)

print(y_predicted)

df['K-Means Cluster'] = y_predicted
print(list(df.columns))

df.to_csv(output_path, index=False)