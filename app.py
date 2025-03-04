import streamlit as st
import pandas as pd

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Unit conversion functions
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.20462,
        "Ounce": 35.274,
        "Ton": 0.001
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

# UI Components
st.title("✨Advanced Unit Converter✨")
st.write("⭐Convert between different units easily.⭐")

conversion_type = st.selectbox("⚖️ Select conversion type", [
    "Length", "Weight", "Temperature"
])

if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce", "Ton"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter value", format="%.2f")
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
