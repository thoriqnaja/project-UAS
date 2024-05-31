import streamlit as st

st.title ('hitung luas persegi panjang')

panjang = st.number_input ("masukkan nilai", 0)
lebar = st.number_input ("masukkan lebar", 0)
hitung = st.button ("hitung luas")

if hitung :
  luas = panjang * lebar
  st.write ("luas persegi panjang adalah = ", luas)

