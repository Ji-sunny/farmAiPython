import pandas as pd

def plantgrowthtimegrouptime(data, table_name):
    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    cate = ["growth_unit_id"]
    data = pd.get_dummies(data, columns=cate, prefix_sep='', prefix='')

    data.drop('site_code', axis=1, inplace=True)

    data.rename({'14':'참송이생장DB_14', '19':'딸기생장DB_19',
                 '23':'파프리카생장DB_23', '24':'토마토생장DB_24'},
                axis=1, inplace=True)
    
    data.fillna(0, inplace=True)

    data.rename(columns={"id" : "plant_growth_time_grouptime_id"}, inplace=True)
    return data