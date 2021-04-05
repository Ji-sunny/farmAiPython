from modelingmodule import *
from dbmodule import dbModule
import pandas as pd

oracle_db = dbModule.Database()


def create_macro(table_name, model_name, macro_name, cols_X, col_y):
    cols_X = ','.join(cols_X)
    macro_data = pd.DataFrame({"table_name": [table_name], "model_name": [model_name],
                         "macro_name": [macro_name], "cols_X": [cols_X], "col_y": [col_y]})
    oracle_db.add_macro(macro_data)


import joblib


def create_model():
    macros = oracle_db.read_data_all('macro')

    # 학습
    for i in range(len(macros)):
        globals()[macro_name+'_model'] = getattr(getattr(modelingmodule, model_name), 'modeling')(table_name, cols_X, col_y)

    # 모델 저장
    for i in macros['macro_name']:
        joblib.dump(macro_name+'_model', '/C:/'+macro_name+'.model')


def model_visualize(macro_name, pred_cols_X):
    macro_data = oracle_db.read_macro(macro_name)
    model_name = macro_data['model_name'][0]

    model = joblib.load('/C:/'+macro_name+'.model')

    # 시각화 정보 받기
    visualized_data = getattr(getattr(modelingmodule, model_name), 'visualize')(model, pred_cols_X)

    # 모형평가
    score_data = '짱이야'

    return visualized_data, score_data