from scipy.stats.stats import spearmanr
from scipy.stats.stats import pearsonr
from sklearn.model_selection import train_test_split
from scipy import stats
from statsmodels.formula.api import ols
from dbmodule import dbModule
from pandas import DataFrame
import pandas as pd 

oracle_db = dbModule.Database()

def corr_spearman(table_name, cols_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]
    df = pd.concat([X, y], axis=1)
    result = df.corr(method='spearman')
    return result