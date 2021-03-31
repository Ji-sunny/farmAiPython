import pandas as pd

def plantgrowthdaygroupday(data, table_name):
    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    cate = ['day_group_id','growth_unit_id']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['site_code'], axis=1, inplace=True)
    
    data.fillna(0, inplace=True)
    return data