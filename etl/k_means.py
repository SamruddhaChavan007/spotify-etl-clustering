import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ---------- Load Dataset ----------
dataset_path = "data/processed data/spotify_features_final.csv"
df = pd.read_csv(dataset_path)

# ---------- Select Audio Features ----------
audio_features = [
    'danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
    'instrumentalness', 'liveness', 'valence', 'tempo'
]
X = df[audio_features]

# ---------- Elbow Method ----------
k_range = range(1, 10)
wcss = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
print(wcss)

# ---------- Plot the Elbow ----------
plt.plot(k_range, wcss, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Within-Cluster Sum of Squares (WCSS)")
plt.grid(True)
plt.tight_layout()
plt.show()