from mlp import mlp_predicting
from data_treatment import read_and_treat_data
from classification_report import classify_ml_solution
from sklearn.metrics import accuracy_score


if __name__ == '__main__':
    # read_data
    X_train, X_test, y_train, y_test = read_and_treat_data()
    predicted_data = mlp_predicting(X_train, X_test, y_train)
    print("Accuracy = ", accuracy_score(y_test, predicted_data))
    classify_ml_solution(y_test, predicted_data)
