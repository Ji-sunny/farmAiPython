import pandas as pd

def plantgrowthsensor(data, table_name):
    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    upper = lambda x : x.upper()
    data['title'] = data['title'].apply(upper)

    cate = ['title']
    data = pd.get_dummies(data, columns=cate, prefix_sep='', prefix='')

    cate = ['growth_unit_id']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['site_code', 'thread'], axis=1, inplace=True)

    return data