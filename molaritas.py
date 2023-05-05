import streamlit as st

st.title("Aplikasi Menghitung Molaritas")

sampel = st.text_input("Masukkan nama bahan baku sekunder")
penitar = st.text_input("Masukkan nama bahan baku primer")

bobot = st.number_input("Masukkan nilai bobot zat bahan baku primer (gram)")
volume = st.number_input("Masukkan volume larutan bahan baku sekunder (mL)")
mr = st.number_input("Masukkan nilai Mr bahan baku primer (g/mol)")

tombol = st.button("Hitung nilai Molaritas")

if tombol:
    molaritas=bobot/(mr*volume)
    st.success(f'Nilai Molaritas adalah {molaritas}')
    
press=st.button("Tampilkan Kesimpulan")

if press:
    kesimpulan=bobot/(mr*volume)
    st.write(f"Bahan baku sekunder",sampel,"yang telah distandarisasi oleh",penitar,"bernilai",kesimpulan,"mol/L")