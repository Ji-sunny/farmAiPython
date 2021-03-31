import pandas as pd

def efarmschedule(data, table_name):
    data['is_start'] = data['is_start'].map({'Y':1, 'N':0})

    run = lambda x : 1 if '즉시실행' in str(x) else 0
    sche = lambda x : 1 if '스케줄' in str(x) else 0
    data['즉시실행'] = data['name'].apply(run)

    data['스케줄'] = data['name'].apply(sche)

    data.rename({'id':'efarm_schedule_id'}, axis=1, inplace=True)

    data = data[['is_start','즉시실행','스케줄', 'efarm_schedule_id']]

    data.fillna(0, inplace=True)

    return data