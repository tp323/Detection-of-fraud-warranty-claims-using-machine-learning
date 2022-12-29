import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
columns = ["Area", "Consumer_profile", "Product_category", "Product_type", "AC_1001_Issue", "AC_1002_Issue",
               "AC_1003_Issue", "TV_2001_Issue", "TV_2002_Issue", "TV_2003_Issue", "Claim_Value", "Service_Centre",
               "Product_Age", "Purchased_from", "Call_details", "Purpose", "Fraud"]
columns_with_values = ["AC_1001_Issue", "AC_1002_Issue", "AC_1003_Issue", "TV_2001_Issue", "TV_2002_Issue",
                       "TV_2003_Issue", "Claim_Value", "Service_Centre", "Product_Age", "Call_details", "Fraud"]
columns_with_strings = ["Area", "Consumer_profile", "Product_category", "Product_type", "Purchased_from", "Purpose"]


def find_domain(column):
    unique_values = set()
    for element in column:
        unique_values.add(element)
    return list(unique_values)


def treat_vals(data_to_fix):
    for i in columns_with_values:
        data_to_fix[i] = data_to_fix[i].fillna(data_to_fix[i].median())
    for i in columns_with_strings:
        data_to_fix[i] = data_to_fix[i].fillna(data_to_fix[i].mode()[0])


if __name__ == '__main__':
    csv_data = pd.read_csv(r'data\warranty_claims.csv')
    data = csv_data.drop("ID", axis='columns')
    treat_vals(data)
    for n in columns_with_strings:
        print(n, " -> ", find_domain(data[n]))

# Unique values
# Area  ->  ['Urban', 'Rural']
# Consumer_profile  ->  ['Personal', 'Business']
# Product_category  ->  ['Entertainment', 'Household']
# Product_type  ->  ['TV', 'AC']
# Purchased_from  ->  ['Manufacturer', 'Dealer', 'Internet']
# Purpose  ->  ['Complaint', 'Claim', 'claim', 'Other']

# Area,Consumer_profile,Product_category,Product_type,AC_1001_Issue,AC_1002_Issue,AC_1003_Issue,TV_2001_Issue,TV_2002_Issue,TV_2003_Issue,Claim_Value,Service_Centre,Product_Age,Purchased_from,Call_details,Purpose,Fraud
# AC_1001_Issue,AC_1002_Issue,AC_1003_Issue,TV_2001_Issue,TV_2002_Issue,TV_2003_Issue,Claim_Value,Service_Centre,Product_Age,Call_details
# Area,Consumer_profile,Product_category,Product_type,Purchased_from,Purpose
