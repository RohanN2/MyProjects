import json
import pickle
import numpy as np

columns = None
location = None
model = None


def load_artifact():
    print('Loading saved artifacts...! ')
    global columns
    global location
    global model

    with open('./artifacts/columns.json', 'r') as f:
        columns = json.load(f)['data_columns']
        location = columns[3:]

    with open('./artifacts/house_prediction_model.pickle', 'rb') as f:
        model = pickle.load(f)
    print('loading saved artifacts....DONE!')


def estimated_price(location, sqft, bhk, bath):
    with open('./artifacts/columns.json', 'r') as f:
        columns = json.load(f)['data_columns']
        location = columns[3:]

    with open('./artifacts/house_prediction_model.pickle', 'rb') as f:
        model = pickle.load(f)
    try:
        loc_index = columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(columns))
    x[0] = bath
    x[1] = bhk
    x[2] = sqft

    if loc_index >= 0:
        loc_index = 1
    return(round(model.predict([x])[0], 2))



def get_location_name():
    return location




if __name__ == "__main__":
    load_artifact()
    print(get_location_name())
    print('The estimated value of given property ')
    estimated_price('1st Phase JP Nagar', 1000, 2, 2)
    estimated_price('5th Phase JP Nagar', 1000, 2, 3)
    estimated_price('1st Phase JP Nagar', 2000, 2, 4)
    estimated_price('5th Phase JP Nagar', 2000, 2, 2)
