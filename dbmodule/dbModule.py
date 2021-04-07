from sqlalchemy import types, create_engine
import pandas as pd
from dbmodule import conn

conn = conn.conn()


class Database():
    def __init__(self):
        self.pd = pd

    def read_data(self, table_name, files_name):
        sql = "select * from {} where files_name = '{}'".format(table_name, files_name)
        data = self.pd.read_sql(sql, conn)
        # data 열이름 소문자처리
        data.columns = data.columns.str.lower()
        return data

    def read_data_all(self, table_name):
        data = self.pd.read_sql_table(table_name, conn)
        return data

    def create_data(self, data, new_table_name):
        # 새로운 테이블에 저장
        cols = data.columns
        type_dict = {}
        for col in cols:
            if type(data[col][0]) == str:
                type_dict[col] = types.VARCHAR(50)
        data.to_sql(new_table_name, conn, if_exists='append', index=False, dtype=type_dict)

    def read_macro(self, macro_name):
        sql = "select * from macro where macro_name = '{}'".format(macro_name)
        macro_data = pd.read_sql(sql, conn)
        return macro_data

    def add_score(self, macro_name, score, report):
        print(1)
        data = pd.DataFrame({'macro_name':macro_name, 'score':score, 'report':report}, index=[0])
        data.to_sql('scores', conn, if_exists='append', index=False, dtype=types.VARCHAR(50))

    def visualize(self, table_name, model_name, visualized_data):
        visualized_data.to_sql(table_name + '_' + model_name, conn, if_exists='append', index=False)

    def set_storage(self, new_files_name, new_table_name):

        names = pd.DataFrame(data={'tables_name':new_table_name, 'files_name':new_files_name}, index=[0])

        names.to_sql('file_storage', conn, if_exists='append', index=False)

        conn.execute("alter table {} add foreign key (files_name) references file_storage(files_name) on delete cascade".format(new_table_name))

    def read_sql(self, sql):
        data = pd.read_sql(sql, conn)

        return data