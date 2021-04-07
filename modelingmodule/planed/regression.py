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
from pandas as pd 

oracle_db = dbModule.Database()


#다중회귀분석 
def modeling(table_name, col_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[col_X]
    y = data[col_y]
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)
    df = pd.concat([train_X, train_y], axis=1)
    df[y.name] = pd.to_numeric(df[y.name])
    formula = "{}~".format(train_y.name) + "+".join(train_X.columns)
    model = smf.ols(formula=formula, data = df).fit()
    score = None
    return model, score

def visualize(model, pred_cols_X =None):
    a = str(model.params).split('\n')
    coef = [float(a[i][-8:]) for i in range(len(a)-1)]
    b = str(model.bse).split('\n')
    std_err = [float(a[i][-8:])for i in range(len(a)-1)]
    c = str(model.params).split('\n')
    cols_name = [str(a[i][:8]).replace(" ","") for i in range(len(a)-1)]

    result = pd.DataFrame(data={'coef': coef, 'std_err': std_err, 'pvalue': pvalue},
                     columns=['coef', 'std_err', 'pvalue'], index=cols_name)
    return result
