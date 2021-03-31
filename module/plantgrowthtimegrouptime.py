import pandas as pd

def plantgrowthtimegrouptime(data, table_name):
    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    cate = ["growth_unit_id"]
    data = pd.get_dummies(data, columns=cate, prefix_sep='', prefix='')

    data.drop('site_code', axis=1, inplace=True)

    data.rename({'14':'14_참송이생장DB', '19':'19_딸기생장DB',
                 '23':'23_파프리카생장DB', '24':'24_토마토생장DB'},
                axis=1, inplace=True)
    
    data.fillna(0, inplace=True)
    return data