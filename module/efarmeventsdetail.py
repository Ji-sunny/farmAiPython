import pandas as pd

def efarmeventsdetail(data, table_name):
    
    data['site_code'] = data['site_code'].str[9:]
    
    data.drop(["crop_id"], axis=1, inplace=True)
    category=['events_type']
    data.rename(columns = {'id': 'efarm_events_detail_id', '_left':'_left_events_detail', 
                           '_top':'_top_left_events_detail'}, inplace=True)
    data = pd.get_dummies(data, columns=category, prefix_sep='', prefix='')
    
    data.fillna(0, inplace=True)
    return data    