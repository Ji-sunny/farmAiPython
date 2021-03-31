import pandas as pd
import time

def stevent(data, table_name):
    
    data['site_code'] = data['site_code'].str[9:]
    
    year = []
    month = []
    day = []
    hour = []
    minute = []
    second = []
    for i in range(len(data)):
        tm = time.localtime(data['event_time'][i])
        year.append(tm.tm_year)
        month.append(tm.tm_mon)
        day.append(tm.tm_mday)
        hour.append(tm.tm_hour)
        minute.append(tm.tm_min)
        second.append(tm.tm_sec)

    #EVENT_MSG
    category = ['event_msg']
    dummy0 = pd.get_dummies(data.event_msg.str.split(' ').str[0], columns=category)
    dummy1 = pd.get_dummies(data.event_msg.str.split(' ').str[1], columns=category)
    dummy = pd.concat([dummy0, dummy1], axis=1)
    dummy.columns =['robot', 'sensor1', 'sensor6', 'sensor9', 'event_msg_2_', 'event_msg_2_대기습도', 'event_msg_2_대기온도', 
                    'event_msg_2_명령실패', 'event_msg_2_수분센서', 'event_msg_2_지온센서', 'event_msg_2_통신이상']    
    data = pd.concat([data, dummy], axis=1)


    #수정
    #FREE_Y
    data.replace({'free_y': 'N'}, 0, inplace =True)
    data.replace({'free_y': 'Y'}, 1, inplace =True)

    #SEND_Y
    data['send_y'].fillna('N')
    data.replace({'send_y': 'N'}, 0, inplace =True)

    data['year'] =year
    data['month'] =month
    data['day'] =day
    data['hour'] =hour
    data['minute'] =minute
    data['second'] =second

    #제거 
    data.drop(['event_type', 'event_msg', 'event_time', 'free_time', 'send_time', 'memo1', 'memo2', 'memo_member',
                       'memo_y', 'memo_time', 'modify_time', 'end_time','status', 'vtype', 'memo_user_id', 'send_free_y', 'send_free_time',
                       'sync_event_y','sync_event_time', 'sync_event_free_y', 'sync_event_free_time', 'sync_memo_y', 'sync_memo_time',
                      'sync_memo_modify_y', 'sync_memo_modify_time'], axis=1, inplace=True)

    return data
