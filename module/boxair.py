import pandas as pd
import datetime


def boxair(data, table_name):
    def AddDays(sourceDate, count):
        targetDate = sourceDate + datetime.timedelta(days=count)
        return targetDate

    def GetWeekLastDate(sourceDate):
        temporaryDate = datetime.datetime(sourceDate.year, sourceDate.month, sourceDate.day)
        weekDayCount = temporaryDate.weekday()
        targetDate = AddDays(sourceDate, -weekDayCount + 6);
        return targetDate

    # 열이름 소문자로 사용 (설계서에서는 DT지만 코드는 dt로)
    data['dt'] = data['dt'].map(lambda x: str(x).split(' ')[0])
    data['dt'] = pd.to_datetime(data['dt'])
    data['dt'] = data['dt'].map(lambda x: GetWeekLastDate(x))

    # filename에서 사용하던 정보 data['files_name']에서 받아오기
    data['box_num'] = data['files_name'].map(lambda x: x.split('_')[1])
    data['bed'] = data['box_num'].map(lambda x: 0 if int(x) > 6 else 1)
    data['farmbot'] = data['box_num'].map(lambda x: 1 if int(x) > 6 else 0)

    data.drop({'s_n', 'idx', 'type'}, axis=1, inplace=True)

    data.fillna(0, inplace=True)
    return data
