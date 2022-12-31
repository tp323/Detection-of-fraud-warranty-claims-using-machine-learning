import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier

from data_treatment import *

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = read_and_treat_data()
    print()
