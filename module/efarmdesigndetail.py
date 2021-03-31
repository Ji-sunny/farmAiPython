import pandas as pd

def efarmdesigndetail(data, table_name):
    # 경로 필요
    base = os.getcwd() #현재 파일의 경로
    filepath_ = os.path.join(base, 'data', 'sunchang', 'db')   #db의 파일 경로
    folder_names=os.listdir(filepath_)   #db에 폴더이름 들어간다
    file_list = os.listdir(filepath_ + "/"+folder_names[0]) #첫번째 db_날짜의 파일 리스트
    fname = fname+'.csv'
    efarm = os.path.join(filepath_,folder_names[0], fname) 
    data = pd.read_csv(efarm, encoding='UTF-8',header=0)
    #
    
    data["date"] = folder_names[0].split('_')[1]  #data열 추가
    data['site_code'] = data.site_code.str.split('FARM').str[1]
    #날짜 0과 NaN값 삭제
    change_ = {0.0 : np.NaN }
    data = data.replace({'work_date': change_})
    data.dropna(subset=['work_date'],inplace=True)
    data['work_date'] = pd.to_datetime(data['work_date'], unit='s')
    data['year'] = data['work_date'].dt.year #year
    data['month'] = data['work_date'].dt.month #month
    data['day'] = data['work_date'].dt.day #day
    data['hour'] = data['work_date'].dt.hour #hour
    data['minute'] = data['work_date'].dt.minute #min
    data['second'] = data['work_date'].dt.second #sec
    category=['object_type']
    data = pd.get_dummies(data, columns=category, prefix_sep='', prefix='')
    data.drop(["work_date"], axis=1, inplace=True) 
    
    data.fillna(0, inplace=True)
    return data