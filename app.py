import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model_uas.pkl")

st.write("Prediksi Biaya Asuransi")

def predict(age, sex, bmi, children, smoker):
    prediction = model.predict([[age, sex, bmi, children, smoker]])
    return prediction
app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.title('Ricky Dharma - 2019230050 - UAS DATA MINING') 
    st.markdown('Dataset :')
    data=pd.read_csv('insurance1.csv')
    st.write(data.head())
    
   

elif app_mode == 'Prediction':
    age = st.number_input("Umur",0)
    sex = st.selectbox("Jenis Kelamin", ["0", "1"])
    bmi = st.number_input("BMI",0)
    children = st.number_input("Jumlah Anak", 0)
    smoker = st.selectbox("Smoker", ["0", "1"])

    if st.button("Predict"):
        result = predict(age, 1 if sex == "1" else 0, bmi, children, 1 if smoker == "1" else 0)
        st.write("Prediksi Biaya: $", result[0])
