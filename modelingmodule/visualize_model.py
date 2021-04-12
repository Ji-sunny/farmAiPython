from dbmodule import dbModule
import joblib
import modelingmodule
from modelingmodule import *

oracle_db = dbModule.Database()

def model_visualize(macro_name, pred_cols_X):
    # 포스트맨 테스트를 위한 스트링 리스트화, 추후 제거
    import ast
    pred_cols_X = ast.literal_eval(pred_cols_X)

    model_name = oracle_db.read_sql("select model_name from macro where macro_name = '{}'".format(macro_name))

    model_name = model_name['model_name'][0]
    model = joblib.load('C:/Users/COM/folder/'+macro_name+'.model')
    # 시각화 정보 받기
    visualized_data = getattr(getattr(modelingmodule, model_name), 'visualize')(model, macro_name, pred_cols_X)


    return visualized_data