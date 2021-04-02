import itertools
from dbmodule import dbModule

oracle_db = dbModule.Database()


def macro(table_names, sel_cols, stnd_cols):
    data = pd.DataFrame()

    for i, table_name in enumerate(table_names):
        globals()['data{}'.format(i)] = oracle_db.read_data_all(table_name)
        globals()['data{}'.format(i)] = globals()['data{}'.format(i)][sel_cols[i]]

    stnd_cols_list = set(itertools.chain(*stnd_cols))

    for stnd_col in stnd_cols_list:  # 기준열들["11","33","29"]
        if stnd_col in data.columns:
            pass
        else:
            # 조인하려는 테이블 종류 받기
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

    return data