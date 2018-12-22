from data.data_analyzer import DataAnalyzer
from learning.train import TitanicTrain


def titanic_survival() -> None:
    titanic_train = TitanicTrain()
    if not titanic_train.load_files('../data', train_file='train.csv', test_file='test.csv'):
        return
    # Modeling the data, finding interesting features
    data_analyzer: DataAnalyzer = DataAnalyzer(titanic_train.train_data, titanic_train.test_data)
    data_analyzer.analyze()
    # Do the actual learning and predicting
    # c_data = data_analyzer.model_data(['Survived'])
    # titanic_train.train_knn(c_data, 3)


if __name__ == '__main__':
    titanic_survival()
