import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="Sistema de Web Scraping", layout="wide")
st.title("Sistema de Web Scraping com Streamlit")
st.write("Insira a URL e selecione os elementos que deseja extrair.")

with st.form("form_scraping"):
    url = st.text_input("URL do Site", value="https://www.example.com", help="Insira a URL do site que deseja fazer o scraping.")
    
    st.markdown("### Selecione os elementos para extrair:")
    extract_title = st.checkbox("Título (h1)")
    extract_paragraph = st.checkbox("Parágrafos (p)")
    extract_links = st.checkbox("Links (a)")
    extract_images = st.checkbox("Imagens (img)")
    
    submit = st.form_submit_button("Iniciar Scraping")

def scrape_website(url, extract_title, extract_paragraph, extract_links, extract_images):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a URL: {e}")
        return None
    
    soup = BeautifulSoup(response.text, 'lxml')
    
    data = {}
    
    if extract_title:
        titles = [title.get_text(strip=True) for title in soup.find_all('h1')]
        data['Títulos (h1)'] = titles if titles else ["Nenhum título encontrado."]
    
    if extract_paragraph:
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        data['Parágrafos (p)'] = paragraphs if paragraphs else ["Nenhum parágrafo encontrado."]
    
    if extract_links:
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        data['Links (a)'] = links if links else ["Nenhum link encontrado."]
    
    if extract_images:
        images = [img.get('src') for img in soup.find_all('img', src=True)]
        data['Imagens (img)'] = images if images else ["Nenhuma imagem encontrada."]
    
    return data

if submit:
    if not url:
        st.error("Por favor, insira uma URL válida.")
    elif not any([extract_title, extract_paragraph, extract_links, extract_images]):
        st.error("Por favor, selecione pelo menos um elemento para extrair.")
    else:
        with st.spinner("Realizando scraping..."):
            result = scrape_website(url, extract_title, extract_paragraph, extract_links, extract_images)
        
        if result:
            st.success("Scraping concluído com sucesso!")
            
            for key, value in result.items():
                st.markdown(f"### {key}")
                if isinstance(value, list):
                    df = pd.DataFrame({key: value})
                    st.dataframe(df)
                    
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label=f"Baixar {key}",
                        data=csv,
                        file_name=f"{key}.csv",
                        mime="text/csv",
                    )
                else:
                    st.write(value)
