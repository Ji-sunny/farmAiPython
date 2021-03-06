from scipy.stats.stats import spearmanr
from scipy.stats.stats import pearsonr
from sklearn.model_selection import train_test_split
from scipy import stats
from statsmodels.formula.api import ols
from dbmodule import dbModule


oracle_db = dbModule.Database()

def corr_spearman(table_name, cols_X):
    data = oracle_db.read_data_all(table_name)

    data = data[cols_X].astype(float)
    data = data.corr(method='spearman')
    result = data.reset_index().rename(columns={"index":" "})

    return result