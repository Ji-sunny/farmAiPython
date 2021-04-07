import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from module import main_factory, merge_table
from apscheduler.schedulers.background import BackgroundScheduler
import joblib
from modelingmodule import *
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


@app.route('/visualize', methods=['POST'])
def visualize():
    params = request.get_json()

    macro_name = params['macro_name']
    pred_cols_X = params['pred_cols_X']

    visualized_data, score_data = model_visualize(macro_name, pred_cols_X)

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
    app.run(port="8082")
