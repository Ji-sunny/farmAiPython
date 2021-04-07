import pandas as pd

def efarmfield(data, table_name):
    data = data.loc[:, ['id', 'site_code']]
    
    # site_code 다른 table columns들과 같은 형식으로 변경(숫자만)
    data["site_code"] = data["site_code"].str.replace("SITE_FARM", '')
    data["site_code"] = pd.to_numeric(data["site_code"])

    data.rename(columns = {'id': 'efarm_device_id'}, inplace=True)
    data.fillna(0, inplace=True)

    return data