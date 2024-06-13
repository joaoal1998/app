import streamlit as st
import requests
import pandas as pd
from io import StringIO

# Seu token de acesso pessoal do GitHub e URL do arquivo CSV no repositório privado
token = st.secrets["database"]["token"]
url = st.secrets["database"]["url"]

# Cabeçalhos para a requisição autenticada
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3.raw'
}

@st.experimental_memo
def get_data() -> pd.DataFrame:
    # Fazendo a requisição para obter o conteúdo do CSV
    response = requests.get(url, headers=headers)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Lendo o conteúdo do CSV diretamente com pandas
        csv_content = response.content.decode('ISO-8859-1')  # Ajuste o encoding conforme necessário
        data = StringIO(csv_content)
        df = pd.read_csv(data)
        return df
    else:
        st.error(f"Falha ao obter o arquivo: {response.status_code}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

if st.button("Buscar"):
    df = get_data()
    if not df.empty:
        st.dataframe(df)
