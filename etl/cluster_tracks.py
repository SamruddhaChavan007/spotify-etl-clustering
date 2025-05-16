import pandas as pd
from sklearn.cluster import KMeans
import logging

logging.basicConfig(
    filename='logs/etl_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#---------------------Load the dataset---------------------
def load_dataset(path, label):
    try:
        dataframe = pd.read_csv(path)
        print(f"Loaded {label} dataset with {len(dataframe)} rows.")
        return dataframe
    except Exception as e:
        logging.error(f"Failed to load {label} dataset from the {path}: {e}")
        return pd.DataFrame()

#---------------------K Means Algorithm---------------------
def kmean_algorithm(df, audio_features):
    try:
        X = df[audio_features]
        kmeans = KMeans(n_clusters=4, random_state=42)
        df['K-Means Cluster'] = kmeans.fit_predict(X)
        print(f"Clustering complete. Columns now: {list(df.columns)}")
        return df
    except Exception as e:
        logging.error(f"KMeans clustering failed: {e}")

#---------------------Save the dataset---------------------
def save_dataset(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Saved the processed dataset to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save the dataset: {e}")

#---------------------Main Function---------------------
def main():
    dataset_path = "data/processed data/spotify_features_final.csv"
    output_path = "data/processed data/spotify_features_clustered.csv"

    # Load the datasets
    kaggle_dataframe = load_dataset(
        dataset_path, 'Kaggle Dataset')

    # ---------- Select Audio Features ----------
    audio_features = [
        'danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
        'instrumentalness', 'liveness', 'valence', 'tempo'
    ]

    if not kaggle_dataframe.empty:
        kaggle_dataframe = kmean_algorithm(kaggle_dataframe, audio_features)
        save_dataset(kaggle_dataframe, output_path)


if __name__ == '__main__':
    main()