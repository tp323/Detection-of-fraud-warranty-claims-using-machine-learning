import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer

UNNECESSARY_COLUMNS = ["ID"]


def standardize_data(data):
    scaler = StandardScaler().fit(data)
    standardized_data = scaler.transform(data)
    # print(standardized_data)
    print(standardized_data.std(axis=0))  # proof of standardization
    return data


def standardize_x_data(X_train, X_test):
    # TODO(CHECK IF MORE TREATMENT OF DATA IS REQUIRED FOR Y OR THERE IS NO NEED TO STANDARDIZE y SINCE ITS (1.0, 0.0))
    X_train_scaled = standardize_data(X_train)
    X_test_scaled = standardize_data(X_test)
    return X_train_scaled, X_test_scaled


def treat_data(data):
    data["Purpose"] = data["Purpose"].replace("claim", "Claim")  # fix lower case claim
    categorical_cols = list(data.select_dtypes(include=['object']).columns)
    x_numeric_cols = list(data.select_dtypes(include=['float64']).columns.values)  # all numeric except Fraud

    # column transformers
    ct_x = make_column_transformer((OneHotEncoder(), categorical_cols), (SimpleImputer(), x_numeric_cols), remainder='passthrough')

    X = data.drop("Fraud", axis='columns')
    y = data['Fraud']

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.9, test_size=.1)

    # one hot encode and fill missing values
    X_train = ct_x.fit_transform(X_train)
    X_test = ct_x.fit_transform(X_test)

    # TODO(FIX STANDARDIZATION IF BEFORE ENCODING AND FILLING MISSING VALUES THIS WILL EITHER CONTINUE EMPTY OR BE
    #  FILLED WITH INCORRECT VALUES IF AFTER WE ACCIDENTALLY STANDARDIZE ONE HOT ENCODE VALUES WHICH SHOULD NOT BE DONE
    #  CANT FILTER TABLES AND DIAGRAM SUGGESTS THAT STANDARDIZATION MUST BE DONE AFTER FILLING MISSING VALUES
    #  SOLUTION MIGHT JUST BE HARD CODED VALUES WITH THE TABLE NUMBERS TO BE STANDARDIZED FROM INDEX 14 ONWARDS)
    X_train_scaled, X_test_scaled = standardize_x_data(X_train, X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test


def read_and_treat_data():
    data = pd.read_csv(r'data\warranty_claims.csv').drop(columns=UNNECESSARY_COLUMNS)
    return treat_data(data)

