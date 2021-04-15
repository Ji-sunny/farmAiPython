import itertools
from dbmodule import dbModule
import pandas as pd
oracle_db = dbModule.Database()
import ast
import json

def merge_table(table_names, sel_cols, stnd_cols):
    try:
        data = pd.DataFrame()

        # table_name None값 제거
        for i in range(table_names.count(None)):
            table_names.pop()
        
        # 소문자로 변경
        for i, cols in enumerate(sel_cols):
            arr = []
            for j in cols:
                arr.append(j.lower())
            sel_cols[i] = arr
        for i, cols in enumerate(stnd_cols):
            arr = []
            for j in cols:
                arr.append(j.lower())
            stnd_cols[i] = arr


        # new_table_name 생성
        name_dict = {'BOXAIR':'BA',
                        'BOX':'B',
                        'BOXIOCROPS':'BI',
                        'EFARMDESIGN':'EDS',
                        'EFARMDESIGNDETAIL':'EDD',
                        'EFARMDEVICE':'EDV',
                        'EFARMEVENTSDETAIL':'EED',
                        'EFARMEVENTSSYNCED':'EES',
                        'EFARMFIELD':'EF',
                        'EFARMSCHEDULE':'ES',
                        'FARMINGBOX':'FBX',
                        'FIELDDEF':'FD',
                        'FIELDDEFLOG':'FDL',
                        'PLANTGROWTHDAYGROUP':'GDG',
                        'PLANTGROWTHDAYGROUPDAY':'GDGD',
                        'PLANTGROWTHDB':'GD',
                        'PLANTGROWTHDBREP':'GDR',
                        'PLANTGROWTHSENSOR':'GSR',
                        'PLANTGROWTHSTEP':'GST',
                        'PLANTGROWTHTIMEGROUP':'GTG',
                        'PLANTGROWTHTIMEGROUPTIME':'GTGT',
                        'PLANTGROWTHUNIT':'GU',
                        'SITEFARM3':'SF3',
                        'SITEFARM4':'SF4',
                        'SITEFARM5':'SF5',
                        'SITEFARM6':'SF6',
                        'SITEFARM7':'SF7',
                        'SITEFARM8':'SF8',
                        'SITEFARM9':'SF9',
                        'SITEFARM10':'SF10',
                        'SITEFARM11':'SF11',
                        'SITEFARM12':'SF12',
                        'SITEFARM13':'SF13',
                        'STEVENT':'SE',
                        'STFACILITIESCODE':'SFTC',
                        'STFARMCODE':'SFMC',
                        'STLOCATIONCODE':'SLC',
                        'STMEMBER':'SM',
                        'STMEMBERFACILITIES':'SMF',
                        'STMEMBERLOCATION':'SML',
                        'STMEMBERSITE':'SMS',
                        'STNOTI':'SN',
                        'STRTU':'SR',
                        'STSEASON':'SS',
                        'STSITEINFO':'SSI',
                        'TBCCTVIMAGE':'TCI',
                        'TBCCTVPRESET':'TCP'}

        new_table_names = []
        for i in table_names:
            new_table_names.append(i.split('_')[0])

        new_table_name = []
        for i in new_table_names:
            new_table_name.append(name_dict[i])

        new_table_name = '_'.join(new_table_name) + '_NEW'

        for i, table_name in enumerate(table_names):
            globals()['data{}'.format(i)] = oracle_db.read_data_all(table_name)
            globals()['data{}'.format(i)] = globals()['data{}'.format(i)][sel_cols[i]]
        stnd_cols_list = set(itertools.chain(*stnd_cols))

        for stnd_col in stnd_cols_list:
            if not(data.empty) & (stnd_col not in data.columns):
                stnd_cols_list.append(stnd_col)
                pass
            else:
                join_table = []
                for j in range(len(table_names)):
                    if stnd_col in stnd_cols[j]:
                        join_table.append(table_names[j])

                if data.empty:
                    data = globals()['data' + str(table_names.index(join_table[0]))]
                    for j in range(len(join_table) - 1):
                        data = pd.merge(data, globals()['data' + str(table_names.index(join_table[j + 1]))],
                                        how='left', on=stnd_col)
                else:
                    for j in range(len(join_table) - 1):
                        data = pd.merge(data, globals()['data' + str(table_names.index(join_table[j]))],
                                        how='left', on=stnd_col)

                for table_name in join_table:
                    table_names.remove(table_name)

                if len(table_names) == 0:
                    break


        data['files_name'] = new_table_name
        data.fillna(0, inplace=True)

        oracle_db.create_data(data, new_table_name)
        oracle_db.set_storage(new_table_name, new_table_name)

        result = {"result": "success"}

        return result
    except (IndexError, SyntaxError, NameError, ZeroDivisionError, ValueError, KeyError, AttributeError,
            FileExistsError, TypeError) as e:
        result = {"result": e}
        return result
