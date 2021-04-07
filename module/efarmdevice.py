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
    
    # data['site_code'] = data.site_code.str.split('FARM').str[1]
    data["site_code"] = data.site_code.str.replace("SITE_FARM", "")
    data["site_code"] = pd.to_numeric(data["site_code"])
    # site_code dtype str --> numpy.int64로 수정

    data['device_code'] = data['device_code'].str.replace('D', '')
    data["device_code"] = pd.to_numeric(data["device_code"])
    # device_code dtype str --> numpy.int64로 수정

    data['test2']  = data['name'].map(lambda x : korean_(x)[0])
    data['name']=data.name.str.extract('(\d+)')

    data["name"] = pd.to_numeric(data["name"])
    # name dtype str --> numpy.int64로 수정

    data['test2']  = data['test2'].map(lambda x : origin_(x))  #origin 열
    data.rename(columns={"test2" : "origin"}, inplace=True)

    data.rename(columns={"id" : "efarm_device_id"}, inplace=True)
    # id는 고유 efarm_device_id로 변경.

    # data.rename(columns={"_width" : "width"}, inplace=True)
    # data.rename(columns={"_height" : "height"}, inplace=True)
    # data.rename(columns={"_width_all" : "width_all"}, inplace=True)
    # data.rename(columns={"_height_all" : "height_all"}, inplace=True)
    # # _로 시작하는 columns _ 삭제.
    category=['type']
    data = pd.get_dummies(data, columns=category, prefix_sep='', prefix='')
    
    data.fillna(0, inplace=True)
    return data