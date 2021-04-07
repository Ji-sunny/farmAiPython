from sqlalchemy import create_engine

def conn():
    conn = create_engine('oracle+cx_oracle://hr:hr@localhost:1521/xe')

    return conn