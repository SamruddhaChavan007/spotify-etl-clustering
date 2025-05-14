import os
import pandas as pd
from rapidfuzz import fuzz, process
import re

# -------------------------------
# File paths
# -------------------------------
extracted_spotify_data = "data/raw/tracks.csv"
kaggle_dataset_path = "data/external/tracks_features.csv"
output_path = "data/processed data/enriched_tracks.csv"

# -------------------------------
# Load CSVs
# -------------------------------
spotify_dataframe = pd.read_csv(extracted_spotify_data)
kaggle_dataframe = pd.read_csv(kaggle_dataset_path)

# -------------------------------
# Clean + combine fields for better matching
# -------------------------------
def clean_name(text):
    text = re.sub(r"\(.*?\)", "", str(text))  # Remove parentheses
    text = re.sub(r"feat\..*", "", text, flags=re.IGNORECASE)  # Remove 'feat.' part
    return re.sub(r'\s+', ' ', text).strip().lower()  # Normalize whitespace and lowercase

spotify_dataframe["track_name_clean"] = spotify_dataframe["track_name"].apply(clean_name)
spotify_dataframe["artist_clean"] = spotify_dataframe["artist"].str.lower().str.strip()
spotify_dataframe["key"] = spotify_dataframe["track_name_clean"] + " " + spotify_dataframe["artist_clean"]

kaggle_dataframe["track_name_clean"] = kaggle_dataframe["name"].apply(clean_name)
kaggle_dataframe["artist_clean"] = kaggle_dataframe["artists"].str.lower().str.strip()
kaggle_dataframe["key"] = kaggle_dataframe["track_name_clean"] + " " + kaggle_dataframe["artist_clean"]

# -------------------------------
# Build list of Kaggle keys for fuzzy search
# -------------------------------
kaggle_keys = kaggle_dataframe["key"].tolist()
print("Built the list of Kaggle keys")

# -------------------------------
# Collect matched results
# -------------------------------
matched_rows = []
print("Prepared to collect matched results")
print("Starting the matching loop")

counter = 1
for idx, row in spotify_dataframe.iterrows():
    query = row["key"]
    match, score, match_idx = process.extractOne(query, kaggle_keys, scorer=fuzz.token_sort_ratio)

    if score >= 85:
        enriched = kaggle_dataframe.iloc[match_idx].copy()
        enriched["match_score"] = score

        # Combine both datasets
        combined = row.to_dict()
        combined.update(enriched.to_dict())
        matched_rows.append(combined)
    else:
        print(f"No good match for: {query} → best: {match} (score: {score})")
    
    print(f"Iteration {counter} complete...")
    counter += 1

print("Finished matching loop.")

# -------------------------------
# Create final DataFrame and Save
# -------------------------------
enriched_df = pd.DataFrame(matched_rows)

if not enriched_df.empty:
    enriched_df.to_csv(output_path, index=False)
    print(f"Enriched data saved to: {output_path}")

print(f"Final match count: {len(enriched_df)} / {len(spotify_dataframe)} tracks")