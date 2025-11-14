import os
import pandas as pd
import kaggle

kaggle.api.authenticate()
DOWNLOAD_ROOT = "drgilermo/nba-players-stats"
HOUSING_PATH = "datasets/nba"


def fetch_nba_data(housing_url=DOWNLOAD_ROOT, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        kaggle.api.dataset_download_files(housing_url, path=housing_path, unzip=True)


def load_season_stats_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "Seasons_Stats.csv")
    return pd.read_csv(csv_path)


def main():
    print("Hello world!")
    fetch_nba_data()


if __name__ == '__main__':
    main()

