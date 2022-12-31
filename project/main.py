import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.compose import make_column_transformer

UNNECESSARY_COLUMNS = ["ID"]


def standardize_data(data_to_standardize):
    scaler = StandardScaler().fit(data_to_standardize)
    standardized_data = scaler.transform(data_to_standardize)
    # print(standardized_data)
    print(standardized_data.std(axis=0))  # proof of standardization

    return standardized_data


if __name__ == '__main__':
    data = pd.read_csv(r'data\warranty_claims.csv').drop(columns=UNNECESSARY_COLUMNS)
    data["Purpose"] = data["Purpose"].replace("claim", "Claim")  # fix lower case claim

    num_cols = list(data.select_dtypes(include=[np.number]).columns.values)
    categorical_cols = list(data.select_dtypes(include=['object']).columns)
    x_numeric_cols = list(data.select_dtypes(include=['float64']).columns.values)  # all numeric except Fraud
    y_col = ['Fraud']

    ohe = OneHotEncoder()
    si = SimpleImputer()

    # column transformers
    # ct_all = make_column_transformer((ohe, categorical_cols), (si, num_cols), remainder='passthrough')
    ct_x = make_column_transformer((ohe, categorical_cols), (si, x_numeric_cols), remainder='passthrough')

    # one hot encode and fill missing values
    # encoded_data = ct_all.fit_transform(data)

    X = data.drop("Fraud", axis='columns')

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.9, test_size=.1)

    # one hot encode and fill missing values
    X_train = ct_x.fit_transform(X_train)
    X_test = ct_x.fit_transform(X_test)

    # standardize data
    # no need to standardize y since its binary (1.0, 0.0)
    X_train_scaled = standardize_data(X_train)
    X_test_scaled = standardize_data(X_test)

    # TODO(CHECK IF MORE TREATMENT OF DATA IS REQUIRED FOR Y)
    # print(X_train_scaled)
    # print(X_test_scaled)
