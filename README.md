# Spotify Playlist ETL and Clustering

This project focuses on building an end-to-end ETL pipeline for Spotify playlist data, enriching it with audio features, and preparing the data for clustering using unsupervised learning techniques.

## Objective

To extract, process, and cluster music tracks based on their audio features to identify underlying patterns and groupings among songs.

## Project Overview

1. Data Extraction
   - Playlist metadata was extracted using the Spotify Web API.
   - The extracted data includes track name, artist, album, popularity, and duration.
   - The extracted dataset was saved as spotify_extracted_data.csv.

2. Dataset Enrichment
   - The Kaggle Spotify dataset was used to supplement the audio feature information.
   - Due to limited overlap between the Spotify API and Kaggle datasets, the clustering will be based on the full Kaggle dataset.

3. Data Normalization
   - Audio features from the Kaggle dataset were normalized using MinMaxScaler.
   - The processed dataset was saved as spotify_features_final.csv.

4. Pipeline Testing
   - A pipeline testing script (test_pipeline.py) was created to:
     - Load the input datasets.
     - Normalize the audio features.
     - Log any errors during the process to logs/etl_errors.log.
     - Save the final feature dataset.

5. Clustering and Visualization
   - KMeans clustering was applied to the normalized dataset with K=4.
   - PCA was used to reduce the feature space to 2D for visualization.
   - The clustered data was saved as spotify_features_clustered.csv and plotted using a scatter plot.

6. Cluster Interpretation
   - The resulting clusters were analyzed by computing the mean of each audio feature per cluster.

### 📊 Cluster Profiles (KMeans, K=4 — Based on Real Data)

| Cluster | Description | Key Audio Characteristics |
|---------|-------------|---------------------------|
| *0* | 🎻 Instrumental & Acoustic | High acousticness (0.89), instrumentalness (0.83), low energy — likely ambient or classical music |
| *1* | 🎉 Energetic & Electronic | High energy (0.71), low acousticness (0.12), high instrumentalness — likely EDM/electronic tracks |
| *2* | 🎧 Mainstream & Danceable | High energy (0.72), danceability (0.56), low instrumentalness — likely pop or upbeat tracks |
| *3* | 🌿 Chill & Acoustic | High acousticness (0.79), moderate tempo, low speechiness — likely acoustic or indie songs |

## Next Steps
- Build a Tableau dashboard using the clustered dataset.
- Use SQL queries to explore feature-based filtering, genre grouping, or mood-based track selection.
- Finalize project documentation and publish on GitHub.