import pandas as pd
import time

def stnoti(data, table_name):
    time_ch = lambda x : time.strftime("%Y%m%d%H%M%S", time.localtime(int(x)))

    data['reg_date'] = data['reg_date'].map(time_ch)

    data['reg_year'] = data['reg_date'].str[0:4]
    data['reg_month'] = data['reg_date'].str[4:6]
    data['reg_day'] = data['reg_date'].str[6:8]
    data['reg_hour'] = data['reg_date'].str[8:10]
    data['reg_minute'] = data['reg_date'].str[10:12]
    data['reg_second'] = data['reg_date'].str[12:14] 

    data['send_time'] = data['send_time'].map(time_ch)

    data['send_year'] = data['send_time'].str[0:4]
    data['send_month'] = data['send_time'].str[4:6]
    data['send_day'] = data['send_time'].str[6:8]
    data['send_hour'] = data['send_time'].str[8:10]
    data['send_minute'] = data['send_time'].str[10:12]
    data['send_second'] = data['send_time'].str[12:14]

    data['send_y'] = 'Y'

    cate = ['title', 'contents']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['reg_date', 'device_key', 'user_id', 'send_time'], axis=1, inplace=True)

    return data