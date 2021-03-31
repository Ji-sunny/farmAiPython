import pandas as pd

def stmember(data, table_name):
    data = data.loc[:, ['user_id', 'user_level', 'site_code', 'use_sms', 'free_sms']]
    
    data['site_code'] = data['site_code'].str[9:]
    
    category=['user_id']
    data = pd.get_dummies(data, columns=category)
    
    return data
