from sklearn.metrics import classification_report, confusion_matrix


def classify_ml_solution(y_test, y_predict):
    classification_rep = classification_report(y_test, y_predict, target_names=["No Fraud", "Fraud"])
    conf_matrix = confusion_matrix(y_test, y_predict)
    print(classification_rep)
    return classification_rep, conf_matrix
