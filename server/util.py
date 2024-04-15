import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, area, rooms, floor, rent, building_ownership, construction_status, outdoor, heating, car):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = rooms
    x[2] = floor
    x[3] = rent
    x[4] = building_ownership
    x[5] = construction_status
    x[6] = outdoor
    x[7] = heating
    x[8] = car
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)



def load_data():
    print('Loading data...')
    global __data_columns
    global __locations


    with open('artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[9:]
    global __model
    with open('artifacts/home_price_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading artifacts done!')

def get_data():
    return __locations

if __name__ == '__main__':
    load_data()
    print(get_data())
    print(get_estimated_price('wawer', 100, 2, 3, 1, 1, 1, 1, 1, 1))