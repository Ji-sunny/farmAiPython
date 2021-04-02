# Linear/Quadratic Discriminant Analysis
# QDA(이차판별분석)
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import pandas as pd
from sklearn.preprocessing import minmax_scale

from dbmodule import dbModule

oracle_db = dbModule.Database()

def qda(table_name, col_X, col_y):
    data = oracle_db.read_data_all(table_name)

    X = pd.DataFrame(data, columns=col_X)
    X = data_minmax_scaled = minmax_scale(X)
    y = pd.DataFrame(data, columns=[col_y])
    y = data_minmax_scaled = minmax_scale(y)

    model = QuadraticDiscriminantAnalysis()
    model.fit(X, y)
    y_pred = model.predict(X)
    
    return X, y, model, y_pred