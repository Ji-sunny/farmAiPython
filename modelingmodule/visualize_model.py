from dbmodule import dbModule
import joblib
import modelingmodule
from modelingmodule import *

oracle_db = dbModule.Database()

def model_visualize(macro_name, pred_cols_X):
    macro_data = oracle_db.read_macro(macro_name)
    model_name = macro_data['model_name'][0]
    cols_X = macro_data['cols_X'][0]
    col_y = macro_data['col_y'][0]
    cols_X = [x for x in cols_X.split(',')]

    model = joblib.load('C:/Users/COM/folder/'+macro_name+'.model')


    # 시각화 정보 받기
    visualized_data = getattr(getattr(modelingmodule, model_name), 'visualize')(model, cols_X, col_y, pred_cols_X)

    # 모형평가
    score_data = '짱이야'

    return visualized_data, score_data