import streamlit as st
import requests
import pandas as pd
from io import StringIO

if st.button("Buscar"):
    df = pd.read_csv('dados_genericos.csv')
    st.dataframe(df)
