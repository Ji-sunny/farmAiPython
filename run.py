import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from module import main_factory, merge_table
from apscheduler.schedulers.background import BackgroundScheduler
import joblib


app = Flask(__name__)
cors = CORS(app)


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
    # 이곳 경로 model_visualize 경로와 통일


sched = BackgroundScheduler(daemon=True)
sched.add_job(create_model, 'cron', hours='0')
sched.start()


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


@app.route('/macro', methods=['GET'])
def macro():
    params = request.get_json()

    table_name = params['table_name']
    model_name = params['model_name']
    macro_name = params['macro_name']
    cols_X = params['cols_X']
    col_y = params['col_y']

    result = macro.create_macro(table_name, model_name, macro_name, cols_X, col_y)

    return jsonify(result)


@app.route('/visualize', methods=['POST'])
def visualize():
    params = request.get_json()

    macro_name = params['macro_name']
    pred_cols_X = params['pred_cols_X']

    visualized_data, score_data = macro.model_visualize(macro_name, pred_cols_X)

    visualized_data = visualized_data.to_json()

    return visualized_data, score_data


@app.route('/test', methods=['POST'])
def test():
    print("hello")
    params = json.loads(request.get_data(), encoding='utf-8')
    print(params)
    result = {"result": "success"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8082")
