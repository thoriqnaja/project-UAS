import pickle
import numpy as np
import streamlit as st

st.title ('prediksi sakit jantung')

age = st.text_input ('umur')

sex = st.text_input ('jenis kelamin')

chol = st.text_input ('kolestrol')

reasting blood preasure = st.text_input ('tekanan darah')
