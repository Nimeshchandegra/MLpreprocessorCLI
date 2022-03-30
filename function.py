import pandas as pd
from os import path
import sys
from sklearn.datasets import load_iris
from tabulate import tabulate


supported_extension = '.csv'
df = pd.read_csv('dataset_clinic.csv')
target_columns = 'diagnosis'




def show_columns(data):
    column_name=data.columns
    for columns in column_name:
        print (columns+'\t')
        return column_name



def target_column(column_name):
    target_columns = input('please select the target column:')
    i = 0
    for column in column_name:
        if target_columns == column:
            return column

        else:
            i = 2
            continue
    if i == 2:
        i = 0
        print('please enter valid column')
        return target_column(column_name)



def column_info(dataset):
    return dataset.info()



def column_describe(dataset):
    return dataset.describe()



def spec_col_describe(dataset,column_name):
    return dataset[column_name].describe()



def display_dataset(dataset):
    return dataset



def to_lower_case(col):

    for i in range(len(col)):
        col[i] = col[i].lower()
    return col



def unique_values(dataset):
    object_col = dataset.select_dtypes(include='object')
    i=0

    for col in object_col:
        col_dict = {col : str(dataset[col].nunique())}
        print(col_dict)
        i=i+1




label_encoder()

print(
df.head(10)
)


