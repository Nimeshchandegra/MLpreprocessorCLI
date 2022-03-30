import pandas as pd
from sklearn.model_selection import train_test_split
dataset = pd.read_csv(r'C:\Users\Admin\Desktop\ml project\train-data.csv')
numeric_col = ['int16','int32','int64','float16','float32','float64']

global X_train
global X_test
global y_train
global y_test


def train_test_split_dataset(dataframe,target_column):
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

train_test_split_dataset(dataset,'Price')
print(y_test.shape)