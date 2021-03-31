import pandas as pd

def farmingbox(data, table_name):
    # data       : data called from Database
    # table_name : called Database table name

    data.drop("empty", axis=1, inplace=True)

    data.drop("files_name", axis=1, inplace=True)

    data["year"] = data.DATE.str.split('-').str[0]
    data["month"] = data.DATE.str.split('-').str[1]
    data["day"] = data.DATE.str.split('-').str[2].str.split(' ').str[0]
    data["hour"] = data.DATE.str.split(' ').str[1].str.split(':').str[0]
    data["minute"] = data.DATE.str.split(' ').str[1].str.split(':').str[1]
    data["second"] = data.DATE.str.split(' ').str[1].str.split(':').str[2]
    
    data["name1"] = data.name.str.split("_").str[0]
    data["name2"] = data.name.str.split("_").str[1]
    data["name3"] = data.name.str.split("_").str[2]
    
    data["1F"] = 0
    data["2F"] = 0
    data["20%"] = 0
    data["30%"] = 0
    data["50%"] = 0
    data["1"] = 0
    data["2"] = 0
    data["3"] = 0
    data["4"] = 0
    data["5"] = 0
    data["B1"] = 0
    data["B2"] = 0
    data["B3"] = 0
    data["B4"] = 0
    data["B5"] = 0
    data["W1"] = 0
    data["W2"] = 0
    data["W3"] = 0
    data["W4"] = 0
    data["W5"] = 0
    testindexes = data[data["name1"]=="Test"].index
    if len(testindexes):
        for testindex in testindexes:
            data.drop(testindex, axis=0, inplace=True)
        
    co2indexes = data[data["name2"]=="CO2"].index
    if len(co2indexes):
        for co2index in co2indexes:
            data.drop(co2index, axis=0, inplace=True)
        
    fbindexes = data[data["name3"]=="FB"].index
    if len(fbindexes):
        for fbindex in fbindexes:
            data.drop(fbindex, axis=0, inplace=True)
    
    for index, decide in enumerate(data["name1"]=="1F"):
        if decide:
            data["1F"][index] = 1
    for index, decide in enumerate(data["name1"]=="2F"):
        if decide:
            data["2F"][index] = 1
    for index, decide in enumerate(data["name2"]=="20%"):
        if decide:
            data["20%"][index] = 1
    for index, decide in enumerate(data["name2"]=="30%"):
        if decide:
            data["30%"][index] = 1
    for index, decide in enumerate(data["name2"]=="50%"):
        if decide:
            data["50%"][index] = 1
    for index, decide in enumerate(data["name3"]=="1"):
        if decide:
            data["1"][index] = 1
    for index, decide in enumerate(data["name3"]=="2"):
        if decide:
            data["2"][index] = 1
    for index, decide in enumerate(data["name3"]=="3"):
        if decide:
            data["3"][index] = 1
    for index, decide in enumerate(data["name3"]=="4"):
        if decide:
            data["4"][index] = 1
    for index, decide in enumerate(data["name3"]=="5"):
        if decide:
            data["5"][index] = 1
    for index, decide in enumerate(data["name3"]=="B1"):
        if decide:
            data["B1"][index] = 1
    for index, decide in enumerate(data["name3"]=="B2"):
        if decide:
            data["B2"][index] = 1
    for index, decide in enumerate(data["name3"]=="B3"):
        if decide:
            data["B3"][index] = 1
    for index, decide in enumerate(data["name3"]=="B4"):
        if decide:
            data["B4"][index] = 1
    for index, decide in enumerate(data["name3"]=="B5"):
        if decide:
            data["B5"][index] = 1
    for index, decide in enumerate(data["name3"]=="W1"):
        if decide:
            data["W1"][index] = 1
    for index, decide in enumerate(data["name3"]=="W2"):
        if decide:
            data["W2"][index] = 1
    for index, decide in enumerate(data["name3"]=="W3"):
        if decide:
            data["W3"][index] = 1
    for index, decide in enumerate(data["name3"]=="W4"):
        if decide:
            data["W4"][index] = 1
    for index, decide in enumerate(data["name3"]=="W5"):
        if decide:
            data["W5"][index] = 1    

    data.drop("name", axis=1, inplace=True)
    data.drop("name1", axis=1, inplace=True)
    data.drop("name2", axis=1, inplace=True)
    data.drop("name3", axis=1, inplace=True)
    data.drop("DATE", axis=1, inplace=True)
    
    data.fillna(0, inplace=True)
    return data