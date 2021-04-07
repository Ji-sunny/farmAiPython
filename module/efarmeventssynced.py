import pandas as pd

def efarmeventssynced(data, table_name):
    data.rename({'id':'efarm_events_synced_id'}, axis=1, inplace=True)
    # data.rename({'_left':"left"}, axis=1, inplace=True)
    # data.rename({'_top':"top"}, axis=1, inplace=True)
    # data.rename({'_status':"status"}, axis=1, inplace=True)
    # _로 시작하는 columns 수정

    # data['site_code'] = data['site_code'].str[9:]
    data["site_code"] = data.site_code.str.replace("SITE_FARM", '')
    data["site_code"] = pd.to_numeric(data["site_code"])
    # site_code dtype str --> numpy.int64로 수정

    # data['year'] = data['act_time'].str[0:4]
    # data['month'] = data['act_time'].str[5:7]
    # data['day'] = data['act_time'].str[8:10]
    # data['hour'] = data['act_time'].str[11:13]
    # data['minute'] = data['act_time'].str[14:16]
    # data['second'] = data['act_time'].str[17:19]

    # data['act_time'] = pd.to_datetime(data['act_time'], unit='s')
    data["act_time"] = pd.to_datetime(data["act_time"])
    data['year'] = data['act_time'].dt.year #year
    data['month'] = data['act_time'].dt.month #month
    data['day'] = data['act_time'].dt.day #day
    data['hour'] = data['act_time'].dt.hour #hour
    data['minute'] = data['act_time'].dt.minute #min
    data['second'] = data['act_time'].dt.second #sec
    # act_time dtype str --> int64로 수정

    cate=['work_type', 'status', 'device_code', 'crop_code']
    data = pd.get_dummies(data, columns=cate)

    data.drop(['work_type_ZZ','command_group', 'proto', 'regdate', 'act_time']
              , axis=1, inplace=True)

    data.fillna(0, inplace=True)

    return data