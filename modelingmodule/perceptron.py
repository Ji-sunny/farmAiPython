import pandas as pd
import numpy as np

from dbmodule import dbModule
oracle_db = dbModule.Database()

from sklearn.linear_model import Perceptron

def perceptron(table_name, col_X, col_y):
    # ---------------------------------------------
    data = oracle_db.read_data_all(table_name)
    # data --> table_name으로 바꾸기
    # ---------------------------------------------

    # col_X : <list>
    # col_y : <string>
    # pred_cols_X : <list>
    # sel_cols -> [col_name, col_name, ...]
    
    col_X_arr = pd.DataFrame(data, columns=col_X).values
    col_y_arr = data[col_y].values
    
    model = Perceptron(max_iter=100, eta0=0.1, random_state=1).fit(col_X_arr, col_y_arr)
    
    col_X_arr = pd.DataFrame(data, columns=col_X).values
    col_y_arr = (data[col_y].values).squeeze()
    # Humidity 20이하값의 row 전처리에서 삭제하기
    # temperature 20이하값의 row 전처리에서 삭제하기

    # 추측해보려는 전처리된 데이터 값은 pred_cols_X 임
    # X, y = perceptron_single_col(data, col_X=col_X, col_y=col_y, pred_cols_X=pred_cols_X)
    model = Perceptron(max_iter=1000, eta0=0.1, random_state=1).fit(col_X_arr, col_y_arr)

    XX_min, XX_max = col_X_arr[:, 0].min()-1, col_X_arr[:, 0].max()+1
    YY_min, YY_max = col_X_arr[:, 1].min()-1, col_X_arr[:, 1].max()+1

    XX, YY = np.meshgrid(np.linspace(XX_min, XX_max, 1000), np.linspace(YY_min, YY_max, 1000))

    ZZ = model.predict(np.c_[XX.ravel(), YY.ravel()]).reshape(XX.shape)

    # import matplotlib.pyplot as plt
    # # %matplotlib inline

    # plt.contour(XX, YY, ZZ, colors='k')
    # plt.scatter(col_X_arr[:, 0], col_X_arr[:, 1], c=col_y_arr, s=30, linewidth=1)

    # idx = [20, 30, 40]
    # for i in idx:
    #     plt.annotate(i, xy=(col_X_arr[i,0], col_X_arr[i,1]+0.1))
    # plt.grid(True)
    # plt.title("Perceptron Discriminant Area")
    # plt.xlabel("x1")
    # plt.ylabel("y1")
    # plt.xlim(10,40)
    # plt.ylim(20,90)
    # plt.show()

    return model, XX_min, XX_max, YY_min, YY_max, XX, YY, ZZ

# perceptron_Modified(data)