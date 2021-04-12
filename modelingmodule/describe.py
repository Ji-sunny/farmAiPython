import pandas as pd
from dbmodule import dbModule
import numpy as np
oracle_db = dbModule.Database()


# =================================================================
def describe(table_name, cols_X):
    data = oracle_db.read_data_all(table_name)

    data = data[cols_X].astype(float)
    data = data.describe(include ='all')
    result = data.reset_index().rename(columns={"index": " "})
    return result