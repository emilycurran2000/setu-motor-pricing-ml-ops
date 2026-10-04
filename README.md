# SETU Motor Pricing MLOps Project

Project for the SETU Data Handling and Infrastructure for AI module.

## Project

The aim is to build a motor insurance risk model using a public Spanish motor insurance dataset from Mendeley Data.

The data covers 2022 to 2024 and include policy, driver, vehcile, exposure and claims information.

Raw data is not stored in this repo.

## Milestone 1

Milestone 1 covers the data source, storage and split design.

The current split is:

- 2022 - train / validation
- 2023 - test
- 2024 - future data

full write-up:

[Milestone 1](Milestone1.md)

## Code

Main scripts are in `src/`:

- `prepare_splits.py`
- `upload_to_gcs.py`
- `verify_gcs.py`

Dependencies are in `requirements.txt`.