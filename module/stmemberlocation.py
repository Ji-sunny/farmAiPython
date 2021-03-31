import pandas as pd

def stmemberlocation(data, table_name):

    #===AREA_ID 참조====
    data['site_code'] = data['site_code'].str[9:]
    #===================

    return data
   