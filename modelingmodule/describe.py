import pandas as pd
from dbmodule import dbModule
import numpy as np
oracle_db = dbModule.Database()


# =================================================================
def describe(table_name, cols_X, col_y):
    data = oracle_db.read_data_all(table_name)
    X = data[cols_X]
    y = data[col_y]

    data = pd.concat([X, y], axis=1)
    result = data.describe(include ='all')
    return result