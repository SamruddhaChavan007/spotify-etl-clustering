# Spotify Playlist ETL and Clustering

This project focuses on building an end-to-end ETL pipeline for Spotify playlist data, enriching it with audio features, and preparing the data for clustering using unsupervised learning techniques.

## Objective

To extract, process, and cluster music tracks based on their audio features to identify underlying patterns and groupings among songs.

## Project Overview

1. *Data Extraction*
   - Playlist metadata was extracted using the Spotify Web API.
   - The extracted data includes track name, artist, album, popularity, and duration.
   - The extracted dataset was saved as spotify_extracted_data.csv.

2. *Dataset Enrichment*
   - The Kaggle Spotify dataset was used to supplement the audio feature information.
   - Due to limited overlap between the Spotify API and Kaggle datasets, the clustering will be based on the full Kaggle dataset.

3. *Data Normalization*
   - Audio features from the Kaggle dataset were normalized using MinMaxScaler.
   - The processed dataset was saved as spotify_features_final.csv.

4. *Pipeline Testing*
   - A pipeline testing script (test_pipeline.py) was created to:
     - Load the input datasets.
     - Normalize the audio features.
     - Log any errors during the process to logs/etl_errors.log.
     - Save the final feature dataset.

## Next Steps
- Apply clustering (e.g., KMeans) on the processed dataset.
- Visualize the clusters using dimensionality reduction techniques like PCA.
- Interpret and analyze the resulting clusters.