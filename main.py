import os
import pandas as pd
import kaggle
import matplotlib.pyplot as plt

SEASON_STATS_DOWNLOAD_ROOT = "drgilermo/nba-players-stats"
TWENTY_FOUR_DOWNLOAD_ROOT = "eduardopalmieri/nba-player-stats-season-2425"
HOUSING_PATH = "datasets/nba"
OTHER_HOUSING = "datasets/nba/2024"


def fetch_nba_data(housing_url=SEASON_STATS_DOWNLOAD_ROOT, housing_path=HOUSING_PATH):
    kaggle.api.authenticate()
    if not os.path.isdir(housing_path):
        kaggle.api.dataset_download_files(housing_url, path=housing_path, unzip=True)


def load_season_stats_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "Seasons_Stats.csv")
    return pd.read_csv(csv_path)


def fetch_twenty_twenty_four_nba_data(housing_url=TWENTY_FOUR_DOWNLOAD_ROOT, housing_path=OTHER_HOUSING):
    kaggle.api.authenticate()
    if not os.path.isdir(housing_path):
        kaggle.api.dataset_download_files(housing_url, path=housing_path, unzip=True)


def load_twenty_four_stats_data(housing_path=OTHER_HOUSING):
    csv_path = os.path.join(housing_path, "database_24_25.csv")
    return pd.read_csv(csv_path)


def main():
    fetch_nba_data()
    fetch_twenty_twenty_four_nba_data()
    seasons_stats = load_season_stats_data()
    twenty_four_season_stats = load_twenty_four_stats_data()
    # seasons_stats_head = seasons_stats.head()
    # twenty_four_head = twenty_four_season_stats.head()
    print("obama")
    seasons_stats.hist(bins=50, figsize=(20, 15))
    plt.show()


if __name__ == '__main__':
    main()

