from modelingmodule import *
import modelingmodule
from dbmodule import dbModule
import pandas as pd
import joblib

oracle_db = dbModule.Database()


def create_model():
    macros = oracle_db.read_data_all('macro')

    # 학습
    for i in range(len(macros)):

        model_name = macros['model_name'][i].lower()
        table_name = macros['table_name'][i].lower()
        macro_name = macros['macro_name'][i].lower()
        cols_X = macros['cols_x'][i]
        col_y = macros['col_y'][i].lower()
        cols_X = [x.lower() for x in cols_X.split(',')]
        model, score, report = getattr(getattr(modelingmodule, model_name), 'modeling')(table_name, cols_X, col_y)

    # 모델 저장
    for i in macros['macro_name']:
        print(i)
        joblib.dump(model, 'C:/Users/COM/folder/'+macro_name+'.model')
    print(3)
    # report json 형태로 변환
    report = report.to_json()

    print(report)
    # score, report 저장
    oracle_db.add_score(macro_name, score, report)
