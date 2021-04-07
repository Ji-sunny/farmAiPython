import pandas as pd
import numpy as np
import pickle 
from dbmodule import dbModule
oracle_db = dbModule.Database()

from sklearn.linear_model import Perceptron

def modeling(table_name, col_X, col_y):
    # ---------------------------------------------
    data = oracle_db.read_data_all(table_name)
    # data --> table_name으로 바꾸기
    # ---------------------------------------------

    # col_X : <list>
    # col_y : <string>
    # pred_cols_X : <list>
    # sel_cols -> [col_name, col_name, ...]
    
    col_X_arr = pd.DataFrame(data, columns=col_X).values
    col_y_arr = data[col_y].values
    
    model = Perceptron(max_iter=100, eta0=0.1, random_state=1).fit(col_X_arr, col_y_arr)
    
    col_X_arr = pd.DataFrame(data, columns=col_X).values
    col_y_arr = (data[col_y].values).squeeze()
    # Humidity 20이하값의 이상치 row 삭제하기
    # temperature 20이하값의 이상치 row 삭제하기
    model = Perceptron(max_iter=1000, eta0=0.1, random_state=1).fit(col_X_arr, col_y_arr)

    # model만 return 하도록 수정
    return model

# uses perceptron model & data for visualization
def visualizeperceptron(table_name, model, col_X, pred_X):
    # https://www.amcharts.com/demos/polar-scatter/
    # scatter visualization
    # category -> column명들 : col_X
    pred_X_label = model.predict(pred_X)
    pred_X_score = model.score(pred_X, pred_X_label)
    data = oracle_db.read_data_all(table_name)

    # 1. 기존 학습 데이터 값
    original_trained_X = pd.DataFrame(data, columns=col_X)
    # 2. pred_col_X으로 들어온 테스트 데이터 값
    # --> pred_X

    vdata = [original_trained_X, pred_X, pred_X_label, pred_X_score]
    # vdata --> [
    #   {   "length" : 2
    #       "1":   [{ "x": 22.6, "y": 76.2 },
    #               { "x": 22.8, "y": 76.5 },
    #               ...],
    #       "2":   [{ "x": 22.6, "y": 76.2 },
    #               { "x": 22.8, "y": 76.5 },
    #               ...]
    #   }
    # ]

    return vdata