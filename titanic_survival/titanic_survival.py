from learning.train import TitanicTrain


def titanic_survival():
    titanic_train = TitanicTrain('../data', train_file='train.csv', test_file='test.csv')
    c_data = titanic_train.model_data(['Survived'])
    titanic_train.train_knn(c_data, 3)


if __name__ == '__main__':
    titanic_survival()
