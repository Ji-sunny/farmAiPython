import pandas as pd

def plantgrowthtimegroup(data, table_name):

    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    cate = ['growth_unit_id', 'title']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['site_code', 'content'], axis=1, inplace=True)

    data.rename({'GROWTH_UNIT_ID_14':'14_참송이생장DB', 'GROWTH_UNIT_ID_19':'19_딸기생장DB',
                 'GROWTH_UNIT_ID_23':'23_파프리카생장DB', 'GROWTH_UNIT_ID_24':'24_토마토생장DB'},
                axis=1, inplace=True)
    
    data.fillna(0, inplace=True)

    return data