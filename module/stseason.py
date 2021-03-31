import pandas as pd
import time
from dbmodule import dbModule

oracle_db = dbModule.Database()

def stseason(data, table_name):

    #시간| 전처리 

    START_year = []
    START_month = []
    START_day = []
    START_hour = []
    START_minute = []
    START_second = []

    END_year = []
    END_month = []
    END_day = []
    END_hour = []
    END_minute = []
    END_second = []

    REG_year = []
    REG_month = []
    REG_day = []
    REG_hour = []
    REG_minute = []
    REG_second = []

    
    #===AREA_ID 참조====
    data['site_code'] = data['site_code'].str[9:]
    #===================

    for i in range(len(data)):
        tm = time.localtime(data['start_date'][i])
        START_year.append(tm.tm_year)
        START_month.append(tm.tm_mon)
        START_day.append(tm.tm_mday)
        START_hour.append(tm.tm_hour)
        START_minute.append(tm.tm_min)
        START_second.append(tm.tm_sec)

    for i in range(len(data)):
        tm = time.localtime(data['end_date'][i])
        END_year.append(tm.tm_year)
        END_month.append(tm.tm_mon)
        END_day.append(tm.tm_mday)
        END_hour.append(tm.tm_hour)
        END_minute.append(tm.tm_min)
        END_second.append(tm.tm_sec)

    for i in range(len(data)):
        tm = time.localtime(data['reg_date'][i])
        REG_year.append(tm.tm_year)
        REG_month.append(tm.tm_mon)
        REG_day.append(tm.tm_mday)
        REG_hour.append(tm.tm_hour)
        REG_minute.append(tm.tm_min)
        REG_second.append(tm.tm_sec)    


    ##### 시간 변수 추가 

    data['start_year'] =START_year
    data['start_month'] =START_month
    data['start_day'] =START_day
    data['start_hour'] =START_hour
    data['start_minute'] =START_minute
    data['start_second'] =START_second

    data['end_year'] =END_year
    data['end_month'] =END_month
    data['end_day'] =END_day
    data['end_hour'] =END_hour
    data['end_minute'] =END_minute
    data['end_second'] =END_second

    data['reg_year'] =REG_year
    data['reg_month'] =REG_month
    data['reg_day'] =REG_day
    data['reg_hour'] =REG_hour
    data['reg_minute'] =REG_minute
    data['reg_second'] =REG_second

    #제거 
    data.drop(['name', 'start_date', 'end_date', 'reg_date'],axis=1, inplace=True)
    return data