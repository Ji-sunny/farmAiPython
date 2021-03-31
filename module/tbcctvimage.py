import pandas as pd
import time

def tbcctvimage(data, table_name):

    a_ch = lambda x : 1 if x == 'A' else 0
    data['category_a'] = data['category'].apply(a_ch)

    cate = ["site_code"]
    data = pd.get_dummies(data, columns=cate, prefix_sep='', prefix='')

    time_ch = lambda x : time.strftime("%Y%m%d%H%M%S", time.localtime(int(x)))

    data['registdate'] = data['registdate'].map(time_ch)

    data['regist_year'] = data['registdate'].str[0:4]
    data['regist_month'] = data['registdate'].str[4:6]
    data['regist_day'] = data['registdate'].str[6:8]
    data['regist_hour'] = data['registdate'].str[8:10]
    data['regist_minute'] = data['registdate'].str[10:12]
    data['regist_second'] = data['registdate'].str[12:14]

    data.drop(['registdate','memo','category'], axis=1, inplace=True)

    return data