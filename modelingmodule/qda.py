# Linear/Quadratic Discriminant Analysis
# QDA(이차판별분석)
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import pandas as pd
from sklearn.preprocessing import minmax_scale

from dbmodule import dbModule

oracle_db = dbModule.Database()
# prediction은 따로 함
def qda(table_name, col_X, col_y):
    data = oracle_db.read_data_all(table_name)
    
    # oracle_db.create_modeling_table(table_name, modeling_name, visualized_data)
    # 시각화용 table 입력 필요

    X = pd.DataFrame(data, columns=col_X)
    X = data_minmax_scaled = minmax_scale(X)
    y = pd.DataFrame(data, columns=[col_y])
    y = data_minmax_scaled = minmax_scale(y)

    model = QuadraticDiscriminantAnalysis().fit(X, y)

    return model


# uses qda model & data for specific scatter visualization
def visualizeqda(table_name, col_X, col_y, pred_X):
    data = oracle_db.read_data_all(table_name)
    
    # oracle_db.create_modeling_table(table_name, modeling_name, visualized_data)
    # 시각화용 table 입력 필요

    X = pd.DataFrame(data, columns=col_X)
    X = data_minmax_scaled = minmax_scale(X)
    y = pd.DataFrame(data, columns=[col_y])
    y = data_minmax_scaled = minmax_scale(y)

    model = QuadraticDiscriminantAnalysis().fit(X, y)
    
    model.predict(pred_X)
    
    return model