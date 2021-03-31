import pandas as pd

def stsiteinfo(data, table_name):
    data.drop(['loader_in_ip', 'loader_in_port', 'loader_in_mask', 'loader_out_ip', 'loader_out_port', 
                     'loader_length', 'loader_cmd', 'loader_debug', 'usee', 'site_state', 'do_magic', 'is_center', 'is_hub_center'], axis=1, inplace=True)
    
    return data