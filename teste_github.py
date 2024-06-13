import streamlit as st
from github import Github
import pandas as pd
from io import StringIO

# Token de acesso pessoal do GitHub
token = st.secrets["database"]["token"]

# Criando uma instância da classe Github com o token de acesso
g = Github(token)

# Nome do repositório e caminho para o arquivo CSV
repo_name = 'joaoal1998/csv'
file_path = 'dados_genericos.csv'

# Obtendo o conteúdo do arquivo CSV
repo = g.get_repo(repo_name)
file_content = repo.get_contents(file_path)

# Lendo os dados do CSV usando StringIO para simular um arquivo
csv_data = StringIO(file_content.decoded_content.decode('utf-8'))

# Criando o DataFrame a partir dos dados CSV
df = pd.read_csv(csv_data)

# Exibindo as primeiras linhas do DataFrame para verificar se funcionou corretamente
st.dataframe(df)
