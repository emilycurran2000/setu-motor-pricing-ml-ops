from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/Dataset of motor insurance portfolio.csv")
OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW_PATH, sep=";")

required_columns = {"year", "insured_id"}
missing = required_columns - set(df.columns)

if missing:
    raise ValueError(f"Missing required columns: {missing}")

print("Full dataset:", df.shape)
print(df["year"].value_counts().sort_index())

data_2022 = df[df["year"] == 2022].copy()
test = df[df["year"] == 2023].copy()
future = df[df["year"] == 2024].copy()

# Randomly split 2022 into 80% training / 20% validation
data_2022 = data_2022.sample(frac=1, random_state=42)

split_point = int(len(data_2022) * 0.8)

train = data_2022.iloc[:split_point].copy()
validation = data_2022.iloc[split_point:].copy()

# Sanity checks
assert len(train) + len(validation) == len(data_2022)
assert len(train) + len(validation) + len(test) + len(future) == len(df)

assert set(train["year"]) == {2022}
assert set(validation["year"]) == {2022}
assert set(test["year"]) == {2023}
assert set(future["year"]) == {2024}

# Store as Parquet
train.to_parquet(
    OUTPUT_DIR / "train_2022.parquet",
    index=False
)

validation.to_parquet(
    OUTPUT_DIR / "validation_2022.parquet",
    index=False
)

test.to_parquet(
    OUTPUT_DIR / "test_2023.parquet",
    index=False
)

future.to_parquet(
    OUTPUT_DIR / "future_2024.parquet",
    index=False
)

print(f"Train:      {train.shape}")
print(f"Validation: {validation.shape}")
print(f"Test:       {test.shape}")
print(f"Future:     {future.shape}")

# Read files back to check they were written correctly
for file in [
    "train_2022.parquet",
    "validation_2022.parquet",
    "test_2023.parquet",
    "future_2024.parquet",
]:
    path = OUTPUT_DIR / file
    check = pd.read_parquet(path)
    print(f"{file}: {check.shape}")