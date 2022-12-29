import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
columns_with_strings = ["Area", "Consumer_profile", "Product_category", "Product_type", "Purchased_from", "Purpose"]


def treat_vals(data_to_fix):
    columns_with_values = ["AC_1001_Issue", "AC_1002_Issue", "AC_1003_Issue", "TV_2001_Issue", "TV_2002_Issue",
                           "TV_2003_Issue", "Claim_Value", "Service_Centre", "Product_Age", "Call_details", "Fraud"]
    # should Fraud be here to?
    for i in columns_with_values:
        data_to_fix[i] = data_to_fix[i].fillna(data_to_fix[i].mean())
    for i in columns_with_strings:
        data_to_fix[i] = data_to_fix[i].fillna(data_to_fix[i].mode()[0])


def one_hot_encode():
    area = ['Rural', 'Urban']
    consumer_profile = ['Personal', 'Business']
    product_category = ['Household', 'Entertainment']
    product_type = ['AC', 'TV']
    purchased_from = ['Manufacturer', 'Dealer', 'Internet']
    purpose = ['Other', 'claim', 'Claim', 'Complaint']
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
    treat_vals(data)

    X = data.drop("Fraud", axis='columns')
    y = data['Fraud']
    t = train_test_split(X, y, train_size=.9, test_size=.1)
    one_hot_encode()
