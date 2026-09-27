# Importando a biblioteca Streamlit, utilizada para construir a interface web da aplicação a partir de código Python.
import streamlit as st


# Definindo as configurações básicas da página, como o título exibido na aba do navegador e o ícone da aplicação.
st.set_page_config(
    page_title="DescobriSP",
    page_icon="🔎"
)

#Para exibir o nome principal da aplicação na página.
st.title("🔎 DescobriSP")

#Criando a função para a apresentação breve da proposta da ferramenta para o usuário.
st.write(
    "Encontre e entenda dados públicos de São Paulo."
)

