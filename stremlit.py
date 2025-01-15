import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('M:/gold-price-prediction/trained_model.sav', 'rb'))

def gold_price_prediction(input_data):
    
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    return f' Prediction value of Gold is : {prediction[0]}'
  

def main():

    st.title('Gold price Prediction Web App')
 
    
    
    SPX = st.text_input('SPX index value')
    USO = st.text_input('USO index value')
    SLV = st.text_input('iShares Silver Trust index value')
    EUR_USD = st.text_input('euro against the U.S. dollar pair, EUR/USD')

    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Predict Gold Price'):
        diagnosis = gold_price_prediction([SPX, USO, SLV, EUR_USD])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    