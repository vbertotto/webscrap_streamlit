# 🕸️ Sistema de Web Scraping com Streamlit

Este projeto é um sistema de web scraping interativo desenvolvido com **Streamlit**. Através de uma interface web, os usuários podem inserir a URL de um site e selecionar os elementos que desejam extrair, como títulos, parágrafos, links e imagens. Os dados extraídos são exibidos em formato tabular e podem ser baixados em arquivos CSV.

## 🚀 Funcionalidades

- **Inserção de URL**: Permite que os usuários insiram a URL do site que desejam realizar o scraping.
- **Seleção de Elementos**: Opções para selecionar quais elementos HTML extrair (h1, p, a, img).
- **Exibição de Dados**: Apresenta os dados extraídos em tabelas interativas.
- **Download de Dados**: Possibilidade de baixar os dados extraídos em formato CSV.
- **Tratamento de Erros**: Notifica o usuário em caso de erros durante o scraping.

## 🛠️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para construção de aplicações web interativas.
- **[Requests](https://pypi.org/project/requests/)**: Biblioteca para fazer requisições HTTP.
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**: Biblioteca para parsing de HTML e XML.
- **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulação e análise de dados.
- **[lxml](https://lxml.de/)**: Parser XML e HTML de alto desempenho.

## 📦 Instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/vbertotto/webscrap_streamlit.git
    cd sistema-webscraping-streamlit
    ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate   # No Windows: venv\Scripts\activate
    ```

3. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

## 🔧 Como Usar

1. **Execute a aplicação**:

    No terminal, navegue até o diretório do projeto e execute:

    ```bash
    streamlit run app.py
    ```

2. **Acesse a aplicação**:

    A aplicação será aberta automaticamente no seu navegador padrão. Caso contrário, você pode acessá-la manualmente pelo endereço:

    ```
    http://localhost:8501
    ```

3. **Realize o Web Scraping**:

    - Insira a URL do site que deseja fazer o scraping.
    - Selecione os elementos que deseja extrair (títulos, parágrafos, links, imagens).
    - Clique em "Iniciar Scraping".
    - Visualize os dados extraídos e, se desejar, baixe-os em formato CSV.

## Contato

Para mais informações ou perguntas, entre em contato:

- **LinkedIn**: [Vinicius Bertotto](https://www.linkedin.com/in/vinicius-bertotto/)
- **GitHub**: [vbertotto](https://github.com/vbertotto)
- **Website**: [bertotto.online](https://bertotto.online/)
```

