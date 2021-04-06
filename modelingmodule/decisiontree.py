from dbmodule import dbModule
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import pandas as pd
import io
from sklearn.tree import export_graphviz
#시각화시각화
import pydot 
from IPython.core.display import Image
import matplotlib.pyplot as plt


oracle_db = dbModule.Database()

def modeling(table_name, cols_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]
    feature_names = cols_X
    train_X, test_X , train_y, test_y = train_test_split(X, y, test_size=0.3)
    model = DecisionTreeClassifier(criterion='entropy',
                                     max_depth=1, random_state=0)
    model.fit(train_X, train_y)
    scores = model.score(test_X, test_y)
    return model, scores


def visualize(model, cols_X=None, col_y=None,  pred_cols_X =None):  

    feature_names = cols_X
    dot_buf = io.StringIO()
    export_graphviz(model, out_file=dot_buf, feature_names = feature_names)
    graph = pydot.graph_from_dot_data(dot_buf.getvalue())[0]
    image = graph.create_png()
   
        
    return Image(image)