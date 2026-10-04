from pathlib import Path
from google.cloud import storage

BUCKET_NAME = "setu-data-handling"
PROJECT_ID = "SETU-20123784"

PROCESSED_DIR = Path("data/processed")

FILES_TO_UPLOAD = {
    PROCESSED_DIR / "train_2022.parquet":
        "processed/train_2022.parquet",

    PROCESSED_DIR / "validation_2022.parquet":
        "processed/validation_2022.parquet",

    PROCESSED_DIR / "test_2023.parquet":
        "processed/test_2023.parquet",

    PROCESSED_DIR / "future_2024.parquet":
        "processed/future_2024.parquet",
}


def upload_file(bucket, local_path, gcs_path):
    if not local_path.exists():
        raise FileNotFoundError(f"Local file not found: {local_path}")

    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(local_path)

    print(f"Uploaded {local_path} -> gs://{BUCKET_NAME}/{gcs_path}")


def main():

    client = storage.Client(project=PROJECT_ID)
    bucket = client.bucket(BUCKET_NAME)

    for local_path, gcs_path in FILES_TO_UPLOAD.items():
        upload_file(bucket, local_path, gcs_path)


if __name__ == "__main__":
    main()