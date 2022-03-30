import pandas as pd

dataset = pd.read_csv(r'C:\Users\Admin\Desktop\ml project\train-data.csv')
numeric_col = ['int16','int32','int64','float16','float32','float64']



def show_columns(dataset):
    column_name=dataset.columns
    for columns in column_name:
        print (columns+'\t')



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


def display_dataset(dataset):
    no_col=int(input('please enter number of row you want to print:'))
    print(dataset.head(no_col))
    print()


def print_task(task):
    print()
    print('select task you want to perform')
    print()
    for tasks in task:
        print(tasks)


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
            # func_task()
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
            col_name=input('Enter a particular column name you want to fill missing value(one at a time):')
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
            col_name=input('Enter a particular column name you want to fill missing value(one at a time):')
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
            col_name=input('Enter a particular column name you want to fill missing value(one at a time):')
            dataframe[col_name].fillna(int_col[col_name].mode()[0], inplace=True)

        elif task_missing_mode == 2:
            for i in int_col.columns[int_col.isnull().any(axis=0)]:
                dataframe[i].fillna(int_col[i].mode()[0], inplace=True)
        print(int_col.isnull().sum())






func_task_missing()



