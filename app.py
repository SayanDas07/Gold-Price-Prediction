import numpy as np
import pickle

loaded_model = pickle.load(open('M:/gold-price-prediction/trained_model.sav', 'rb'))


input = (1447.160034, 78.470001, 15.18, 1.5)

array = np.asanyarray(input)

array1 = array.reshape(1, -1)

print("Model loaded successfully and prediction is done!")
print("Prediction is: ", loaded_model.predict(array1))