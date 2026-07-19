import pandas as pd


DATA_PATH = "/home/aximsoft/Documents/EOWA/Week_08/Notebooks/dataset/house_prices_cleaned.csv"


def load_data():

    return pd.read_csv(DATA_PATH)


def load_comparison():

    return pd.read_csv("/home/aximsoft/Documents/EOWA/Week_08/Notebooks/dataset/reports/model_comparison.csv")