from sklearn.pipeline import Pipeline
from data_treatment import read_and_treat_data
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import pickle
from sklearn.metrics import classification_report


def model_stats(test, predicted):
    print("Accuracy = ", accuracy_score(test, predicted))
    class_rep = classification_report(test, predicted, target_names=["No Fraud", "Fraud"])
    return class_rep


if __name__ == '__main__':
    # read_data
    X_train, X_test, y_train, y_test, preprocessor = read_and_treat_data()
    ml_pipeline = Pipeline(steps=[("preprocess", preprocessor), ("model", MLPClassifier())])
    ml_pipeline.fit(X_train, y_train)
    print(ml_pipeline.score(X_test, y_test))
    print(model_stats(y_test, ml_pipeline.predict(X_test)))
    filename = 'saved_model.plk'
    pickle.dump(ml_pipeline, open(filename, 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))
    model_stats(y_test, loaded_model.predict(X_test))
