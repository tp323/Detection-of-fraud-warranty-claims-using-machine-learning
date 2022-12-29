import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def treat_vals(data_to_fix):
    columns_with_values = ["AC_1001_Issue", "AC_1002_Issue", "AC_1003_Issue", "TV_2001_Issue", "TV_2002_Issue",
                           "TV_2003_Issue", "Claim_Value", "Service_Centre", "Product_Age", "Call_details", "Fraud"]
    columns_with_strings = ["Area", "Consumer_profile", "Product_category", "Product_type", "Purchased_from", "Purpose"]
    # should Fraud be here to?
    for i in columns_with_values:
        data_to_fix[i] = data_to_fix[i].fillna(data_to_fix[i].median())
    for i in columns_with_strings:
        data_to_fix[i] = data_to_fix[i].fillna(data_to_fix[i].mode()[0])
    # return data_to_fix


if __name__ == '__main__':
    csv_data = pd.read_csv(r'data\warranty_claims.csv')
    data = csv_data.drop("ID", axis='columns')
    # df.fillna(df.median())
    # df['Claim_Value'] = df['Claim_Value'].fillna(df['Claim_Value'].median())

    treat_vals(data)
    # treated_data = treat_vals(data)

    # print(df)
    # print(df.columns)

    X = data.drop("Fraud", axis='columns')
    y = data['Fraud']
    t = train_test_split(X, y, train_size=.9, test_size=.1)

