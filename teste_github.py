import streamlit as st
import requests
import pandas as pd
from io import StringIO

if st.button("Buscar"):
    url = 'https://raw.githubusercontent.com/joaoal1998/app/main/dados_genericos.csv'
    df = pd.read_csv(url)
    st.dataframe(df)
