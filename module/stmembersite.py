import pandas as pd
import time

def stmembersite(data, table_name):
   
    REG_year = []
    REG_month = []
    REG_day = []
    REG_hour = []
    REG_minute = []
    REG_second = []
    for i in range(len(data)):
        tm = time.localtime(data['reg_time'][i])
        REG_year.append(tm.tm_year)
        REG_month.append(tm.tm_mon)
        REG_day.append(tm.tm_mday)
        REG_hour.append(tm.tm_hour)
        REG_minute.append(tm.tm_min)
        REG_second.append(tm.tm_sec)    


    #===AREA_ID 참조====
    data['site_code'] = data['site_code'].str[9:]
    #===================
    ##### 시간 변수 추가 


    data['regyear'] =REG_year
    data['regmonth'] =REG_month
    data['regday'] =REG_day
    data['reghour'] =REG_hour
    data['regminute'] =REG_minute
    data['regsecond'] =REG_second

    a=list(data.columns)
    cols = [i.replace("_","") for i in a]
    cols = [i.replace(" ","") for i in cols]

    #제거 
    data.drop(['user_id', 'reg_time', 'flag'],axis=1, inplace=True)
    
    return data 
