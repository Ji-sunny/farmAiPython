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
import datetime
import os
from dbmodule import folder_path

oracle_db = dbModule.Database()


def modeling(table_name, cols_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X].astype(float)
    y = data[col_y]
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)
    model = DecisionTreeClassifier(criterion='entropy',
                                   max_depth=10, random_state=0)
    model.fit(train_X, train_y)
    score = model.score(test_X, test_y)
    y_pred = model.predict(test_X)
    report = metrics.classification_report(test_y, y_pred, output_dict=True)
    report = pd.DataFrame(report).transpose()
    return model, score, report


def visualize(model, macro_name, pred_cols_X=None):
    sql = "select cols_x from macro where macro_name = '{}'".format(macro_name)
    macros = oracle_db.read_sql(sql)
    x_cols = macros['cols_x'][0]
    x_cols = [x.lower() for x in x_cols.split(',')]

    def createFolder(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            pass

    path = folder_path.png_path()

    createFolder("{}".format(path))
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y%m%d')
    name = '{}_{}'.format(macro_name, nowDate)
    export_graphviz(model, out_file=path+"{}.dot".format(name), feature_names=x_cols)
    (graph,) = pydot.graph_from_dot_file(path+"{}.dot".format(name), encoding='utf8')
    graph.write_png(path+'{}.png'.format(name))

    result = path+'{}.png'.format(name)
    return result