import streamlit as st
import joblib
import pandas as pd

st.title("Liver Disease Prediction App")

# Load your trained model
model = joblib.load("model.pkl")

# User inputs
age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex", ["Male", "Female"])
bilirubin = st.number_input("Total Bilirubin", 0.0, 50.0)
alkaline = st.number_input("Alkaline Phosphotase", 0.0, 2000.0)
sgpt = st.number_input("Alamine Aminotransferase (SGPT)", 0.0, 2000.0)
sgot = st.number_input("Aspartate Aminotransferase (SGOT)", 0.0, 2000.0)
proteins = st.number_input("Total Proteins", 0.0, 10.0)
albumin = st.number_input("Albumin", 0.0, 10.0)
ag_ratio = st.number_input("Albumin/Globulin Ratio", 0.0, 5.0)

# Make input DataFrame
data = pd.DataFrame([[age, 1 if sex=="Male" else 0, bilirubin, alkaline, sgpt, sgot, proteins, albumin, ag_ratio]],
    columns=["Age","Sex","Total_Bilirubin","Alkaline_Phosphotase","Alamine_Aminotransferase",
             "Aspartate_Aminotransferase","Total_Proteins","Albumin","Albumin_and_Globulin_Ratio"])

# Predict button
if st.button("Predict"):
    prediction = model.predict(data)
    st.success(f"Prediction: {'Liver Disease' if prediction[0]==1 else 'No Disease'}")
