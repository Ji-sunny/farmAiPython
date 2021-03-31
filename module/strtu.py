import pandas as pd
import time

def strtu(data, table_name):
    cate = ['rtu_name']
    data = pd.get_dummies(data, columns=cate, prefix_sep='', prefix='')
    
    data['site_code'] = data['site_code'].str[9:]

    time_ch = lambda x : time.strftime("%Y%m%d%H%M%S", time.localtime(int(x)))

    data['reg_time'] = data['reg_time'].map(time_ch)

    data['reg_year'] = data['reg_time'].str[0:4]
    data['reg_month'] = data['reg_time'].str[4:6]
    data['reg_day'] = data['reg_time'].str[6:8]
    data['reg_hour'] = data['reg_time'].str[8:10]
    data['reg_minute'] = data['reg_time'].str[10:12]
    data['reg_second'] = data['reg_time'].str[12:14]

    data['update_time'] = data['update_time'].map(time_ch)

    data['update_year'] = data['update_time'].str[0:4]
    data['update_month'] = data['update_time'].str[4:6]
    data['update_day'] = data['update_time'].str[6:8]
    data['update_hour'] = data['update_time'].str[8:10]
    data['update_minute'] = data['update_time'].str[10:12]
    data['update_second'] = data['update_time'].str[12:14] 

    data.drop(['reg_time', 'update_time', 'status', 'serial_number', 'thread', 'xrtu_length', 
               'location_code', 'di_status', 'rtu_id', 'rtu_ip', 'rtu_pid'], axis=1, inplace=True)

    for i in range(1,33):
        data.drop(['ch'+str(i)+'_title','ch'+str(i)+'_fac','ch'+str(i)+'_use',
                  'ch'+str(i)+'_type','ch'+str(i)+'_loc'], axis=1, inplace=True)

    return data