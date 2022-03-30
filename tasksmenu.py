import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


dataset=pd.read_csv(r'C:\Users\Admin\Desktop\ml project\train-data.csv')
dataset_encoded = pd.read_csv(r'C:\Users\Admin\PycharmProjects\sem3\missing_done2.csv')


def print_task(task):
    print()
    print('select task you want to perform')
    print()
    for tasks in task:
        print(tasks)
    print()


global X_train_scaled
global X_test_scaled
global X_train
global X_test
global y_train
global y_test
target_column = 'Price'


def train_test_split_dataset(dataframe):
    global X_train
    global X_test
    global y_train
    global y_test

    X = dataframe.drop(target_column,axis=1)
    y = dataframe[target_column]

    X_train,X_test,y_train,y_test = train_test_split(X , y , test_size=0.2 ,random_state=42)
    print('shape of X_train = ',X_train.shape)
    print('shape of X_test = ',X_test.shape)
    print('shape of y_train = ',y_train.shape)
    print('shape of y_test = ',y_test.shape)




def normalization(X_train_dataframe,X_test_dataframe):
    scaler=preprocessing.MinMaxScaler()
    col_name=X_train_dataframe.columns.values
    train_scaled = scaler.fit_transform(X_train_dataframe)
    test_scaled = scaler.fit_transform(X_test_dataframe)

    dataframe_train_scaled = pd.DataFrame(train_scaled, columns=col_name)
    dataframe_test_scaled = pd.DataFrame(test_scaled, columns=col_name)
    return dataframe_train_scaled,dataframe_test_scaled


def standardization(X_train_dataframe,X_test_dataframe):
    scaler = preprocessing.StandardScaler()
    col_name = X_train_dataframe.columns.values
    train_scaled = scaler.fit_transform(X_train_dataframe)
    test_scaled = scaler.fit_transform(X_test_dataframe)

    dataframe_train_scaled = pd.DataFrame(train_scaled, columns=col_name)
    dataframe_test_scaled = pd.DataFrame(test_scaled, columns=col_name)
    return dataframe_train_scaled, dataframe_test_scaled


def feature_scaling():
    print()
    task_scaling = [
        '1. perform standardization',
        '2. perform normalization',
        '0. Go to task menu'
    ]
    print_task(task_scaling)
    print()
    while 1:
        task_selected = int(
            input('select the task u want to perform(press 0 to exit):'))
        if task_selected == 0:
            # func_task()
            continue


        elif task_selected == 1:
            print()
            X_train_scaled , X_test_scaled = standardization(X_train,X_test)
            print(X_train_scaled.describe().round(2))

            print_task(task_scaling)
            continue


        elif task_selected == 2:
            X_train_scaled , X_test_scaled = normalization(X_train,X_test)
            print(X_train_scaled.describe().round(2))
            print_task(task_scaling)

            continue

        elif task_selected == 3:
            train_test_split_dataset(dataset_encoded)
            print_task(task_scaling)

            continue




feature_scaling()









