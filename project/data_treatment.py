import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

UNNECESSARY_COLUMNS = ["ID"]


def treat_data(data, random_state=None):
    data["Purpose"] = data["Purpose"].replace("claim", "Claim")  # fix lower case claim
    num_cols = list(data.select_dtypes(include=['float64']).columns.values)  # all numeric except Fraud
    cat_cols = list(data.select_dtypes(exclude='number').columns)

    # create pipelines
    num_pip = Pipeline(steps=[('impute', SimpleImputer()), ('standardize', StandardScaler())])
    cat_pip = Pipeline(steps=[('one-hot-encode', OneHotEncoder())])
    full_processor = ColumnTransformer(transformers=[('number', num_pip, num_cols), ('category', cat_pip, cat_cols)])

    # split data for training and testing
    X, y = data.drop("Fraud", axis='columns'), data['Fraud']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.9, test_size=.1, random_state=random_state)

    # treat data
    # y is not treated because it's numeric and does not require fill missing files and standardization
    X_train = full_processor.fit_transform(X_train)
    X_test = full_processor.fit_transform(X_test)
    return X_train, X_test, y_train, y_test


def read_and_treat_data(random_state=None):
    file = os.path.join(os.path.dirname(__file__), r'data\warranty_claims.csv')
    data = pd.read_csv(file).drop(columns=UNNECESSARY_COLUMNS)
    return treat_data(data, random_state)
