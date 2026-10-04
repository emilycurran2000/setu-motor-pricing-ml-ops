import pandas as pd

GCS_PATH = "gs://setu-data-handling/processed/validation_2022.parquet"

df = pd.read_parquet(GCS_PATH)

print("Loaded from GCS:", df.shape)
print(df.head())