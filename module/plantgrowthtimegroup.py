import pandas as pd

def plantgrowthtimegroup(data, table_name):

    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    cate = ['growth_unit_id', 'title']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['site_code', 'content'], axis=1, inplace=True)
    data.fillna(0, inplace=True)

    data.rename(columns={"growth_unit_id_14" : "참송이생장DB_14"}, inplace=True)
    data.rename(columns={"growth_unit_id_19" : "딸기생장DB_19"}, inplace=True)
    data.rename(columns={"growth_unit_id_23" : "파프리카생장DB_23"}, inplace=True)
    data.rename(columns={"growth_unit_id_24" : "토마토생장DB_24"}, inplace=True)

    data.rename(columns={"id" : "plant_growth_time_group_id"}, inplace=True)

    return data