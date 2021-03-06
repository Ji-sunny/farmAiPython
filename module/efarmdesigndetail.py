import pandas as pd
import numpy as np

def efarmdesigndetail(data, table_name):
    # 경로 필요
#    base = os.getcwd() #현재 파일의 경로
#    filepath_ = os.path.join(base, 'data', 'sunchang', 'db')   #db의 파일 경로
#    folder_names=os.listdir(filepath_)   #db에 폴더이름 들어간다
#    file_list = os.listdir(filepath_ + "/"+folder_names[0]) #첫번째 db_날짜의 파일 리스트
#    fname = fname+'.csv'
#    efarm = os.path.join(filepath_,folder_names[0], fname)
#    data = pd.read_csv(efarm, encoding='UTF-8',header=0)
#    data["date"] = folder_names[0].split('_')[1]  # data열 추가
    #
    data["site_code"] = data.site_code.str.replace("SITE_FARM", '')
    data["site_code"] = pd.to_numeric(data["site_code"])
    # site_code dtype str --> numpy.int64로 수정

    #날짜 0과 NaN값 삭제
    change_ = {"0" : np.NaN}
    # 0: np.NaN --> "0": np.NaN으로 수정해줘야 0값이 NaN으로 바뀜
    # --> DB에서는 모든 값들을 VARCHAR2로 설정하기 때문에 모두 str값으로 들어옴
    data = data.replace({'work_date': change_})
    data.dropna(subset=['work_date'], inplace=True)
    category = ['object_type']
    data = pd.get_dummies(data, columns=category, prefix_sep='', prefix='')
    # column 순서 수정

    data['work_date'] = pd.to_datetime(data['work_date'], unit="s")
    # unit은 's'면 적용이 안되고, "s" 쌍따옴표로 바꿔줘야 함

    data['year'] = data['work_date'].dt.year  # year
    data['month'] = data['work_date'].dt.month  # month
    data['day'] = data['work_date'].dt.day  # day
    data['hour'] = data['work_date'].dt.hour  # hour
    data['minute'] = data['work_date'].dt.minute  # min
    data['second'] = data['work_date'].dt.second  # sec
    data.drop(["work_date"], axis=1, inplace=True)

    data.rename(columns={"id": "efarm_design_detail_id"}, inplace=True)
    data.fillna(0, inplace=True)

    return data
