import streamlit as st

st.markdown("""
    <style>
        .title {
            text-align: center;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)
#judul web
st.markdown('<h1 class="title">SkorPlus</h1>', unsafe_allow_html=True)
st.write('SkorPlus adalah website untuk prediksi hasil pertandingan sepakbola dengan menggunakan metode AdaBoost. Pada website ini juga terdapat performa dari metode XGBoost, LightGBM, dan AdaBoost untuk prediksi hasil pertandingan sepakbola')

