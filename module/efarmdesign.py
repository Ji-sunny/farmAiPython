import pandas as pd

def efarmdesign(data, table_name):
    # data['site_code'] = data.site_code.str.split('FARM').str[1]
    data["site_code"] = data.site_code.str.replace("SITE_FARM", '')
    data["site_code"] = pd.to_numeric(data["site_code"])
    # site_code dtype을 int64로 수정함
    
    data['reg_date'] = pd.to_datetime(data['reg_date'], unit='s')
    data['year'] = data['reg_date'].dt.year #year
    data['month'] = data['reg_date'].dt.month #month
    data['day'] = data['reg_date'].dt.day #day
    data['hour'] = data['reg_date'].dt.hour #hour
    data['minute'] = data['reg_date'].dt.minute #min
    data['second'] = data['reg_date'].dt.second #sec

    data.drop(["title"], axis=1, inplace=True) 
    data.drop(["reg_date"], axis=1, inplace=True) 
    
    data.rename(columns={"id" : "efarm_design_id"}, inplace=True)

    data.fillna(0, inplace=True)
    
    return data