import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR.parent / "data" / "processed" / "feature_engineered_dataset.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    return df