import pandas as pd


class DataReader:
    def __init__(self) -> None:
        pass

    @staticmethod
    def load_csv(path: str) -> pd.DataFrame:
        return pd.read_csv(path)
