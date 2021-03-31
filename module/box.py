import pandas as pd
import datetime

def box(data, table_name):
    def AddDays(sourceDate, count):
        targetDate = sourceDate + datetime.timedelta(days = count) 
        return targetDate
    def GetWeekLastDate(sourceDate): 
        temporaryDate = datetime.datetime(sourceDate.year, sourceDate.month, sourceDate.day)
        weekDayCount = temporaryDate.weekday() 
        targetDate = AddDays(sourceDate, -weekDayCount + 6); 
        return targetDate

    data['dt'] = data['dt'].map(lambda x : x.split(' ')[0])
    data['dt'] = pd.to_datetime(data['dt'])
    data['dt'] = data['dt'].map(lambda x : GetWeekLastDate(x))

    data['box_num'] = data['files_name'].map(lambda x : x.split('_')[1])

    data.drop({'s_n','idx','type'}, axis=1, inplace=True)


    #원핫, 센서가 bed인지 farmbot인지
    data['bed'] = data['box_num'].map(lambda x : 0 if int(x) > 6 else 1)
    data['farmbot'] = data['box_num'].map(lambda x : 1 if int(x) > 6 else 0)

    data.fillna(0, inplace=True)
    return data