import pandas as pd
import datetime

def tbcctvpreset(data, table_name):

    map_YN = {'Y':1, 'N':0}
    arr = ['useflag', 'autosave', 'set_auto', 'do_print']
    data[arr] = data[arr].applymap(map_YN.get)

    data = data.fillna({"pan":0,"tilt":0,"zoom":0,"axisx":0,"axisy":0})

    cate = ["site_code", "presetname"]
    data = pd.get_dummies(data, columns=cate, prefix_sep='', prefix='')

    return data