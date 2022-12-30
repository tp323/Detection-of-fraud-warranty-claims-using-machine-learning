import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from main import *

columns = ["Area", "Consumer_profile", "Product_category", "Product_type", "AC_1001_Issue", "AC_1002_Issue",
               "AC_1003_Issue", "TV_2001_Issue", "TV_2002_Issue", "TV_2003_Issue", "Claim_Value", "Service_Centre",
               "Product_Age", "Purchased_from", "Call_details", "Purpose", "Fraud"]


def find_domain(column):
    unique_values = set()
    for element in column:
        unique_values.add(element)
    return list(unique_values)


if __name__ == '__main__':
    csv_data = pd.read_csv(r'data\warranty_claims.csv')
    data = csv_data.drop("ID", axis='columns')
    columns_with_numeric_values = list(data.select_dtypes(include=[np.number]).columns.values)
    columns_with_strings = list(data.select_dtypes(include=['object']).columns)
    columns = list(data.columns.values)

    treat_vals(data, columns_with_strings)

    # print(list(data.select_dtypes(include=['int64']).columns.values))  # Fraud column
    # print(list(data.select_dtypes(include=['float64']).columns.values))  # all number columns except Fraud

    for n in columns_with_strings:
        print(n, "=", find_domain(data[n]))

# Unique values
# Area = ['Rural', 'Urban']
# Consumer_profile = ['Business', 'Personal']
# Product_category = ['Entertainment', 'Household']
# Product_type = ['TV', 'AC']
# Purchased_from = ['Manufacturer', 'Internet', 'Dealer']
# Purpose = ['Complaint', 'Other', 'Claim']

# Area,Consumer_profile,Product_category,Product_type,AC_1001_Issue,AC_1002_Issue,AC_1003_Issue,TV_2001_Issue,TV_2002_Issue,TV_2003_Issue,Claim_Value,Service_Centre,Product_Age,Purchased_from,Call_details,Purpose,Fraud
# AC_1001_Issue,AC_1002_Issue,AC_1003_Issue,TV_2001_Issue,TV_2002_Issue,TV_2003_Issue,Claim_Value,Service_Centre,Product_Age,Call_details
# Area,Consumer_profile,Product_category,Product_type,Purchased_from,Purpose
