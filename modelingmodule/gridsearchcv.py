import pandas as pd
from dbmodule import dbModule
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn import metrics


oracle_db = dbModule.Database()
#모델링이 어떻게 들어오느냐에 따라 다ㅡㄹ게 검증할 필요가 잇음 
def modeling(table_name, cols_X, col_y, model):
  
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]
    train_X, test_X, train_y, test_y = train_test_split(X, y , test_size=0.3)
    
    model_get_params = str(model.get_params)
    LR = 'LogisticRegression'
    DT = 'DecisionTreeClassifier'
    RF = 'RandomForestClassifier'
   
    if RF in model_get_params:
        params ={
            'n_estimators': [10, 100],
            'max_depth' :[8,10,12,14],
            'min_samples' :[8,12,18],
            'min_samples_split' :[8,16,20]
        }
        rf = RandomForestClassifier(random_state=0, n_jobs=1)
        model = GridSearchCV(rf, param_grid=params, cv=5, n_jobs=1)
   
    elif LR in model_get_params:
        params ={
                'max_iter': np.linspace(100, 1000, 20, endpoint=False),
                'C': np.linspace(0.1, 100, 20)
            }
        LR = LogisticRegression(random_state=1)
        model = GridSearchCV(LR, param_grid=params, cv=5, n_jobs=1)
    
    elif DT in model_get_params:
        params ={
                'max_leaf_nodes' :[10, 12,14,16,18],
                'max_depth' :[10, 12,14,16, 18],
                'min_samples_leaf' :[8,12,18],
                'min_samples_split' :[8,16,20]
            }
        DT = DecisionTreeClassifier(random_state=0)
        model = GridSearchCV(rf, param_grid=params, cv=5)
        

    model.fit(test_X, test_y)
    score = model.score(test_X, test_y)
    y_pred = model.predict(test_X)
    report = metrics.classification_report(test_y, y_pred, output_dict=True)
    report = pd.DataFrame(report).transpose()

    return model, score, report 
  