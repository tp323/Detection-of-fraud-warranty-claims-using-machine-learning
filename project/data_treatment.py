import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer

UNNECESSARY_COLUMNS = ["ID"]


def standardize_data(data, x_numeric_cols):
    scaler = StandardScaler().set_output(transform="pandas")
    data[x_numeric_cols] = scaler.fit_transform(data[x_numeric_cols])
    # print(data[x_numeric_cols].std(axis=0))  # proof of standardization
    return data


def treat_data(data, random_state=None):
    data["Purpose"] = data["Purpose"].replace("claim", "Claim")  # fix lower case claim
    x_num_cols = list(data.select_dtypes(include=['float64']).columns.values)  # all numeric except Fraud
    si = SimpleImputer()

    # column transformers
    ct_x_impute = make_column_transformer((si, x_num_cols), remainder='passthrough').set_output(transform="pandas")

    X, y = data.drop("Fraud", axis='columns'), data['Fraud']

    # split data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.9, test_size=.1, random_state=random_state)

    # fill missing values
    X_train = ct_x_impute.fit_transform(X_train)
    X_test = ct_x_impute.fit_transform(X_test)

    x_num_cols = list(X_train.select_dtypes(include=['float64']).columns.values)  # all numeric except Fraud

    # standardize numerical data
    standardize_data(X_train, x_num_cols)
    standardize_data(X_test, x_num_cols)

    # read new table to get new columns names for categorical data
    categorical_cols = list(X_train.select_dtypes(include=['object']).columns)
    ct_x_categorical_data = make_column_transformer((OneHotEncoder(), categorical_cols), remainder='passthrough')

    # one hot encode
    X_train_scaled = ct_x_categorical_data.fit_transform(X_train)
    X_test_scaled = ct_x_categorical_data.fit_transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test


def read_and_treat_data(random_state=None):
    file = os.path.join(os.path.dirname(__file__), r'data\warranty_claims.csv')
    data = pd.read_csv(file).drop(columns=UNNECESSARY_COLUMNS)
    return treat_data(data, random_state)
