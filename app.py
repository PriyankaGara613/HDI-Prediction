import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("hdi_model.pkl")
encoder = joblib.load("label_encoder.pkl")

st.title("🌍 Human Development Index Prediction")

life = st.number_input(
    "Life Expectancy at Birth",
    min_value=40.0,
    max_value=90.0,
    value=75.0
)

expected = st.number_input(
    "Expected Years of Schooling",
    min_value=0.0,
    max_value=25.0,
    value=15.0
)

mean = st.number_input(
    "Mean Years of Schooling",
    min_value=0.0,
    max_value=20.0,
    value=10.0
)

gni = st.number_input(
    "Gross National Income (GNI) per Capita",
    min_value=0,
    value=15000
)

if st.button("Predict HDI"):
    input_df = pd.DataFrame({
        "Life expectancy at birth": [life],
        "Expected years of schooling": [expected],
        "Mean years of schooling": [mean],
        "Gross national income (GNI) per capita": [gni]
    })

    prediction = model.predict(input_df)
    result = encoder.inverse_transform(prediction)

    st.success(f"Predicted HDI Category: {result[0]}")