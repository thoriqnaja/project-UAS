import pickle
import numpy as np
import streamlit as st

st.title ('prediksi sakit jantung')

age = st.text_input ('umur')

sex = st.text_input ('jenis kelamin')

chol = st.text_input ('kolestrol')

#code for prediction
hearth_diagnosis =''

#membuat tombol prediksi
if st.button ('prediksi penyakit jantung'):
  heart_prediction = model.predict([[age,sex,chol]])
  
  if (heart_prediction [0]==1)
    heart_diagnosis = 'pasien terkena penyakit jantung'
  else :
    heart_diagnosis = 'pasien tidak terkena penyakit jantung'
st.success(heart_diagnosis)
  
  
  
