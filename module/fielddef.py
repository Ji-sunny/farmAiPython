import pandas as pd

def fielddef(data, table_name):
    data = data.loc[:, ['id', 'areaid', 'tag_dis', 'alset', 'allow', 'almax', 'usee', 'location_code',
                        'facilities_code', 'alset2', 'allow2', 'almax2', 'alset3', 
                        'allow3', 'almax3', 'vtype']]
    YN = {"Y": 1, "N": 0}
    data.loc[:, "usee"]=data.loc[:, "usee"].map(YN)
    data.loc[:, "alset2"]=data.loc[:, "alset2"].map(YN)
    data.loc[:, "alset3"]=data.loc[:, "alset3"].map(YN)
    
    #원핫인코딩
    data['tag_dis_1'] = data.tag_dis.str.split(' ').str[0]
    data['tag_dis_2'] = data.tag_dis.str.split(' ').str[1]
    category=['tag_dis_1', 'tag_dis_2']
    data = pd.get_dummies(data, columns=category)
    
    #원핫 인코딩후 열 삭제
    data.drop(["tag_dis"], axis=1, inplace=True) 
    
    data.rename(columns={"id" : "field_def_id"}, inplace=True)
    # id --> field_def_id 고유 식별자로 변경
    
    data.fillna(0, inplace=True)
    return data