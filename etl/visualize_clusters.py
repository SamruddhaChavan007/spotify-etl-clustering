import pandas as pd
from matplotlib import pyplot as pt
from sklearn.decomposition import PCA
import logging

logging.basicConfig(
    filename='logs/etl_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------------Load the dataset---------------------


def load_dataset(path, label):
    try:
        dataframe = pd.read_csv(path)
        print(f"Loaded {label} dataset with {len(dataframe)} rows.")
        return dataframe
    except Exception as e:
        logging.error(f"Failed to load {label} dataset from the {path}: {e}")
        return pd.DataFrame()


def visualize(df, audio_features):
    try:
        X = df[audio_features]
        pca = PCA(0.95)
        pca_result = pca.fit_transform(X)
        print(f"Successfully implemented PCA, Shape: {pca_result.shape}")
        clusters = df['K-Means Cluster']
        x_axis = pca_result[:, 0]
        y_axis = pca_result[:, 1]
        pt.scatter(x_axis, y_axis, c=clusters, cmap='viridis', s=10)
        pt.xlabel("Principal Component 1")
        pt.ylabel("Principal Component 2")
        pt.title("Spotify Track Clusters (K=4) - PCA Projection")
        pt.show()
    except Exception as e:
        logging.error(f"Error during PCA transformation: {e}")

# ---------------------Main Function---------------------


def main():
    dataset_path = "data/processed data/spotify_features_clustered.csv"

    # Load the datasets
    kaggle_dataframe = load_dataset(dataset_path, 'Kaggle Dataset')

    # ---------- Select Audio Features ----------
    audio_features = [
        'danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
        'instrumentalness', 'liveness', 'valence', 'tempo'
    ]

    if not kaggle_dataframe.empty:
        visualize(kaggle_dataframe, audio_features)


if __name__ == '__main__':
    main()
