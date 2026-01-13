import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="House Price Prediction", layout="centered")

st.title("🏠 House Price Prediction")

st.write("Fill any fields you want. Missing fields will be auto-imputed.")

def input_field(label):
    value = st.text_input(label)
    return float(value) if value.strip() else None

payload = {
    "CRIM": input_field("CRIM"),
    "ZN": input_field("ZN"),
    "INDUS": input_field("INDUS"),
    "CHAS": input_field("CHAS"),
    "NOX": input_field("NOX"),
    "RM": input_field("RM"),
    "AGE": input_field("AGE"),
    "DIS": input_field("DIS"),
    "RAD": input_field("RAD"),
    "TAX": input_field("TAX"),
    "PTRATIO": input_field("PTRATIO"),
    "B": input_field("B"),
    "LSTAT": input_field("LSTAT"),
}

payload = {k: v for k, v in payload.items() if v is not None}

if st.button("Predict"):
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"💰 Predicted Price: {result['predicted_house_price']}")
        
        if result.get("missing_fields"):
            st.warning(f"Missing fields imputed: {result['missing_fields']}")

        if result.get("warnings"):
            st.info("⚠️ Input Warnings")
            for w in result["warnings"]:
                st.write("-", w)
    else:
        st.error(response.text)
