import streamlit as st
import requests
import pandas as pd
from io import StringIO

if st.button("Buscar"):
    
    token = st.secrets["database"]["token"]

    url = st.secrets["database"]["url"]
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3.raw'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        
        csv_content = response.content.decode('ISO-8859-1')
        data = StringIO(csv_content)
        df = pd.read_csv(data)
        st.dataframe(df)
    else:
        print(f"Falha ao obter o arquivo: {response.status_code}")


