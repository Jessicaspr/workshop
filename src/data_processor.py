import argparse
import numpy as np
import pandas as pd

def load_data(data_path):
    df = pd.read_csv(data_path)
    return df

def save_data(data_path, df):
    df.to_csv(data_path.replace('.csv','_processed.csv'), index=False)
    return None

def name_data(df):
    # Define the new column names
    col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 
                 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 
                 'native_country', 'income']
    
    df.columns = col_names
    return df

def data_replace(df):
    # replace value
    df['workclass'].replace('?', np.NaN, inplace=True)
    df['occupation'].replace('?', np.NaN, inplace=True)
    df['native_country'].replace('?', np.NaN, inplace=True)
    return df

def fill_data_categorical(df):
    # Identify categorical columns with missing values
    categorical_cols_with_na = [col for col in df.columns if df[col].dtype == 'object' and df[col].isnull().any()]
    
    for column_name in categorical_cols_with_na:
        # Calculate the most frequent value in the current column
        most_frequent_value = df[column_name].mode()[0]
        # Fill missing values with the most frequent value
        df[column_name].fillna(most_frequent_value, inplace=True)
    return df




# def log_txf(df, cols: list):
#     for col in cols:
#         df['log_'+col] = np.log(df[col]+1)
#     return df

# def remap_emp_length(x):
#     if x in ['< 1 year','1 year','2 years']:
#         return 'less_than_3yr'
#     if x in ['3 years','4 years','5 years']:
#         return '3_to_5yr'
#     if x in ['6 years','7 years','8 years','9 years']:
#         return '6_to_9yr'
#     return 'more_than_9yr'

def run(data_path):
    df = load_data(data_path)
    print("DataFrame Loaded:", df is not None)
    # df = log_txf(df, ['annual_inc'])
    # df['emp_len'] = df['emp_length'].map(remap_emp_length)
    df = name_data(df)
    print("DataFrame Loaded:", df is not None)
    df = data_replace(df)
    print("DataFrame Loaded:", df is not None)
    df=fill_data_categorical(df)
    print("DataFrame Loaded:", df is not None)
    save_data(data_path, df)
    return df

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--data_path", type=str)
    args = argparser.parse_args()
    run(args.data_path)