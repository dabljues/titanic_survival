import os
from dataclasses import dataclass

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from .data_reader import DataReader


@dataclass
class ClassificationData:
    X_train: pd.DataFrame
    Y_train: pd.DataFrame
    X_test: pd.DataFrame


class TitanicTrain:
    def __init__(self, data_dir, train_file='', test_file=''):
        self.data_reader = DataReader()
        self._load_files(data_dir, train_file, test_file)

    def _load_files(self, data_dir, train_file='', test_file=''):
        self.train_data = self.data_reader.load_csv(os.path.join(os.path.abspath(data_dir), train_file))
        self.test_data = self.data_reader.load_csv(os.path.join(os.path.abspath(data_dir), test_file))

    def model_data(self, features: []) -> ():
        return ClassificationData(self.train_data.drop(features), self.train_data[features],
                                  self.test_data.drop('PassengerId', axis=1).copy())

    def train_knn(self, data: ClassificationData, n_neighbors: int = 1):
        knn = KNeighborsClassifier(n_neighbors)
        knn.fit(data.X_train, data.Y_train)
