import unittest
from mlp import mlp_predicting
from data_treatment import read_and_treat_data
from sklearn.metrics import accuracy_score


def mlp_score():
    test_X_train, test_X_test, test_y_train, test_y_test = read_and_treat_data()
    test_predicted_data = mlp_predicting(test_X_train, test_X_test, test_y_train)
    score = accuracy_score(test_y_test, test_predicted_data)
    return score


class TestMLP(unittest.TestCase):

    def test_prediction_above_70_percent(self):
        score = mlp_score()
        self.assertGreater(score, 0.7)
        print("Accuracy = ", score)

    def test_prediction_above_80_percent(self):
        score = mlp_score()
        self.assertGreater(score, 0.8)

    def test_prediction_above_90_percent(self):
        score = mlp_score()
        self.assertGreater(score, 0.9)

    def test_prediction_above_95_percent(self):
        score = mlp_score()
        self.assertGreater(score, 0.95)


if __name__ == '__main__':
    unittest.main()
