import pandas as pd
from matplotlib import pyplot as pt
import os
import numpy as np

dataset_path = "data/processed data/spotify_features_final.csv"
df = pd.read_csv(dataset_path)
print(list[df.columns])

pt.scatter(df['danceability'], df['energy'], df['loudness'])
pt.show()