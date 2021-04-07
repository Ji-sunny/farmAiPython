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

oracle_db = dbModule.Database()



#다중회귀분석 
def modeling(table_name, cols_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]
    df = pd.concat([X, y], axis=1)
    # OLSResult는 따로 scores평가를 하지 않기때문에 오히려 값이 많은 것이 더 좋다.
    df[y.columns[0]] = pd.to_numeric(df[y.columns[0]])
    formula = "{}~".format(y.columns[0]) + "+".join(X.columns)
    model = smf.ols(formula=formula, data = df).fit()
    score = None
    return model, score


def visualize(model, cols_X=None, col_y=None,  pred_cols_X =None):
    a = str(model.params).split('\n')ㄴ
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
