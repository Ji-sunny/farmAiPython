import pandas as pd
from dbmodule import dbModule
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.model_selection import train_test_split

oracle_db = dbModule.Database()


# ========================= returns model only ===============================
def modeling(table_name, cols_X, col_y):

    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]

    train_X, test_X, train_y, test_y = train_test_split(X, y , test_size=0.3)
    rf_model = RandomForestClassifier(n_estimators =10, random_state=10)
    model = RFE(rf_model,  n_features_to_select=int(len(X.columns)/2))
    model.fit(train_X, train_y)
    score = model.score(test_X, test_y)
    y_pred = rf_model.predict(test_X)
    report = metrics.classification_report(y_test, y_pred, output_dict=True)
    report = pd.DataFrame(report).transpose()
    return model, score, report


    return model, score



# ========================== original version ============================
def visualize(model, cols_X, col_y,  pred_cols_X =None):
    
    result = pd.DataFrame(data= np.c_[X.columns.values, rfe_model.get_support()])
    result.sort_values(by=1, ascending=False, inplace=True)
    
    return result

