import os
from dataclasses import dataclass
from typing import List

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from data.data_reader import DataReader


@dataclass
class ClassificationData:
    X_train: pd.DataFrame
    Y_train: pd.DataFrame
    X_test: pd.DataFrame


class TitanicTrain:
    data_reader: DataReader
    train_data: pd.DataFrame
    test_data: pd.DataFrame

    def __init__(self):
        self.data_reader = DataReader()

    def load_files(self, data_dir, train_file='', test_file='') -> bool:
        try:
            self.train_data = self.data_reader.load_csv(os.path.join(os.path.abspath(data_dir), train_file))
        except FileNotFoundError:
            print(f'Train file doesn\'t exist!')
            return False
        try:
            self.test_data = self.data_reader.load_csv(os.path.join(os.path.abspath(data_dir), test_file))
        except FileNotFoundError:
            print(f'Test file doesn\'t exist!')
            return False
        return True

    def model_data(self, features: List[str]) -> ClassificationData:
        return ClassificationData(self.train_data.drop(features, axis=1), self.train_data[features],
                                  self.test_data.drop('PassengerId', axis=1).copy())

    @staticmethod
    def train_knn(data: ClassificationData, n_neighbors: int = 1) -> float:
        knn = KNeighborsClassifier(n_neighbors)
        knn.fit(data.X_train, data.Y_train)
        return 0.0
