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

def decisiontree(table_name, cols_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]
    feature_names = cols_X
    train_X, test_X , train_y, test_y = train_test_split(X, y, test_size=0.3)
    dt_model = DecisionTreeClassifier(criterion='entropy',
                                     max_depth=1, random_state=0)
    dt_model.fit(train_X, train_y)
    scores = dt_model.score(test_X, test_y)
    
    dot_buf = io.StringIO()
    export_graphviz(dt_model, out_file=dot_buf, feature_names = feature_names)
#     graph = pydot.graph_from_dot_data(dot_buf.getvalue())[0]
#     image = graph.create_png()
   
        
    return scores,dot_buf.getvalue()