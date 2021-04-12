from dbmodule import dbModule
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import pandas as pd
import io
from sklearn.tree import export_graphviz
import pydot 
from IPython.core.display import Image
from sklearn.metrics import classification_report
from sklearn import metrics
from time import time
import os


oracle_db = dbModule.Database()

def modeling(table_name, cols_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]
    train_X, test_X , train_y, test_y = train_test_split(X, y, test_size=0.3)
    model = DecisionTreeClassifier(criterion='entropy',
                                     max_depth=10, random_state=0)
    model.fit(train_X, train_y)
    score = model.score(test_X, test_y)
    y_pred = model.predict(test_X)
    report = metrics.classification_report(test_y, y_pred, output_dict=True)
    report = pd.DataFrame(report).transpose()
    return model, score, report




def visualize(model, macro_name, pred_cols_X =None):  
    def createFolder(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            pass
        
    createFolder("./DecisionTree_png")

    name =time()
    export_graphviz(model, out_file="./DecisionTree_png/{}.dot".format(name),feature_names = feature_names)
    (graph, ) = pydot.graph_from_dot_file("./DecisionTree_png/{}.dot".format(name), encoding='utf8')
    graph.write_png('./DecisionTree_png/{}.png'.format(name))

    result = './DecisionTree_png/{}.png'.format(name)
    return result