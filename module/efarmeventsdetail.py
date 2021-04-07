import pandas as pd

def efarmeventsdetail(data, table_name):
    
    # data['site_code'] = data.site_code.str.split('FARM').str[1]
    data["site_code"] = data.site_code.str.replace("SITE_FARM", '')
    data["site_code"] = pd.to_numeric(data["site_code"])
    # site_code dtype str --> numpy.int64로 수정
    
    data.drop(["crop_id"], axis=1, inplace=True)
    category=['events_type']
    data.rename(columns = {'id': 'efarm_events_detail_id', 'left':'left_events_detail', 
                           'top':'top_left_events_detail'}, inplace=True)
    data = pd.get_dummies(data, columns=category, prefix_sep='', prefix='')
    
    # data.rename(columns={"_left_events_detail" : "left_events_detail"}, inplace=True)
    # data.rename(columns={"_top_left_events_detail" : "top_left_events_detail"}, inplace=True)
    # _* columns edit
    
    data.fillna(0, inplace=True)
    return data