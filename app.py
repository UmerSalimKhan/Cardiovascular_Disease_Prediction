# Importing libs 
import streamlit as st
import joblib
import pandas as pd
import time

# Load model
def load_model(path):
    return joblib.load(path)

model = load_model("model/xgb_model_finetune.joblib")

# Streamlit app 
st.title("Cardiovascular Disease Risk Predictor")
st.subheader("Highly trained model on important features to predict the risk of cardiovascular disease")
st.header("About Dataset:")
st.subheader("A dataset based on 70k real patient history and outcome")
st.header("About Model")
st.subheader("Multiple model was trained after feature selection based on Gini importance and the best model was finetuned and is presented here")

st.metric(label="XGBoost Feature Selected Fine Tuned Model", value="73%", delta="3%")

# Data Collection
age = st.number_input("Age (years)", min_value=1, max_value=120, value=30)
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=70)
ap_hi = st.number_input("Systolic Blood Pressure (ap_hi)", min_value=50, max_value=250, value=120)
ap_lo = st.number_input("Diastolic Blood Pressure (ap_lo)", min_value=30, max_value=150, value=80)

# Input data config
input_data = [[age, height, weight, ap_hi, ap_lo]]

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    risk = "High Risk of Cardiovascular Disease" if prediction[0] == 1 else "Low Risk of Cardiovascular Disease"

    # Show and update progress bar for managing delay with model calculation
    bar = st.progress(33)
    time.sleep(0.5)
    bar.progress(66)
    time.sleep(0.5)
    bar.progress(100)

    with st.status("Analyzing...") as s:
        time.sleep(0.5)
        st.write("Almost done...")
        s.update(label="Done")

    if prediction[0] == 1:
        st.markdown(
            "<div style='padding: 12px; background-color:#ffcccc; color:; "
            "border-radius:8px; font-size:20px;'><b>High Risk of Cardiovascular Disease</b></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='padding: 12px; background-color:#ccffcc; color:#006600; "
            "border-radius:8px; font-size:20px;'><b>Low Risk of Cardiovascular Disease</b></div>",
            unsafe_allow_html=True
        )
