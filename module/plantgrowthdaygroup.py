import pandas as pd

def plantgrowthdaygroup(data, table_name):
    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    cate = ['title','growth_unit_id']
    data = pd.get_dummies(data, columns=cate)


    data.drop(['site_code', 'content'], axis=1, inplace=True)
    
    data.rename(columns={"id" : "plant_growth_day_group_id"}, inplace=True)

    data.fillna(0, inplace=True)
    return data