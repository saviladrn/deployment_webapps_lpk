import streamlit as st
import numpy as np

from PIL import Image

st.title("MCounter")
st.header("Aplikasi Penghitung Molaritas")
st.subheader("Molaritas merupakan suatu konsentrasi larutan yang mendefinisikan jumlah mol suatu zat terlarut dalam satu liter larutan. ")

image = Image.open("mol.jpg")

st.image(image, caption="Rumus Molaritas")

sampel = st.text_input("Masukkan nama bahan baku sekunder")
penitar = st.text_input("Masukkan nama bahan baku primer")

bobot = st.number_input("Masukkan nilai bobot zat bahan baku primer (mg)")
volume = st.number_input("Masukkan volume larutan bahan baku sekunder (mL)")
mr = st.number_input("Masukkan nilai Mr bahan baku primer (g/mol)")
fp = st.number_input("Masukkan nilai faktor pengenceran")

tombol = st.button("Hitung nilai Molaritas")

if tombol:
    molaritas=bobot/(mr*volume*fp)
    st.success(f'Nilai Molaritas adalah {molaritas}')
    
press=st.button("Tampilkan Kesimpulan")

if press:
    kesimpulan=bobot/(mr*volume*fp)
    st.write(f"Bahan baku sekunder",sampel,"yang telah distandarisasi oleh",penitar,"bernilai",kesimpulan,"mol/L")
