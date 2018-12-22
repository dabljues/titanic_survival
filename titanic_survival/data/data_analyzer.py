import os
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

    def _facet_grid(self, func, x: List[str], col: str = None, row: str = None, orient: str = 'v',
                    color: str = None, save_name: 'str' = None, show: bool = False) -> None:
        # Enable/disable showing this particular plot
        if not show:
            plt.ioff()
        else:
            plt.ion()
        g = sns.FacetGrid(self.train_data, col=col, row=row)
        if func == sns.barplot:
            g.map(func, *x, orient=orient, ci=None, color=color)
        else:
            g.map(func, *x, color=color)
        if save_name is not None:
            plt.savefig(os.path.abspath(f'../images/{save_name}'), bbox_inches='tight')

    def analyze(self) -> None:
        # Check if survival rate is connected with Age
        self._facet_grid(plt.hist, col='Survived', x=['Age'], show=True, save_name='age_survival')
        # Check if survival rate is connected with Sex
        self._facet_grid(sns.barplot, col='Sex', x=['Survived'], color='#ff9933', save_name='sex_survival.png')
        # Check if the survival rate is connected with PClass
        self._facet_grid(sns.barplot, col='Pclass', x=['Survived'], color='#00ff00', save_name='pclass_survival.png')
        self._facet_grid(sns.barplot, col='Pclass', row='Sex', x=['Survived'], color='#ff33cc',
                         save_name='pclass_sex_survival.png')
