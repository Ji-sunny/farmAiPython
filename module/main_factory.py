
from dbmodule import dbModule
import module
from module import *

oracle_db = dbModule.Database()


def preprocess_table(table_name, files_name):
    try:
        # 테이블 이름 소문자 처리
        table_name = table_name.lower()
        # data 불러오기
        data = oracle_db.read_data(table_name, files_name)

        # print("data1 : ", data)
        # data 전처리
        # (module 패키지 내에 table_name이름을 가진 모듈 내 table_name 함수 호출)
        data = getattr(getattr(module, table_name), table_name)(data, table_name)

        # files_name 변경
        data['files_name'] = files_name + '_new'

        # file_storage에 tables_name, files_name 추가
        new_table_name = table_name + '_new'
        new_files_name = files_name + '_new'

        oracle_db.set_storage(new_files_name, new_table_name)

        # 테이블이 생성된 적 있는지 체크
        table_check = oracle_db.check_table(new_table_name)

        # 전처리한 데이터 새로운 테이블에 집어넣기
        oracle_db.create_data(data, new_table_name)

        # fk, cascade 설정
        if table_check==0:
            oracle_db.set_fk(new_table_name)

        # 성공 했을 경우, 실패했을 경우 fail
        result = {"result": "success"}
        return result
    except (IndexError, SyntaxError, NameError, ZeroDivisionError, ValueError, KeyError, AttributeError,
            FileExistsError, TypeError) as e:
        result = {"result": e}
        return result
