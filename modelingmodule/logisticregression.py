import pandas as pd
from dbmodule import dbModule
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import metrics
oracle_db = dbModule.Database()

# ========================= returns model only ===============================
def modeling(table_name, cols_X, col_y):

    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]

    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)

    # 모델 학습 
    model = LogisticRegression(max_iter=10000).fit(train_X,train_y)
    score = model.score(test_X, test_y)
    y_pred = model.predict(test_X)
    report = metrics.classification_report(test_y, y_pred, output_dict=True)
    report = pd.DataFrame(report).transpose()
    return model, score, report 

# ========================== original version ============================

def visualize(model, macro_name, pred_cols_X = None ):  

    x_cols= oracle_db.read_sql("select cols_X from macro where macro_name = {}".format(macro_name))

    xx = np.linspace(-1, 1, model.n_features_in_*model.max_iter)
    xx = xx.reshape(model.max_iter, model.n_features_in_)
    XX = xx[:, np.newaxis]
    XX = XX.reshape(model.max_iter, model.n_features_in_)
    prob = model.predict_proba(XX)[:,: model.n_features_in_]
    pred_X =[pred_cols_X]
    result = pd.DataFrame(data =  model.predict_proba(x_cols)[0],
                  columns=['predict'], index=model.classes_)
    return result