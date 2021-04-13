from modelingmodule import *
import modelingmodule
from dbmodule import dbModule
import pandas as pd
import joblib
from dbmodule import folder_path

oracle_db = dbModule.Database()


def create_model():
    sql = "select * from macro where macro_name not in (select macro_name from macro_done)"
    macros = oracle_db.read_sql(sql)
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
        path = folder_path.model_path()
        joblib.dump(model, path + macro_name + '.model')
        print(model_name)
        # report json 형태로 변환
        if model_name == "regression":
            pass
        elif model_name == "scaleregression":
            pass
        else:
            report = report.reset_index().rename(columns={"index": " "})
            report = report.to_json(orient='records')

        bar = ['logisticregression', 'feature_importance']
        chart = ['rfe', 'regression', 'scaleregression']

        if model_name in bar:
            kind = 'bar'
        elif model_name in chart:
            kind = 'chart'
        else:
            kind = 'img'

        # score, report 저장
        oracle_db.modeling_done(macro_name, score, report, kind)
