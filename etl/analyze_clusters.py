import pandas as pd
import logging

logging.basicConfig(
    filename='logs/etl_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --------------------- Load the Dataset ---------------------


def load_dataset(path, label):
    try:
        df = pd.read_csv(path)
        print(f"Loaded {label} dataset with {len(df)} rows.")
        return df
    except Exception as e:
        logging.error(f"Failed to load {label} dataset from {path}: {e}")
        return pd.DataFrame()

# --------------------- Analyze Clusters ---------------------


def analyze_clusters(df, audio_features):
    try:
        summary = df.groupby("K-Means Cluster")[audio_features].mean()
        print("\n===== Cluster Feature Summary =====\n")
        print(summary)
        return summary
    except Exception as e:
        logging.error(f"Failed to analyze clusters: {e}")
        return pd.DataFrame()

# --------------------- Main Function ---------------------


def main():
    dataset_path = "data/processed data/spotify_features_clustered.csv"

    # Define audio features
    audio_features = [
        'danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
        'instrumentalness', 'liveness', 'valence', 'tempo'
    ]

    # Load dataset
    df = load_dataset(dataset_path, 'Spotify Clustered Dataset')

    if not df.empty:
        analyze_clusters(df, audio_features)


if __name__ == '__main__':
    main()