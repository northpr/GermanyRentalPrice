import json
import pickle
import numpy as np

__heattype = None
__roomcon = None
__flattype = None
__locations = None


__data_columns = None
__model = None

def get_estimated_price(livingSpace,noRooms,additionCost,heating_type,condition,typeOfFlat,regio2):
    try:
        heatingIndex = __data_columns.index(heating_type.lower())
        conIndex = __data_columns.index(condition.lower())
        flatTypeIndex = __data_columns.index(typeOfFlat.lower())
        regionIndex = __data_columns.index(regio2.lower())
    except:
        heatingIndex = -1
        conIndex = -1
        flatTypeIndex = -1
        regionIndex = -1


    x = np.zeros(len(__data_columns))
    x[0] = livingSpace
    x[1] = noRooms
    x[2] = additionCost

    if heatingIndex >= 0:
        x[heatingIndex] = 1
    if conIndex >= 0:
        x[conIndex] = 1
    if flatTypeIndex >= 0:
        x[flatTypeIndex] = 1
    if regionIndex >= 0:
        x[regionIndex] = 1

    return round(__model.predict([x])[0],2)

def get_heattype_names():
    return __heattype

def get_roomcon_names():
    return __roomcon

def get_flattype_names():
    return __flattype

def get_location_names():
    return __locations



def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __heattype
    global __roomcon
    global __flattype
    global __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __heattype = __data_columns[8:18] 
        __roomcon = __data_columns[19:25] 
        __flattype = __data_columns[26:35] 
        __locations = __data_columns[36:]
        
    global __model
    with open("./artifacts/german_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")



if __name__ == '__main__':
    load_saved_artifacts()

    # print(f"heattype:",get_heattype_names())
    # print(f"room condition:",get_roomcon_names())
    # print(f"flattype:",get_flattype_names())
    # print(f"regio2:",get_location_names())
    print(get_estimated_price(55,4,170,'central_heating','well_kept','apartment','Berlin'))
    print(get_estimated_price(55,4,170,'central_heating','well_kept','apartment','m\u00fcnchen'))
