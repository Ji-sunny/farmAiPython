import pandas as pd

def  stfacilitiescode(data, table_name):

    data['site_code'] = data['site_code'].str[9:]

    dummy = pd.get_dummies(data.name)
    data.reset_index(drop=True, inplace=True)
    data = pd.concat([data, dummy], axis=1)

    data.drop(['name'], axis=1, inplace=True)
        
    return data