import pandas as pd
import joblib


DATA_PATH = "/home/aximsoft/Documents/AximSoft_EOWA/Week_08/Notebooks/dataset/house_prices_cleaned.csv"


def load_data():

    return pd.read_csv(DATA_PATH)


def load_comparison():

    return pd.read_csv("/home/aximsoft/Documents/AximSoft_EOWA/Week_08/Notebooks/dataset/reports/model_comparison.csv")
def model():
    model = joblib.load("/home/aximsoft/Documents/AximSoft_EOWA/Week_08/Notebooks/dataset/models/best_model1.pkl")
    return model