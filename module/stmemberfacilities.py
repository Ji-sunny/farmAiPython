import pandas as pd

def stmemberfacilities(data, table_name):
 
    data['site_code'] = data['site_code'].str[9:]
    return data 
