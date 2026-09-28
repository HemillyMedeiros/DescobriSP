# Importa a biblioteca Streamlit, utilizada para construir a interface web.
import streamlit as st

# Importa o Pandas, utilizado para ler e manipular os dados do catálogo.
import pandas as pd


# Lê o arquivo CSV que contém o catálogo de datasets.
dados = pd.read_csv("data/datasets.csv")


# Define o nome principal da aplicação.
st.title("🔎 DescobriSP")

# Apresenta uma breve descrição da proposta da ferramenta para o usuário.
st.write(
    "Encontre e entenda dados públicos de São Paulo."
)


# Mostra ao usuário a quantidade de datasets disponíveis no catálogo.
st.write(f"Atualmente, temos {len(dados)} conjuntos de dados disponíveis.")


# Cria uma lista com os temas disponíveis no catálogo.
temas = sorted(dados["tema"].unique())

# Mostra os temas disponíveis para o usuário escolher.
# Cria um filtro para o usuário escolher um tema.
tema_selecionado = st.selectbox(
    "📂 Filtre por tema:",
    ["Todos"] + temas
)

# Cria uma caixa para o usuário digitar o que está procurando.
busca = st.text_input(
    "🔎 O que você está procurando?",
    placeholder="Ex.: ciclovias, educação, parques..."
)
# Se o usuário escolheu um tema específico, filtra os datasets por esse tema.
if tema_selecionado != "Todos":
    dados = dados[dados["tema"] == tema_selecionado]



# Verifica se o usuário digitou alguma coisa na caixa de busca.
if busca:

    # Define as colunas que serão utilizadas na busca.
    colunas_busca = [
        "nome",
        "tema",
        "descricao_simples",
        "o_que_encontro",
        "para_que_pode_ser_util"
    ]

    # Junta o conteúdo dessas colunas em um único texto para cada dataset.
    texto_busca = dados[colunas_busca].fillna("").agg(" ".join, axis=1)

    # Procura a palavra digitada dentro das informações dos datasets.
    resultados = dados[
        texto_busca.str.contains(busca, case=False, na=False)
    ]

else:

    # Se a busca estiver vazia, mostra todos os datasets
    # que passaram pelo filtro de tema.
    resultados = dados

# Guarda a quantidade de resultados encontrados.
quantidade_resultados = len(resultados)

# Define a mensagem de acordo com a quantidade de resultados.
if quantidade_resultados == 1:
    st.write("**1 conjunto de dados encontrado.**")
else:
    st.write(f"**{quantidade_resultados} conjuntos de dados encontrados.**")
# Verifica se encontramos algum dataset para a busca.
if len(resultados) > 0:

    # Percorre cada dataset encontrado.
    for _, dataset in resultados.iterrows():

        # Cria um bloco visual separado para cada dataset.
        with st.container(border=True):

            # Mostra o nome do dataset como título.
            st.subheader(dataset["nome"])

            # Mostra o tema ao qual o dataset pertence.
            st.write(f"**Tema:** {dataset['tema']}")

            # Mostra uma explicação simples sobre o dataset.
            st.write(dataset["descricao_simples"])

            # Cria uma separação visual antes das informações mais detalhadas.
            st.divider()

            # Mostra quais informações podem ser encontradas na base.
            st.write(f"**O que encontro:** {dataset['o_que_encontro']}")

            # Cria uma seção destacada explicando possíveis usos do dataset.
            st.markdown("### 💡 Para que pode ser útil?")

            # Apresenta a explicação de uso em linguagem simples.
            st.write(dataset["para_que_pode_ser_util"])

            # Mostra informações básicas sobre a origem e atualização dos dados.
            # Cria quatro colunas para organizar as informações técnicas.
            col1, col2, col3, col4 = st.columns(4)

            # Mostra o órgão responsável na primeira coluna.
            with col1:
                st.write("**Órgão**")
                st.write(dataset["orgao"])

            # Mostra o período na segunda coluna.
            with col2:
                st.write("**Período**")
                st.write(dataset["periodo"])

            # Mostra a frequência na terceira coluna.
            with col3:
                st.write("**Frequência**")
                st.write(dataset["frequencia"])

            # Mostra os formatos disponíveis na quarta coluna.
            with col4:
                st.write("**Formato**")
                st.write(dataset["formato"])
            # Cria um botão que leva o usuário para a fonte oficial.
            st.link_button(
                "🔗 Acessar fonte oficial",
                dataset["url_fonte"]
            )

else:

    # Mensagem exibida quando nenhum dataset corresponde à busca.
    st.write(
        "😕 Não encontramos nenhum dataset para essa busca. "
        "Tente outro termo."
    )