# DescobriSP

> Encontre e entenda dados públicos de São Paulo.

## Sobre o projeto

O **DescobriSP** é uma ferramenta desenvolvida para facilitar a descoberta e a compreensão inicial de conjuntos de dados públicos da Prefeitura de São Paulo.

A proposta é criar uma camada de pesquisa mais simples sobre diferentes conjuntos de dados, permitindo que o usuário encontre informações por assunto e compreenda rapidamente o que pode ser encontrado em cada base, para que ela pode ser utilizada e quais são suas principais características.

## Problema identificado

A Prefeitura de São Paulo disponibiliza diversos conjuntos de dados públicos, porém encontrar uma base adequada para uma determinada necessidade pode exigir que o usuário conheça previamente conceitos relacionados a dados abertos, formatos de arquivos, metadados e documentação.

Além de encontrar um conjunto de dados, também é necessário compreender o seu conteúdo para avaliar se ele pode ser utilizado para determinado objetivo.

A partir disso, o projeto buscou responder à seguinte pergunta:

> **Como facilitar a descoberta e a compreensão inicial de conjuntos de dados públicos para pessoas que não possuem conhecimento técnico sobre dados abertos?**

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

A IA foi utilizada como apoio na **estruturação do projeto, organização das etapas de desenvolvimento, revisão da lógica e documentação**.

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

## Limitações

O DescobriSP foi desenvolvido como uma solução avaliativa e possui um escopo inicial reduzido.

Atualmente:

* o catálogo possui um número limitado de conjuntos de dados;
* os dados do catálogo são cadastrados manualmente no arquivo CSV;
* a pesquisa utiliza correspondência textual e não busca semântica;
* as informações apresentadas dependem dos dados disponíveis nas fontes oficiais consultadas;
* a aplicação não realiza a atualização automática dos datasets originais.
