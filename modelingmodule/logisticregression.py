import pandas as pd
from dbmodule import dbModule
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
oracle_db = dbModule.Database()


def logesticregression(table_name, cols_X, col_y, pred_cols_X):
    
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]

    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)

    # 모델 학습 
    model = LogisticRegression(max_iter=5000).fit(train_X,train_y)
    xx = np.linspace(-1, 1, train_X.shape[1]*train_X.shape[0])
    xx = xx.reshape(train_X.shape[0], train_X.shape[1])
    XX = xx[:, np.newaxis]
    XX = XX.reshape(train_X.shape[0], train_X.shape[1])
    prob = model.predict_proba(XX)[:,:train_X.shape[1]]
    
    score = model.score(test_X, test_y)
    
    #예측된확률
    X_test =[pred_cols_X]
    predict = model.classes_, model.predict_proba(X_test)[0]

    oracle_db.create_modeling_table(table_name, modeling_name, visualized_data)

    return predict, score