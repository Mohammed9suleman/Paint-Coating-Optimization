import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Paint Usage Prediction App")

# User inputs
surface_area = st.number_input("Enter Surface Area (m²):", min_value=1)
humidity = st.slider("Humidity (%)", min_value=20, max_value=80, value=50)
temperature = st.slider("Temperature (°C)", min_value=10, max_value=35, value=25)
num_coats = st.slider("Number of Coats", min_value=1, max_value=3, value=2)
paint_type = st.radio("Select Paint Type:", ['Oil-Based', 'Water-Based', 'Latex'])

# Convert Paint Type to numerical values
paint_type_encoded = {
    'Oil-Based': [1, 0],
    'Water-Based': [0, 1],
    'Latex': [0, 0]  # Default case
}

paint_values = paint_type_encoded[paint_type]

# Create input dataframe
input_data = pd.DataFrame([[surface_area, humidity, temperature, num_coats, *paint_values]],
                          columns=['Surface Area (m²)', 'Humidity (%)', 'Temperature (°C)', 'Number of Coats', 'Paint Type_Oil-Based', 'Paint Type_Water-Based'])

# Predict paint usage
if st.button("Predict Paint Usage"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Paint Usage: {prediction[0]:.2f} Liters")
