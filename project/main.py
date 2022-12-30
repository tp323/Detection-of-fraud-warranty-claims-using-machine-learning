import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


def treat_vals(data_to_fix, string_cols):
    columns_with_numeric_values = list(data_to_fix.select_dtypes(include=[np.number]).columns.values)
    # should Fraud be here to?

    # fix lower case claim
    data_to_fix["Purpose"] = data_to_fix["Purpose"].replace("claim", "Claim")
    for i in columns_with_numeric_values:
        data_to_fix[i] = data_to_fix[i].fillna(data_to_fix[i].mean())
    for i in string_cols:
        data_to_fix[i] = data_to_fix[i].fillna(data_to_fix[i].mode()[0])


def one_hot_encode():
    area = ['Rural', 'Urban']
    consumer_profile = ['Business', 'Personal']
    product_category = ['Entertainment', 'Household']
    product_type = ['TV', 'AC']
    purchased_from = ['Manufacturer', 'Internet', 'Dealer']
    purpose = ['Complaint', 'Other', 'Claim']
    all_arrays = [area, consumer_profile, product_category, product_type, purchased_from, purpose]
    ids = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt = 0
    for n in all_arrays:
        arr = list(zip(ids, n))
        encoded_array = OneHotEncoder().fit_transform(arr).toarray()
        print(columns_with_strings[cnt], " - ", arr, ": \n", encoded_array)
        cnt += 1
    # TODO(save each encoded array)
    # TODO(check if its multi column or single approach)


if __name__ == '__main__':
    csv_data = pd.read_csv(r'data\warranty_claims.csv')
    data = csv_data.drop("ID", axis='columns')
    columns_with_strings = list(data.select_dtypes(include=['object']).columns)
    treat_vals(data, columns_with_strings)
    print(data["Purpose"].value_counts())
    X = data.drop("Fraud", axis='columns')
    y = data['Fraud']
    t = train_test_split(X, y, train_size=.9, test_size=.1)
    one_hot_encode()
