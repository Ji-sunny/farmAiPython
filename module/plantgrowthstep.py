import pandas as pd

def plantgrowthstep(data, table_name):

    light = lambda x : 1 if '조명24시간(on)' in str(x) else 0
    hum = lambda x : 1 if '물에 잠기도록' in str(x) else 0
    temp = lambda x : 1 if '온도' in str(x) else 0
    data['조명24시간'] = data['content'].apply(light)
    data['습도'] = data['content'].apply(hum)
    data['온도변화'] = data['content'].apply(temp)

    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    cate = ['growth_day_id', 'growth_unit_id', 'growth_time_id']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['site_code', 'content', 'title'], axis=1, inplace=True)
    
    data.rename(columns={"id" : "plant_growth_step_id"}, inplace=True)

    data.fillna(0, inplace=True)
    return data