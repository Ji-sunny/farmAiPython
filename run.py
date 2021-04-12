import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from module import main_factory, merge_table
from apscheduler.schedulers.background import BackgroundScheduler
import joblib
from modelingmodule import *
from modelingmodule import modeling
import modelingmodule
from modelingmodule.visualize_model import model_visualize
from dbmodule import dbModule


oracle_db = dbModule.Database()

app = Flask(__name__)
cors = CORS(app)


@app.route('/preprocess', methods=['GET'])
def preprocess():
    table_name = request.args.get('table')
    file_name = request.args.get('file')
    print(table_name)
    print(file_name)
    result = main_factory.preprocess_table(table_name, file_name)
    return jsonify(result)


@app.route('/mergetable', methods=['POST'])
def mergetable():
    params = request.get_json()

    table_names = params['table_names']
    sel_cols = params['sel_cols']
    stnd_cols = params['stnd_cols']

    result = merge_table.merge_table(table_names, sel_cols, stnd_cols)

    return jsonify(result)

# 로컬에 모델 저장 테스트용, 추후 스케쥴러로 뺄 것
@app.route('/run_model', methods=['POST'])
def run_model():

    modeling.create_model()

    result = "success"

    return result

# 모델링 전 변수 분석, 사전탐색
# describe, corr_pearson, corr_spearman, vif
@app.route('/pre_search', methods=['POST'])
def pre_search():
    params = request.get_json()
    print(params)
    model_name = params['model_name']
    table_name = params['table_name']
    cols_X = params['cols_X']

    # 포스트맨 테스트를 위한 스트링 리스트화, 추후 제거
    import ast
    cols_X = ast.literal_eval(cols_X)
    #

    data = getattr(getattr(modelingmodule, model_name), model_name)(table_name, cols_X)

    data = data.to_json(orient = 'records')

    return data


# 모델링 시각화 : 예측할 데이터를 받아 학습된 모델로 예측한 값 return
@app.route('/visualize', methods=['POST'])
def visualize():
    params = request.get_json()
    macro_name = params['macro_name']
    pred_cols_X = params['pred_cols_X']

    visualized_data = model_visualize(macro_name, pred_cols_X)

    visualized_data = visualized_data.to_json(orient = 'records')

    return visualized_data


@app.route('/test', methods=['POST'])
def test():
    print("hello")
    params = json.loads(request.get_data(), encoding='utf-8')
    print(params)
    result = {"result": "success"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(port="8082")
