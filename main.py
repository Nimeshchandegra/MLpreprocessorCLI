
import pandas as pd
from os import path

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
numeric_col = ['int16','int32','int64','float16','float32','float64']

# functions
def print_task(task):
    print()
    print('select task you want to perform')
    print()
    for tasks in task:
        print(tasks)
    print()



def func_task():
    print()
    task = [
        '1. Data Description',
        '2. Handling NULL Values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]
    print_task(task)
    print()
    while 1:
        task_selected = int(
            input('select the task u want to perform(press 0 to exit):'))
        if task_selected == 0:
            print('exit')
            break


        elif task_selected == 1:
            print()
            # function for Data Description
            func_task_Description()
            print_task(task)

        elif task_selected == 2:
            print('function for Handling NULL Values')
            func_task_missing()
            continue

        # function for Encoding Categorical Data
        elif task_selected == 3:
            print(' function for Encoding Categorical Data')
            # function for Encoding Categorical Data
            continue


        elif task_selected == 4:
            print('function for Feature Scaling ')
            # function for Feature Scaling
            continue


        elif task_selected == 5:
            print('function for Download the modified dataset')
            # function for Download the modified dataset
            continue
        else:
            print('please enter a valid input')



def func_task_Description():
    print()
    task_Description = [
        '1. describe all column',
        '2. describe a specific column ',
        '3. show dataset',
        '0. go to tasks selection'
    ]
    print_task(task_Description)
    print()
    while True:

        task_selected_description = int(input('select the task u want to perform(press 0 to exit):'))

        if task_selected_description == 0:
            func_task()

        elif task_selected_description == 1:
            column_describe(dataset)
            print()
            print()
            column_info(dataset)
            print_task(task_Description)
            # function column_describe(dataset)
            continue

        elif task_selected_description == 2:
            spec_col_describe(dataset)
            print_task(task_Description)
            continue
        elif task_selected_description == 3:
            display_dataset(dataset)
            print_task(task_Description)
            continue
        else:
            print('please enter a valid input')



def func_task_missing():
    print()
    task_missing = [
        '1. Number of missing values in each column',
        '2. remove unit from a particular column',
        '3. Remove a particular column',
        '4. Filling missing values using "MEAN"',
        '5. Filling missing values using "MEDIAN"',
        '6. Filling missing values using "MOST-FREQUENT VALUE"',
        '7. Display dataset',
        '0. go to tasks selection'
    ]
    print_task(task_missing)

    while True:

        task_selected_missing = int(input('select the task u want to perform(press 0 to exit):'))

        if task_selected_missing == 0:
            func_task()
            continue



        elif task_selected_missing == 1:
            missing_sum(dataset)
            print_task(task_missing)
            continue



        elif task_selected_missing == 2:
            remove_unit_col(dataset)
            print_task(task_missing)
            continue



        elif task_selected_missing == 3:
            drop_column_missing(dataset)
            print_task(task_missing)
            continue



        elif task_selected_missing == 4:
            missing_mean(dataset)
            print_task(task_missing)
            continue



        elif task_selected_missing == 5:
            missing_median(dataset)
            print_task(task_missing)
            continue



        elif task_selected_missing == 6:
            missing_mode(dataset)
            print_task(task_missing)
            continue



        elif task_selected_missing == 7:
            display_dataset(dataset)
            print_task(task_missing)
            continue

        else:
            print()
            print('please enter a valid input')
            print()



def data_Input():
    supported_extension = '.csv'
    paths = input('please enter the full path of your dataset:')
    filename, file_extension = path.splitext(paths)
    print(file_extension)
    if file_extension != supported_extension:
        print('provide file name with path and extension')
        return data_Input()
    else:
        try:
            df=pd.read_csv(filename+file_extension)

            return df
        except:
            print("dataset not found please provide valid file")
            return data_Input()



def show_columns(dataset):
    column_name=dataset.columns
    for columns in column_name:
        print (columns+'\t')




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
    return print(dataset.describe())



def spec_col_describe(dataset):
    column_name=input('please enter the specific column:')
    for colname in column_name_dict:
        if column_name == colname:
            return print(dataset[column_name].describe())
        else:
            continue
    print('please enter a valid column name')
    spec_col_describe(dataset)



def display_dataset(dataset):
    no_col=int(input('please enter number of row you want to print:'))
    return print(dataset.head(no_col))



def to_lower_case(col):

    for i in range(len(col)):
        col[i] = col[i].lower()
    return col


def remove_unit_col(dataframe):
    while True:
        print('press "0" to go to task menu')
        print()
        show_columns(dataframe)

        col_names = input('Enter the name of column where u want to remove the unit from (one at a time):')
        if col_names == 'exit':
            func_task_missing()
        else:
            dataframe['col'] = dataframe[col_names].str.replace(r'\D', '', regex=True)
            dataframe['col'] = pd.to_numeric(dataframe['col'])
            dataframe[col_names] = dataframe['col']
            print('unit changed')



def missing_sum(dataframe):
    print(dataframe.isnull().sum())



def drop_column_missing(dataframe):
    col_name = input('please enter the column you want to drop:')
    dataframe.drop(col_name, axis=1, inplace=True)



def missing_mean(dataframe):
    int_col = dataframe.select_dtypes(include=numeric_col)
    print('Column where you can use "MEAN" to replace the missing values:')
    print()
    print(int_col.isnull().sum())
    print()
    task_mean = [
        '1. fill missing values in a specific column using MEAN',
        '2. fill missing values in whole dataset using MEAN',
        '0. go to task menu'
    ]
    while True:
        print_task(task_mean)
        task_missing_mean = int(input('select the task u want to perform:'))

        if task_missing_mean == 0:
            func_task_missing()

        elif task_missing_mean == 1:
            col_name = input('Enter a particular column name you want to fill missing value(one at a time):')
            dataframe[col_name].fillna(int_col[col_name].mean(), inplace=True)

        elif task_missing_mean == 2:
            for i in int_col.columns[int_col.isnull().any(axis=0)]:
                dataframe[i].fillna(int_col[i].mean(), inplace=True)
        print(int_col.isnull().sum())



def missing_median(dataframe):
    int_col = dataframe.select_dtypes(include=numeric_col)
    print('Column where you can use "MEDIAN" to replace the missing values:')
    print()
    print(int_col.isnull().sum())
    print()
    task_median = [
        '1. fill missing values in a specific column using MEDIAN',
        '2. fill missing values in whole dataset using MEDIAN',
        '0. go to task menu'
    ]
    while True:
        print_task(task_median)
        task_missing_median = int(input('select the task u want to perform:'))

        if task_missing_median == 0:
            func_task_missing()

        elif task_missing_median == 1:
            col_name = input('Enter a particular column name you want to fill missing value(one at a time):')
            dataframe[col_name].fillna(int_col[col_name].median(), inplace=True)

        elif task_missing_median == 2:
            for i in int_col.columns[int_col.isnull().any(axis=0)]:
                dataframe[i].fillna(int_col[i].median(), inplace=True)
        print(int_col.isnull().sum())



def missing_mode(dataframe):
    int_col = dataframe.select_dtypes(include=numeric_col)
    print('Column where you can use "MODE" to replace the missing values:')
    print()
    print(int_col.isnull().sum())
    print()
    task_mode = [
        '1. fill missing values in a specific column using MODE',
        '2. fill missing values in whole dataset using MODE',
        '0. go to task menu'
    ]
    while True:
        print_task(task_mode)
        task_missing_mode = int(input('select the task u want to perform:'))

        if task_missing_mode == 0:
            func_task_missing()

        elif task_missing_mode == 1:
            col_name = input('Enter a particular column name you want to fill missing value(one at a time):')
            dataframe[col_name].fillna(int_col[col_name].mode()[0], inplace=True)

        elif task_missing_mode == 2:
            for i in int_col.columns[int_col.isnull().any(axis=0)]:
                dataframe[i].fillna(int_col[i].mode()[0], inplace=True)
        print(int_col.isnull().sum())



#function ends


### programs start
print('\t\t\t(^O^)\tHII Welcome To ' +
      '\033[1m'+'EFFORTLESS PREPROCESSER'+'\033[0m'+'\t(^O^)')
print()
print()

# path of dataset=C:\Users\Admin\Desktop\ml project\train-data.csv
dataset = data_Input()
print()
print('dataset suceessfully loaded')



print()
print()

# displaying all column
print('this are the following column in the given dataset:')
column_names = show_columns(dataset)
column_name_dict=dataset.columns
print(column_names)
print()

# asking for the target column
target_columns = target_column(column_name_dict)
print('target column:'+target_columns)
print()

func_task()

