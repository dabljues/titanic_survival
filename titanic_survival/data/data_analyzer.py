from dataclasses import dataclass
from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


@dataclass
class ClassificationData:
    X_train: pd.DataFrame
    Y_train: pd.DataFrame
    X_test: pd.DataFrame


class DataAnalyzer:
    train_data: pd.DataFrame
    test_data: pd.DataFrame

    def __init__(self, train_data: pd.DataFrame, test_data: pd.DataFrame) -> None:
        self.train_data = train_data
        self.test_data = test_data

    def model_data(self, features: List[str]) -> ClassificationData:
        return ClassificationData(self.train_data.drop(features, axis=1), self.train_data[features],
                                  self.test_data.drop('PassengerId', axis=1).copy())

    def _facet_grid(self, func, x: List[str], col: str = None, row: str = None, orient: str = 'v') -> None:
        g = sns.FacetGrid(self.train_data, col=col, row=row)
        if func == sns.barplot:
            g.map(func, *x, orient=orient, ci=None)
        else:
            g.map(func, *x)
        g.add_legend()
        plt.show()

    def analyze(self) -> None:
        # Check if survival rate is connected with Age
        self._facet_grid(plt.hist, col='Survived', x=['Age'])
        # Check if survival rate is connected with Sex
        self._facet_grid(sns.barplot, col='Sex', x=['Survived'])
        # Check if the survival rate is connected with PClass
        self._facet_grid(sns.barplot, col='Pclass', x=['Survived'])
