
from dbmodule import dbModule
import pandas as pd 
from patsy.highlevel import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

oracle_db = dbModule.Database()

def vif(table_name, cols_X):
    data = oracle_db.read_data_all(table_name)
    data = data[cols_X].astype(float)

    feature_cols = list(data.columns[:-1])
    formula = "{}~".format(data.columns[-1]) + "+".join(feature_cols) + '-1'
    y,X = dmatrices(formula, data, return_type="dataframe")
    vif = pd.DataFrame()
    vif['VIF Factor'] = [variance_inflation_factor(X.values, i)
                        for i in range(X.shape[1])]
    vif['features'] = X.columns
    vif.sort_values(by='VIF Factor', ascending=False, inplace=True)


    feature_cols = list(data.columns[:-1])
    for i in range(len(feature_cols)):
        if vif.iloc[0,0] > 10:
            vif.drop(vif.index[0], inplace=True)

        else:
            break
    result = vif
    return result
