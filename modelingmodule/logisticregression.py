
from dbmodule import dbModule
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np

oracle_db = dbModule.Database()


def logesticregression(table_name, cols_X, col_y, pred_cols_X):
    
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]

    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)

    # 모델 학습 
    model = LogisticRegression().fit(X, y)
    xx = np.linspace(-3, 3, X.shape[1]*X.shape[0])
    xx = xx.reshape(shape[0], shape[1])
    XX = xx[:, np.newaxis]
    XX = XX.reshape(shape[0], shape[1])
    prob = model.predict_proba(XX)[:,:shape[1]]

    # 시각화
    X_test =[pred_cols_X]
    plt.subplot(211)
    plt.bar(model.classes_, model.predict_proba(X_test)[0])
    plt.title("temp:{}, humid:{}, ec:{}, ph:{}".format(X_test[0][0],X_test[0][1],X_test[0][2],X_test[0][3]))

