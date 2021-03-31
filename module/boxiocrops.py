import pandas as pd
import datetime

def boxiocrops(data, table_name):

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

    data.drop({'s_n','idx'}, axis=1, inplace=True)

    #원핫, 어느 박스인지
    data['iocrops_1_b4'] = data['box_num'].map(lambda x : 1 if x == '1' else 0)
    data['iocrops_2_5d'] = data['box_num'].map(lambda x : 1 if x == '2' else 0)
    data['iocrops_3_3f'] = data['box_num'].map(lambda x : 1 if x == '3' else 0)
    
    data.fillna(0, inplace=True)
    return data