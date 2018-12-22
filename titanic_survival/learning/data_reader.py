import pandas as pd


class DataReader:
    def __init__(self):
        pass

    @staticmethod
    def load_csv(path) -> pd.DataFrame:
        return pd.read_csv(path)
