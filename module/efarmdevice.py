import pandas as pd
import re

def efarmdevice(data, table_name):
    def korean_(data):
        pattern = re.compile(r'[ㄱ-ㅣ가-힣]+')
        results = re.findall(pattern, data)    
        return results

    def origin_(data):
        if data == '기존팜봇':
            return 1
        else:
            return 0
    
    data['site_code'] = data.site_code.str.split('FARM').str[1]
    data['device_code'] = data['device_code'].str.replace('D', '')
    data['test2']  = data['name'].map(lambda x : korean_(x)[0])
    data['name']=data.name.str.extract('(\d+)')
    data['test2']  = data['test2'].map(lambda x : origin_(x))  #origin 열
    data.rename(columns={"test2" : "origin"}, inplace=True)
    category=['type']
    data = pd.get_dummies(data, columns=category, prefix_sep='', prefix='')
    
    data.fillna(0, inplace=True)
    return data