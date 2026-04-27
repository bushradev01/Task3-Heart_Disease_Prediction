import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

st.title("❤️ Heart Disease Prediction System")
st.write("Enter patient details below:")

# ---------------- INPUT LAYOUT ----------------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 1, 120)

with col2:
    trestbps = st.number_input("Resting Blood Pressure", 80, 200)

with col3:
    chol = st.number_input("Cholesterol", 100, 600)

col4, col5, col6 = st.columns(3)

with col4:
    fbs = st.selectbox("Fasting Blood Sugar (>120)", [0, 1])

with col5:
    thalch = st.number_input("Max Heart Rate", 60, 220)

with col6:
    exang = st.selectbox("Exercise Induced Angina", [0, 1])

col7, col8, col9 = st.columns(3)

with col7:
    oldpeak = st.number_input("Oldpeak", 0.0, 6.0)

with col8:
    sex = st.selectbox("Sex", ["Male", "Female"])

with col9:
    cp = st.selectbox("Chest Pain Type", ["typical angina", "non-anginal", "asymptomatic"])

col10, col11 = st.columns(2)

with col10:
    restecg = st.selectbox("Rest ECG", ["normal", "st-t abnormality"])

# ---------------- ENCODING ----------------
sex = 1 if sex == "Male" else 0

cp_non_anginal = 1 if cp == "non-anginal" else 0
cp_typical = 1 if cp == "typical angina" else 0

restecg_normal = 1 if restecg == "normal" else 0
restecg_st = 1 if restecg == "st-t abnormality" else 0

# ---------------- PREDICTION ----------------
if st.button("Predict Risk"):

    input_data = np.array([[
        age,
        trestbps,
        chol,
        fbs,
        thalch,
        exang,
        oldpeak,
        sex,
        cp_non_anginal,
        cp_typical,
        restecg_normal,
        restecg_st
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

    st.write("")

    if prediction[0] == 1:
        st.error(f"🚨 HIGH RISK OF HEART DISEASE ({probability:.2f})")
    else:
        st.success(f"✅ NO HEART DISEASE RISK ({probability:.2f})")