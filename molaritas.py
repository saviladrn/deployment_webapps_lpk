import streamlit as st
import numpy as np

from PIL import Image

image = Image.open("molfix.jpeg")

st.image(image)

st.subheader("Aplikasi Penghitung Molaritas")
st.write("""Molaritas merupakan suatu konsentrasi larutan yang mendefinisikan jumlah mol suatu 
zat terlarut dalam satu liter larutan. Untuk menghitung molaritas, rumusnya sebagai berikut. Anda
bisa masukkan data yang ingin anda hitung supaya memperoleh hasil nilai molaritas.""")

image = Image.open("rumusmolaritas.jpeg")

st.image(image, caption="Rumus Molaritas")

sampel = st.text_input("Masukkan nama bahan baku sekunder")
penitar = st.text_input("Masukkan nama bahan baku primer")

bobot = st.number_input("Masukkan nilai bobot zat bahan baku primer (mg)")
volume = st.number_input("Masukkan volume larutan bahan baku sekunder (mL)")
mr = st.number_input("Masukkan nilai Mr bahan baku primer (g/mol)")
fp = st.number_input("Masukkan nilai faktor pengenceran")

tombol = st.button("Tampilkan Hasil dan Kesimpulan")

if tombol:
    molaritas=bobot/(mr*volume*fp)
    st.write(f"Bahan baku sekunder",sampel,"yang telah distandarisasi oleh",penitar,"bernilai",molaritas,"mol/L")
