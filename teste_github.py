import streamlit as st
import requests
import pandas as pd
from io import StringIO

# Seu token de acesso pessoal do GitHub
token = st.secrets["database"]["token"]

# URL do arquivo CSV no repositório privado
url = st.secrets["database"]["url"]

# Cabeçalhos para a requisição autenticada
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3.raw'
}

# Fazendo a requisição para obter o conteúdo do CSV
response = requests.get(url, headers=headers)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Lendo o conteúdo do CSV diretamente com pandas
    csv_content = response.content.decode('ISO-8859-1')
    data = StringIO(csv_content)
    df = pd.read_csv(data)
    st.dataframe(df)
else:
    print(f"Falha ao obter o arquivo: {response.status_code}")

# Flag de controle para reiniciar o aplicativo
restart_flag = st.button('Reiniciar App')

# Lógica para reiniciar o app
if restart_flag:
    # Exibe uma mensagem indicando que o aplicativo será reiniciado
    st.warning('Reiniciando o aplicativo...')
    # Simula um redirecionamento que força o navegador a recarregar a página
    # Este truque pode ser usado para forçar o aplicativo a "reiniciar"
    js = """
    <script>
    window.onload = function() {
        setTimeout(function() {
            window.location.reload(true);
        }, 1000);
    }
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)

    # Finaliza a execução do script atual para evitar a execução adicional de código
    st.stop()
