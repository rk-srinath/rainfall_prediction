import streamlit as st
import pickle
import numpy as np
import zipfile
import os

# Unzip the model file if not already extracted
if not os.path.exists('weather_model.pkl'):
    with zipfile.ZipFile('weather_model.zip', 'r') as zip_ref:
        zip_ref.extractall()

# Load the saved model
with open('weather_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.title("Rainfall Prediction")
st.write("Use this app to predict the rainfall based on the features.")

# Feature Input Section
st.sidebar.header("Input Features")
feature_1 = st.sidebar.number_input("MaxT", value=0.0, format="%.2f")
feature_2 = st.sidebar.number_input("MinT", value=0.0, format="%.2f")
feature_3 = st.sidebar.number_input("RH1", value=0.0, format="%.2f")
feature_4 = st.sidebar.number_input("RH2", value=0.0, format="%.2f")
feature_5 = st.sidebar.number_input("Wind", value=0.0, format="%.2f")
feature_7 = st.sidebar.number_input("SSH", value=0.0, format="%.2f")
feature_8 = st.sidebar.number_input("Evap", value=0.0, format="%.2f")
feature_9 = st.sidebar.number_input("Radiation", value=0.0, format="%.2f")
feature_10 = st.sidebar.number_input("FAO56_ET", value=0.0, format="%.2f")
feature_11 = st.sidebar.number_input("Lat", value=0.0, format="%.2f")
feature_12 = st.sidebar.number_input("Lon", value=0.0, format="%.2f")
feature_13 = st.sidebar.number_input("Cum_Rain", value=0.0, format="%.2f")

# Make Prediction
if st.sidebar.button("Predict"):
    input_features = np.array([[feature_1, feature_2, feature_3, feature_4, feature_5,
                                 feature_7, feature_8, feature_9, feature_10,
                                 feature_11, feature_12, feature_13]])
    prediction = model.predict(input_features)
    st.success(f"Predicted Rainfall: {prediction[0]:.4f}")
