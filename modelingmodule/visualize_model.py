from dbmodule import dbModule
import joblib
import modelingmodule
from modelingmodule import *
from dbmodule import model_path

oracle_db = dbModule.Database()

def model_visualize(macro_name, pred_cols_X):

    model_name = oracle_db.read_sql("select model_name from macro where macro_name = '{}'".format(macro_name))

    model_name = model_name['model_name'][0]
    path = model_path.model_path()
    model = joblib.load(path+macro_name+'.model')
    # 시각화 정보 받기
    visualized_data = getattr(getattr(modelingmodule, model_name), 'visualize')(model, macro_name, pred_cols_X)

    return visualized_data