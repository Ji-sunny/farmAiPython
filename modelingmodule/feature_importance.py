import pandas as pd
from dbmodule import dbModule
from sklearn.ensemble import RandomForestClassifier
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

    train_X, test_X, train_y, test_y = train_test_split(X, y , test_size=0.3)
    model = RandomForestClassifier(n_estimators=10, random_state=10)
    model.fit(train_X, train_y)
    score = model.score(test_X, test_y)
    y_pred = model.predict(test_X)
    report = metrics.classification_report(test_y, y_pred, output_dict=True)
    report = pd.DataFrame(report).transpose()
    return model, score, report



# ========================== original version ============================
def visualize(model, macro_name, pred_cols_X =None):  

    x_cols= oracle_db.read_sql("select cols_X from macro where macro_name = {}".format(macro_name))


    model.feature_importances_   
    result = pd.DataFrame(data = np.c_[x_cols,
                                 model.feature_importances_],
                      columns=['feature', 'importance'])
    result.sort_values(by='importance', ascending=False, inplace=True)
    result.reset_index(drop=True, inplace=True)
    
    return result
