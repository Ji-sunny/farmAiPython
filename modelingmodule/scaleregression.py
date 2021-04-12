from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
import math
from dbmodule import dbModule
import statsmodels.formula.api as smf
from pandas import DataFrame
import pandas as pd 
from sklearn.preprocessing import minmax_scale


oracle_db = dbModule.Database()


#다중회귀분석 
def modeling(table_name, cols_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]
    X = minmax_scale(X)
    X = pd.DataFrame(X)

    df = pd.concat([X, y], axis=1)
    df[y.name] = pd.to_numeric(df[y.name])
    print(3)
    formula = "{}~".format(y.name) + "+".join(X.columns)
    print(4)
    model = smf.ols(formula=formula, data = df).fit()
    score = None
    report = None
    return model, score, report

def visualize(model, macro_name, pred_cols_X =None):  
    


    a = str(model.params).split('\n')
    coef = [float(a[i][-8:]) for i in range(len(a)-1)]
    b = str(model.bse).split('\n')
    std_err = [float(a[i][-8:])for i in range(len(a)-1)]
    c = str(model.pvalues).split('\n')
    pvalue = [round(float(a[i][-8:]),8)for i in range(len(a)-1)]
    d = str(model.params).split('\n')
    cols_name = [str(a[i][:8]).replace(" ","") for i in range(len(a)-1)]

    result = pd.DataFrame(data={'coef': coef, 'std_err': std_err, 'pvalue': pvalue},
                     columns=['coef', 'std_err', 'pvalue'], index=cols_name)
    return result
