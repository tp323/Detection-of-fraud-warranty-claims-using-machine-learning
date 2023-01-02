from sklearn.neural_network import MLPClassifier


def mlp_predicting(train, test, y_train):
    mlp = MLPClassifier()
    mlp.fit(train, y_train)
    return mlp.predict(test)

