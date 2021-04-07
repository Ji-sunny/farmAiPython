import pandas as pd
import time

def plantgrowthdb(data, table_name):
    site_ch = lambda x : 1 if x == 'center_1' else 0
    data['center_1'] = data['site_code'].apply(site_ch)

    for i in range(1,7):
        data['normal_'+str(i)].fillna(data['normal_'+str(i)].mean(), inplace=True)
        data['normal_plus_'+str(i)].fillna(5, inplace=True)
        data['normal_minus_'+str(i)].fillna(-5, inplace=True)

    time_ch = lambda x : time.strftime("%Y%m%d%H%M%S", time.localtime(int(x)))

    data['reg_date'] = data['reg_date'].map(time_ch)
    data["reg_date"] = pd.to_datetime(data["reg_date"])
    data["reg_year"] = data["reg_date"].dt.year
    data["reg_month"] = data["reg_date"].dt.month
    data["reg_day"] = data["reg_date"].dt.day
    data["reg_hour"] = data["reg_date"].dt.hour
    data["reg_minute"] = data["reg_date"].dt.minute
    data["reg_second"] = data["reg_date"].dt.second

    data["act_time"] = data["act_time"].map(time_ch)
    data["act_time"] = pd.to_datetime(data["act_time"])
    data["act_year"] = data["act_time"].dt.year
    data["act_month"] = data["act_time"].dt.month
    data["act_day"] = data["act_time"].dt.day
    data["act_hour"] = data["act_time"].dt.hour
    data["act_minute"] = data["act_time"].dt.minute
    data["act_second"] = data["act_time"].dt.second

    cate = ['growth_unit_id']
    data = pd.get_dummies(data, columns=cate)


    data.drop(['site_code', 'reg_date', 'act_time', 'act_time_str'],
              axis=1, inplace=True)
    for i in range(7,11):
        data.drop(['normal_'+str(i),'normal_plus_'+str(i),'normal_minus_'+str(i)], 
                  axis=1, inplace=True)
        
    data.rename(columns={"id" : "plant_growth_db_id"}, inplace=True)

    data.fillna(0, inplace=True)
    return data