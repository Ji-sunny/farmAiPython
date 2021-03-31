import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from module import main_factory

app = Flask(__name__)
cors = CORS(app)


@app.route('/preprocess/<table_name>', methods=['GET'])
def preprocess(table_name):
    print(table_name)
    result = main_factory.preprocess_table(table_name)
    return jsonify(result)


@app.route('/macroprocess', methods=['POST'])
def macroprocess():
    print("hello")
    params = json.loads(request.get_data(), encoding='utf-8')
    print(params)
    result = {"result": "success"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8082")
