import pandas as pd

def efarmeventssynced(data, table_name):
    data.rename({'id':'efarm_events_synced_id'}, axis=1, inplace=True)
    data['site_code'] = data['site_code'].str[9:]
    data['year'] = data['act_time'].str[0:4]
    data['month'] = data['act_time'].str[5:7]
    data['day'] = data['act_time'].str[8:10]
    data['hour'] = data['act_time'].str[11:13]
    data['minute'] = data['act_time'].str[14:16]
    data['second'] = data['act_time'].str[17:19]

    cate=['work_type', 'status', 'device_code', 'crop_code']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['work_type_ZZ','command_group', 'proto', 'regdate', 'act_time']
              , axis=1, inplace=True)

    data.fillna(0, inplace=True)

    return data