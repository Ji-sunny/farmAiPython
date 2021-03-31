import pandas as pd

def efarmfield(data, table_name):
    data = data.loc[:, ['id', 'site_code']]
    data.rename(columns = {'id': 'efarm_device_id'}, inplace=True)
    
    data.fillna(0, inplace=True)
    return data