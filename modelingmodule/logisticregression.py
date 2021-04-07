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
    model = LogisticRegression(max_iter=5000).fit(train_X,train_y)
    score = model.score(test_X, test_y)
    y_pred = model.predict(test_X)
    report = metrics.classification_report(test_y, y_pred, output_dict=True)
    report = pd.DataFrame(report).transpose()
    return model, score, report



# ========================== original version ============================

def visualize(model, pred_cols_X):

    
    xx = np.linspace(-1, 1, X.shape[1]*X.shape[0])
    xx = xx.reshape(X.shape[0], X.shape[1])
    XX = xx[:, np.newaxis]
    XX = XX.reshape(X.shape[0], X.shape[1])
    prob = model.predict_proba(XX)[:,:X.shape[1]]
    
    
    pred_X =[pred_cols_X]
    result = model.classes_, model.predict_proba(pred_X)[0]
    return  result