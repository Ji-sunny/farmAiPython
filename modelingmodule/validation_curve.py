import pandas as pd
from dbmodule import dbModule
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import numpy as np

oracle_db = dbModule.Database()

def modeling(table_name, cols_X, col_y, model):

    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]
    train_X, test_X, train_y, test_y = train_test_split(X, y , test_size=0.3)
    cross_val_score(model, train_X , train_y ,cv=5)
    param_range= np.logspace (-6,-1,10)

    train_scores, test_scores = validation_curve(
    SVC(), train_X , train_y , param_name='gamma', param_range=param_range,
    cv=10, scoring='accuracy', n_jobs=1
    )


    #교차 검증 점수의 평균과 표준편차를 계산
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    #테스트의 스코어가 가장 클때의 감마값을 이용하여 다시 모형을 만듬 
    gamma = param_range[test_scores_mean.argmax()]
    model = SVC(gamma=gamma).fit(train_X , train_y)
    score =model.score(test_X, test_y)


    return model, score