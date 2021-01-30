import pickle

if __name__ == '__main__':
    with open('pkl_model.pkl', 'rb') as file:
        data = pickle.load(file)
        print(data)
