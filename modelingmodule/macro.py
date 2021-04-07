from modelingmodule import *
from dbmodule import dbModule
import pandas as pd
import joblib

oracle_db = dbModule.Database()


def create_macro(table_name, model_name, macro_name, cols_X, col_y):
    try:
        cols_X = ','.join(cols_X)
        macro_data = pd.DataFrame({"table_name": [table_name], "model_name": [model_name],
                                   "macro_name": [macro_name], "cols_X": [cols_X], "col_y": [col_y],
                                   "score": None})
        oracle_db.add_macro(macro_data)

        result = {"result": "success"}
        return result
    except (IndexError, SyntaxError, NameError, ZeroDivisionError, ValueError, KeyError, AttributeError,
            FileExistsError, TypeError) as e:
        result = {"result": e}
        return result


def create_model():
    macros = oracle_db.read_data_all('macro')

    # 학습
    for i in range(len(macros)):
        model_name = macros['model_name'][i]
        table_name = macros['table_name'][i]
        macro_name = macros['macro_name'][i]
        cols_X = macros['cols_X'][i]
        col_y = macros['col_y'][i]
        cols_X = [x for x in cols_X.split(',')]
        globals()[macro_name+'_model'] = getattr(getattr(modelingmodule, model_name), 'modeling')(table_name, cols_X, col_y)

    # 모델 저장
    for i in macros['macro_name']:
        joblib.dump(macro_name+'_model', 'C:/Users/COM/folder/'+macro_name+'.model')


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