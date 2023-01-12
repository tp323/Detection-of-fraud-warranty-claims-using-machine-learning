from sklearn.neural_network import MLPClassifier


def mlp_model(x_train, y_train):
    mlp = MLPClassifier()
    mlp.fit(x_train, y_train)
    return mlp

