import pandas as pd

def efarmfield(data, table_name):
    data = data.loc[:, ['id', "efarm_device_id", 'site_code']]
    
    # site_code 다른 table columns들과 같은 형식으로 변경(숫자만)
    data["site_code"] = data["site_code"].str.replace("SITE_FARM", '')
    data["site_code"] = pd.to_numeric(data["site_code"])
    
    data.rename(columns = {'id': 'efarm_field_id'}, inplace=True)
    # 해당 csv 파일의 id는 efarm_device_id
    # --> efarm_field_id로 (efarm_device_id는 이미 들어가 있는 내용을 사용)
    data.fillna(0, inplace=True)

    return data