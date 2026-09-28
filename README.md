# DescobriSP

> Encontre e entenda dados públicos de São Paulo.

## Sobre o projeto

O **DescobriSP** é uma ferramenta desenvolvida para facilitar a descoberta e a compreensão inicial de conjuntos de dados públicos da Prefeitura de São Paulo.

A proposta é criar uma camada de pesquisa mais simples sobre diferentes conjuntos de dados, permitindo que o usuário encontre informações por assunto e compreenda rapidamente o que pode ser encontrado em cada base, para que ela pode ser utilizada e quais são suas principais características.

## Problema identificado

A Lei nº 12.527/2011 (Lei de Acesso à Informação - LAI) estabelece o acesso à informação como um direito e determina, entre outras diretrizes, a divulgação de informações de interesse público independentemente de solicitação. A lei também prevê que os sites oficiais disponham de ferramentas de pesquisa e que as informações sejam disponibilizadas de forma objetiva, transparente, clara e em linguagem de fácil compreensão, além de contemplar formatos eletrônicos abertos, estruturados e legíveis por máquina.

Mesmo com a disponibilização dessas informações pelos órgãos públicos, o grande volume e a diversidade de dados disponíveis podem tornar difícil para o cidadão encontrar, identificar e compreender a informação que procura.

A partir dessa percepção surgiu a proposta do DescobriSP: uma ferramenta criada para facilitar a busca por conjuntos de dados públicos e melhorar a experiência do usuário na identificação e compreensão inicial dessas informações.

## Objetivo

Desenvolver uma aplicação simples que permita ao usuário:

* pesquisar conjuntos de dados por palavras-chave;
* filtrar os resultados por tema;
* compreender, em linguagem simples, o conteúdo de cada conjunto de dados;
* visualizar informações básicas sobre os dados;
* acessar a fonte oficial.

## Pesquisa e metodologia

O desenvolvimento do DescobriSP começou com a análise de conjuntos de dados públicos disponibilizados pela Prefeitura de São Paulo.

Durante a pesquisa, foram observados diferentes conjuntos de dados, seus temas, órgãos responsáveis, períodos, frequências de atualização, formatos e informações disponibilizadas.

A partir dessa análise, foram selecionados conjuntos de dados de diferentes áreas para compor um catálogo inicial da aplicação.

Para facilitar a compreensão dos dados, o catálogo foi estruturado com informações como:

* **Tema:** área à qual o conjunto de dados está relacionado;
* **Órgão:** órgão responsável pelos dados;
* **Descrição simples:** explicação resumida sobre o conjunto de dados;
* **O que encontro:** exemplos das informações disponíveis na base;
* **Para que pode ser útil:** possíveis usos para pesquisa e análise;
* **Período:** período abrangido pelos dados;
* **Frequência:** frequência de disponibilização ou atualização informada na fonte;
* **Formato:** formatos disponibilizados;
* **Fonte oficial:** página oficial do conjunto de dados.

As informações apresentadas foram baseadas nas páginas oficiais dos conjuntos de dados utilizados no catálogo. Quando determinada informação não estava disponível na fonte consultada, foi utilizada a indicação **"Não informado"**, evitando a criação de informações não presentes na fonte.

## Uso de Inteligência Artificial

A IA foi utilizada como apoio na **organização das etapas de desenvolvimento, revisão da lógica e documentação**.

## Solução desenvolvida

O DescobriSP utiliza um catálogo estruturado em CSV como base para a aplicação.

O usuário pode realizar uma busca por palavra-chave ou selecionar um tema. A aplicação então filtra os conjuntos de dados correspondentes e apresenta os resultados em cartões.

Cada resultado apresenta uma descrição simplificada e informações que ajudam o usuário a avaliar se aquele conjunto de dados é relevante para sua pesquisa.

A aplicação também disponibiliza um link para a fonte oficial, permitindo que o usuário consulte a documentação e os arquivos originais.

### Fluxo da aplicação

```text
Usuário
   ↓
Pesquisa por palavra-chave ou tema
   ↓
DescobriSP
   ↓
Filtragem do catálogo
   ↓
Resultados encontrados
   ↓
Informações simplificadas sobre o dataset
   ↓
Fonte oficial
```

## Funcionalidades

* Pesquisa por palavra-chave;
* Filtro por tema;
* Contagem de resultados encontrados;
* Exibição dos conjuntos de dados em cartões;
* Descrição dos datasets em linguagem simples;
* Informações sobre conteúdo, órgão, período, frequência e formato;
* Acesso à fonte oficial;
* Mensagem para buscas sem resultados.

## Tecnologias utilizadas

* **Python** — linguagem utilizada no desenvolvimento da aplicação;
* **Pandas** — leitura e manipulação do catálogo de dados;
* **Streamlit** — construção da interface web;
* **CSV** — armazenamento estruturado do catálogo;
* **Git** — controle de versão;
* **GitHub** — armazenamento e versionamento do projeto.

## Estrutura do projeto

```text
DescobriSP/
├── data/
│   └── datasets.csv
├── app.py
├── README.md
└── .gitignore
```

### `app.py`

Arquivo principal da aplicação. É responsável por:

* carregar o catálogo;
* criar a interface;
* disponibilizar os filtros;
* realizar a busca por palavras-chave;
* apresentar os resultados;
* disponibilizar os links para as fontes oficiais.

### `data/datasets.csv`

Arquivo que contém o catálogo utilizado pela aplicação.

Cada linha representa um conjunto de dados e possui informações descritivas utilizadas na pesquisa e apresentação dos resultados.

## Fonte dos dados

Os conjuntos de dados utilizados no catálogo foram obtidos a partir do **Portal de Dados Abertos da Prefeitura de São Paulo**.

As páginas oficiais de cada conjunto de dados são disponibilizadas individualmente na aplicação por meio do botão **"Acessar fonte oficial"**.

## Como executar
O projeto pode ser executado pelo terminal integrado do VS Code.

### 1. Clonar o repositório

```bash
git clone https://github.com/HemillyMedeiros/DescobriSP.git
```

### 2. Entrar na pasta do projeto

```bash
cd DescobriSP
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

No Windows PowerShell:

```bash
.venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install streamlit pandas
```

### 6. Executar a aplicação

```bash
streamlit run app.py
```

A aplicação será disponibilizada localmente pelo Streamlit.

