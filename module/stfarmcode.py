import pandas as pd

def st_farm_code(data, table_name):

    dummy = pd.get_dummies(data.name)
    data.reset_index(drop=True, inplace=True)
    data =pd.concat([data, dummy],axis=1)

    return data
