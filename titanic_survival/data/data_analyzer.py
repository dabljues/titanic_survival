# import seaborn as sns
# import matplotlib.pyplot as plt
import pandas as pd


class DataAnalyzer:
    train_data: pd.DataFrame
    test_data: pd.DataFrame

    def __init__(self, train_data: pd.DataFrame, test_data: pd.DataFrame) -> None:
        self.train_data = train_data
        self.test_data = test_data

    def analyze(self):
        pass
