# app.py

import pandas as pd
import numpy as np
import joblib
import streamlit as st

# Load trained model and column structure
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# UI Header
st.title("💧 Water Pollutants Predictor")
st.write("Predict water pollution levels using year, station, and water indicators.")

# User inputs
year_input = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2024)
station_id = st.number_input("Enter Station ID (1–22)", min_value=1, max_value=22, value=1)

st.markdown("### Enter water indicator values (approximate):")
NH4 = st.number_input("NH4 (Ammonium)", min_value=0.0, value=0.5, step=0.1)
BSK5 = st.number_input("BSK5 (Biochemical Oxygen Demand)", min_value=0.0, value=3.0, step=0.1)
Suspended = st.number_input("Suspended Solids", min_value=0.0, value=10.0, step=0.1)

# On click
if st.button('Predict'):
    # Prepare input dataframe
    input_df = pd.DataFrame({
        'year': [year_input],
        'id': [station_id],
        'NH4': [NH4],
        'BSK5': [BSK5],
        'Suspended': [Suspended]
    })

    # One-hot encode and align
    input_encoded = pd.get_dummies(input_df, columns=['id'])
    for col in model_cols:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_cols]

    # Make prediction
    predicted_pollutants = model.predict(input_encoded)[0]
    pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

    # Output results
    st.subheader(f"📊 Predicted Pollutant Levels for Station {station_id} in {year_input}:")
    for p, val in zip(pollutants, predicted_pollutants):
        st.write(f"**{p}**: {val:.2f}")
