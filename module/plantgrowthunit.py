import pandas as pd
import datetime
import time

def plantgrowthunit(data, table_name):
    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    cate = ["title"]
    data = pd.get_dummies(data, columns=cate, prefix_sep='', prefix='')

    time_ch = lambda x : time.strftime("%Y%m%d%H%M%S", time.localtime(int(x)))

    data['reg_date'] = data['reg_date'].map(time_ch)

    data['reg_year'] = data['reg_date'].str[0:4]
    data['reg_month'] = data['reg_date'].str[4:6]
    data['reg_day'] = data['reg_date'].str[6:8]
    data['reg_hour'] = data['reg_date'].str[8:10]
    data['reg_minute'] = data['reg_date'].str[10:12]
    data['reg_second'] = data['reg_date'].str[12:14]

    data.drop(['reg_date', 'site_code'], axis=1, inplace=True)
    
    data.fillna(0, inplace=True)
    return data