import pandas as pd
import time

def plantgrowthdbrep(data, table_name):
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
    
    cate = ['day_group_id', 'growth_unit_id']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['site_code', 'reg_date'],
              axis=1, inplace=True)
    for i in range(7,11):
        data.drop(['normal_'+str(i),'normal_plus_'+str(i),'normal_minus_'+str(i)], 
                  axis=1, inplace=True)
    
    data.rename(columns={"id" : "plant_growth_db_rep_id"})

    data.fillna(0, inplace=True)
    
    return data