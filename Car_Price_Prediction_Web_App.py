#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 16:28:00 2025

@author: aryan
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model = pickle.load(open('/Users/aryan/Documents/Project/trained_model.sav','rb'))

def car_price_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return float(prediction[0])

def main():
    st.title('Car Price Prediction Web App')
    
    Year = st.text_input('Year of Purchase', '0')
    Present_Price = st.text_input('Present Price', '0')
    KMs_Driven = st.text_input('Distance Driven', '0')
    Fuel_Type = st.text_input('Fuel Type (0 for Petrol, 1 for Diesel, 2 for CNG)', '0')
    Seller_Type = st.text_input('Seller Type (0 for Dealer, 1 for Individual)', '0')
    Transmission = st.text_input('Transmission Type (0 for Manual, 1 for Automatic)', '0')
    Owner = st.text_input('No. of Owners', '0')
    
    price = ''
    
    if st.button('Car Price Prediction'):
        
        try:
            # Convert inputs to float
            input_data = [
                float(Year), float(Present_Price), float(KMs_Driven),
                float(Fuel_Type), float(Seller_Type), float(Transmission), float(Owner)
            ]

            price = car_price_prediction(input_data)
            st.success(f"Predicted Car Price: ₹{price:.2f} Lakhs/-")  

        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
    
    st.success(price)
    
if __name__ == '__main__':
    main()