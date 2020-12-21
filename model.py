import pickle
marks_model = pickle.load(open('h_m.pkl', 'rb'))

def answer(hours):
    hours=[hours]
    prediction = car_model.predict(hours)

    message ='Your estimated marks would be'
    return message
