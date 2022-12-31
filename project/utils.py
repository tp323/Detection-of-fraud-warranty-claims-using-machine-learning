

if __name__ == '__main__':
    print()


# num_cols = list(data.select_dtypes(include=[np.number]).columns.values)
# categorical_cols = list(data.select_dtypes(include=['object']).columns)
# x_numeric_cols = list(data.select_dtypes(include=['float64']).columns.values)  # all numeric except Fraud

# column transformers
# ct_all = make_column_transformer((ohe, categorical_cols), (si, num_cols), remainder='passthrough')
# ct_x = make_column_transformer((ohe, categorical_cols), (si, x_numeric_cols), remainder='passthrough')
# ct_y = make_column_transformer((si, y_col), remainder='passthrough')
