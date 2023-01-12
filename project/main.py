from mlp import mlp_model
from data_treatment import read_and_treat_data
from classification_report import classify_ml_solution
from sklearn.metrics import accuracy_score
import pickle


def model_stats(test, predicted):
    print("Accuracy = ", accuracy_score(test, predicted))
    classify_ml_solution(test, predicted)


if __name__ == '__main__':
    # read_data
    X_train, X_test, y_train, y_test, pipeline = read_and_treat_data()
    while True:
        model = mlp_model(X_train, y_train)
        model_stats(y_test, model.predict(X_test))
        # if accuracy_score(y_test, model.predict(X_test)) > 0.982:
        break

    filename = 'saved_model.plk'
    pickle.dump(model, open(filename, 'wb'))

    loaded_model = pickle.load(open(filename, 'rb'))
    model_stats(y_test, loaded_model.predict(X_test))


