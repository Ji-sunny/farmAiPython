import pandas as pd

def fielddeflog(data, table_name):
    YN = {"Y": 1, "N": 0}
    data.loc[:, "alset"]=data.loc[:, "alset"].map(YN)
    data.loc[:, "alset2"]=data.loc[:, "alset2"].map(YN)
    data.loc[:, "alset3"]=data.loc[:, "alset3"].map(YN)
    
    data.rename(columns={"member_user_id":"user_id"}, inplace=True)
    category=['user_id']
    data = pd.get_dummies(data, columns=category)
    
    #원핫 인코딩후 열 삭제
    data.drop(["ip"], axis=1, inplace=True) 
    
    data.fillna(0, inplace=True)
    
    return data