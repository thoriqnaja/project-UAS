import pickle
import numpy as np
import streamlit as st

st.title ('prediksi sakit jantung')

# load save model
model = pickel.load(open('heart_statlog_cleveland_hungary_final.sav','rb'))



