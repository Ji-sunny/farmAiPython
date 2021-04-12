from dbmodule import dbModule
import joblib
import modelingmodule
from modelingmodule import *

oracle_db = dbModule.Database()

def model_visualize(macro_name, pred_cols_X):
    # 포스트맨 테스트를 위한 스트링 리스트화, 추후 제거
    import ast
    pred_cols_X = ast.literal_eval(pred_cols_X)
    type(pred_cols_X)

    macro_data = oracle_db.read_macro(macro_name)
    model_name = macro_data['model_name'][0]
    cols_X = macro_data['cols_x'][0]
    col_y = macro_data['col_y'][0]
    cols_X = [x for x in cols_X.split(',')]

    model = joblib.load('C:/Users/COM/folder/'+macro_name+'.model')
    print("여긴돼")
    # 시각화 정보 받기
    visualized_data = getattr(getattr(modelingmodule, model_name), 'visualize')(model, macro_name, pred_cols_X)
    print("확인:")
    print(visualized_data)

    return visualized_data