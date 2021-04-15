import pandas as pd
from sklearn.impute import SimpleImputer
import time

def sitefarm5(data, table_name):
    col = list(data.columns)

    #결측치 처리 (pd -> np)
    imp_mean = SimpleImputer(strategy='mean')
    if "files_name" in col:
        data.drop(['files_name'], axis=1, inplace=True)
    imp_mean.fit(data)
    A=  imp_mean.transform(data)
    data = pd.DataFrame(A)

    #시간 전처리
    year = []
    month = []
    day = []
    hour = []
    minute = []
    second = []

    for i in range(len(data)):
        tm = time.localtime(data[0][i])
        year.append(tm.tm_year)
        month.append(tm.tm_mon)
        day.append(tm.tm_mday)
        hour.append(tm.tm_hour)
        minute.append(tm.tm_min)
        second.append(tm.tm_sec)

    #열삭제 
    droplist = [19, 18, 17, 16, 15, 13, 10, 9, 6, 2, 0]
    data.drop(droplist, axis=1, inplace=True)
    for i in range(len(droplist)):
        i = droplist[i]
        del col[i]

    data.columns =col
    data.head()

    #열추가
    data['year'] =year
    data['month'] =month
    data['day'] =day
    data['hour'] =hour
    data['minute'] =minute
    data['second'] =second

    return data