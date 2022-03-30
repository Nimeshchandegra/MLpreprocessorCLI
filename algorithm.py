from threading import Thread
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import warnings



warnings.filterwarnings('ignore')
dataset=pd.read_csv(r'C:\Users\Admin\Desktop\ml project\train-data.csv')
dataset_encode = pd.read_csv(r'C:\Users\Admin\PycharmProjects\sem3\missing_done2.csv')
target_column = ['Price']


X = dataset_encode.drop(target_column,axis=1)
y = dataset_encode[target_column]
X_train,X_test,y_train,y_test = train_test_split(X , y , test_size=0.2 ,random_state=42)
print(X_train.shape)
print(y_train.shape)

scaler=preprocessing.StandardScaler()
col_name=X_train.columns.values
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

print('feature scalling done')


"""
regressor = Lasso(alpha=1)
regressor.fit(X_train_scaled,y_train)
y_pred = regressor.predict(X_test_scaled)
print(round(regressor.score(X_test_scaled,y_test)*100,4))

regressor = Ridge(alpha=1)
regressor.fit(X_train_scaled,y_train)
y_pred = regressor.predict(X_test_scaled)
print(round(regressor.score(X_test_scaled,y_test)*100,4))


regressor = LinearRegression()
regressor.fit(X_train_scaled,y_train)
y_pred = regressor.predict(X_test_scaled)
print(round(regressor.score(X_test_scaled,y_test)*100,4))

"""


def algorithm_var():
    global y_train
    y_train_int = y_train.astype(int)

    try:
        from sklearn.linear_model import Ridge, Lasso
        for i in range(1, 10):
            regressor = Lasso(alpha=i)
            regressor.fit(X_train_scaled, y_train)
            print(f"lasso for alpha {i}")
            y_pred = regressor.predict(X_test_scaled)
            print(round(regressor.score(X_test_scaled, y_test) * 100, 4))
            print()
            regressor = Ridge(alpha=i)
            regressor.fit(X_train_scaled, y_train)
            print(f"ridge for alpha {i}")
            y_pred = regressor.predict(X_test_scaled)
            print(round(regressor.score(X_test_scaled, y_test) * 100, 4))
            print()
    except:
        print('ridge and lasso didnt worked')

    print()
    print("---------------------------------------------------------------------------")
    elapsed = 70
    try:
        from sklearn.linear_model import LinearRegression

        clf = LinearRegression()
        clf.fit(X_train_scaled, y_train)
        print("LinearRegression")
        y_pred_LinearRegression = clf.predict(X_test_scaled)
        LinearRegression_score = (round(clf.score(X_test_scaled, y_test) * 100, 4))
        print(LinearRegression_score)
        print()
        print("---------------------------------------------------------------------------")
    except:
        print('linear regression didnt worked')

    try:
        from sklearn import metrics, svm

        clf = svm.SVR()
        clf.fit(X_train_scaled, y_train)
        print("1")
        print("SVR")
        y_pred_SVR = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print()
        print("---------------------------------------------------------------------------")

    except:
        pass

    try:
        from sklearn.tree import DecisionTreeRegressor

        clf = DecisionTreeRegressor(random_state=42)
        clf.fit(X_train_scaled, y_train)
        print("DecisionTreeRegressor")
        y_pred_DecisionTreeClassifier = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print()
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        import xgboost

        clf = xgboost.XGBRegressor(random_state=42)
        clf.fit(X_train_scaled, y_train)
        print("xgboost")
        y_pred_xgboost = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print()
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        from sklearn.ensemble import BaggingRegressor
        clf = BaggingRegressor(random_state=42)
        clf.fit(X_train_scaled, y_train)
        print("BaggingRegressor")
        y_pred_BaggingRegressor = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print()
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        from sklearn.neighbors import KNeighborsRegressor

        clf = KNeighborsRegressor()
        clf.fit(X_train_scaled, y_train_int)
        print("KNeighborsRegressor")
        y_pred_KNeighborsClassifier = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        from sklearn.linear_model import LogisticRegression
        clf = LogisticRegression()
        clf.fit(X_train_scaled, y_train)
        print("LogisticRegression")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass
    try:
        from sklearn.tree import DecisionTreeClassifier

        clf = DecisionTreeClassifier()
        clf.fit(X_train_scaled, y_train)
        print("DecisionTreeClassifier")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass
    try:

        from sklearn.neighbors import KNeighborsClassifier

        clf = KNeighborsClassifier()
        clf.fit(X_train_scaled, y_train)
        print("KNeighborsClassifier")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass
    try:
        from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

        clf = LinearDiscriminantAnalysis()
        clf.fit(X_train_scaled, y_train)
        print("LinearDiscriminantAnalysis")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        from sklearn.naive_bayes import GaussianNB

        clf = GaussianNB()
        clf.fit(X_train_scaled, y_train)
        print("GaussianNB")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")

    except:
        pass

    try:
        from sklearn.svm import SVC
        clf = SVC()
        clf.fit(X_train_scaled, y_train)
        print("SVC")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass

import numpy as np
from sklearn import metrics, svm
from sklearn.linear_model import LinearRegression



























"""
Algorithm for predict values:-
"""
shouldfinish = False
def algorithm_var():
    import time
    global shouldfinish
    global y_train
    y_train_int = y_train.astype(int)

    try:
        from sklearn.linear_model import Ridge, Lasso
        for i in range(1, 10):
            regressor = Lasso(alpha=i)
            regressor.fit(X_train_scaled, y_train)
            print(f"lasso for alpha {i}")
            y_pred = regressor.predict(X_test_scaled)
            print(round(regressor.score(X_test_scaled, y_test) * 100, 4))
            print()
            regressor = Ridge(alpha=i)
            regressor.fit(X_train_scaled, y_train)
            print(f"ridge for alpha {i}")
            y_pred = regressor.predict(X_test_scaled)
            print(round(regressor.score(X_test_scaled, y_test) * 100, 4))
            print()
    except:
        pass

    print()
    print("---------------------------------------------------------------------------")
    elapsed = 70
    try:
        from sklearn.linear_model import LinearRegression

        clf = LinearRegression()
        clf.fit(X_train_scaled, y_train)
        print("LinearRegression")
        y_pred_LinearRegression = clf.predict(X_test_scaled)
        LinearRegression_score = (round(clf.score(X_test_scaled, y_test) * 100, 4))
        print(LinearRegression_score)
        print()
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        from sklearn import metrics, svm

        clf = svm.SVR()
        clf.fit(X_train_scaled, y_train)
        print("1")
        print("SVR")
        y_pred_SVR = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print()
        print("---------------------------------------------------------------------------")

    except:
        pass


    try:
        from sklearn.tree import DecisionTreeRegressor

        clf = DecisionTreeRegressor(random_state=42)
        clf.fit(X_train_scaled, y_train)
        print("DecisionTreeRegressor")
        y_pred_DecisionTreeClassifier = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print()
        print("---------------------------------------------------------------------------")
    except:
        pass



    try:
        import xgboost

        clf = xgboost.XGBRegressor(random_state=42)
        clf.fit(X_train_scaled, y_train)
        print("xgboost")
        y_pred_xgboost = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print()
        print("---------------------------------------------------------------------------")
    except:
        pass


    try:
        from sklearn.ensemble import BaggingRegressor
        clf = BaggingRegressor(random_state=42)
        clf.fit(X_train_scaled, y_train)
        print("BaggingRegressor")
        y_pred_BaggingRegressor = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print()
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        from sklearn.neighbors import KNeighborsRegressor

        clf = KNeighborsRegressor()
        clf.fit(X_train_scaled, y_train_int)
        print("KNeighborsRegressor")
        y_pred_KNeighborsClassifier = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        from sklearn.linear_model import LogisticRegression
        clf = LogisticRegression()
        clf.fit(X_train_scaled, y_train)
        print("LogisticRegression")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass
    try:
        from sklearn.tree import DecisionTreeClassifier


        clf = DecisionTreeClassifier()
        clf.fit(X_train_scaled, y_train)
        print("DecisionTreeClassifier")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass
    try:

        from sklearn.neighbors import KNeighborsClassifier


        clf = KNeighborsClassifier()
        clf.fit(X_train_scaled, y_train)
        print("KNeighborsClassifier")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass
    try:
        from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

        clf = LinearDiscriminantAnalysis()
        clf.fit(X_train_scaled, y_train)
        print("LinearDiscriminantAnalysis")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass

    try:
        from sklearn.naive_bayes import GaussianNB

        clf = GaussianNB()
        clf.fit(X_train_scaled, y_train)
        print("GaussianNB")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")

    except:
        pass

    try:
        from sklearn.svm import SVC
        clf = SVC()
        clf.fit(X_train_scaled, y_train)
        print("SVC")
        y_pred = clf.predict(X_test_scaled)
        print(round(clf.score(X_test_scaled, y_test) * 100, 4))
        print("---------------------------------------------------------------------------")
    except:
        pass






algorithm_var()
"""
Algorithm for catergorical predict:-



"""




