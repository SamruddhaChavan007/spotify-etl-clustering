import os
import pandas as pd
import logging
from sklearn.preprocessing import MinMaxScaler

#Make the directory "logs"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename='logs/etl_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_dataset(path, label):
    try:
        dataframe = pd.read_csv(path)
        print(f"Loaded {label} dataset with {len(dataframe)} rows.")
        return dataframe
    except Exception as e:
        logging.error(f"Failed to load {label} dataset from the {path}: {e}")
        return pd.DataFrame()
    
def normalize_features(df, exclude_cols):
    try:
        features = df.drop(columns=exclude_cols, errors='ignore')
        numeric_cols = features.select_dtypes(include=['float64', 'int64']).columns
        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(df[numeric_cols])
        df[numeric_cols] = scaled
        print(f"Normalized Columns: {list(numeric_cols)}")
        return df
    except Exception as e:
        print(f"Error normalizing features: {e}")
        return df
    
def save_dataset(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Saved the processed dataset to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save the dataset: {e}")
        
def main():
    kaggle_dataset_path = 'data/processed data/kaggle_processed.csv'
    spotify_dataset_path = 'data/processed data/spotify_processed.csv'
    output_path = 'data/processed data/spotify_features_final.csv'
    
    #Load the datasets
    kaggle_dataframe = load_dataset(kaggle_dataset_path, 'Kaggle Audio Features')
    spotify_dataframe = load_dataset(spotify_dataset_path, 'Spotify Audio Features')            #Optional
    
    if not kaggle_dataframe.empty:
        kaggle_dataframe = normalize_features(kaggle_dataframe, exclude_cols=['track_id', 'playlist_id', 'track_name'])
        save_dataset(kaggle_dataframe, output_path)
        
if __name__ == '__main__':
    main()