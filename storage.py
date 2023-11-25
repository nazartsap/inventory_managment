import pickle

def save_inventory(inventory, filename='inventory_data.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(inventory, file)

def load_inventory(filename='inventory_data.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None
