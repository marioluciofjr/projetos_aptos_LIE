import streamlit as st
import google.generativeai as genai
import pandas as pd
from urllib.parse import quote

# Load data from Google Sheets
SHEET_URL = "https://docs.google.com/spreadsheets/d/1N2QmLKcZ1QBLm3gbWoqrARCS8pklGUkMP4LJHCJP4Ek/edit?gid=0#gid=0"
df = pd.read_csv(SHEET_URL)

# Streamlit app
st.set_page_config(layout="wide")
st.title("Lei de Incentivo ao Esporte")

# Gemini API setup
api_key = st.text_input("""Insira sua API Key e aperte *ENTER* \n 
Saiba como gerar sua API Key ---> https://github.com/marioluciofjr/iabout#como-gerar-sua-api-key""", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash',
                                  generation_config={
                                      "candidate_count": 1,
                                      "temperature": 0.75,
                                      "top_k": 40,
                                      "top_p": 0.95
                                  },
                                  safety_settings={
                                      'HATE': 'BLOCK_NONE',
                                      'HARASSMENT': 'BLOCK_NONE',
                                      'SEXUAL': 'BLOCK_NONE',
                                      'DANGEROUS': 'BLOCK_NONE'
                                  },
                                  system_instruction="Agora você é um especialista em FAQ, responsável por fornecer respostas precisas e concisas a perguntas frequentes. Você possui um profundo conhecimento sobre o assunto abordado no prompt e consegue sintetizar informações complexas em respostas claras e fáceis de entender. Sua função principal é garantir que as dúvidas dos usuários sejam respondidas de forma eficaz, utilizando linguagem clara e objetiva.")

# Filter data by sport manifestation
sport_manifestation = st.selectbox("Selecione a manifestação desportiva", df["Manifestação Desportiva"].unique())
filtered_df = df[df["Manifestação Desportiva"] == sport_manifestation]

# Select a project
project = st.selectbox("Selecione um projeto", filtered_df["Projeto"])
selected_row = filtered_df[filtered_df["Projeto"] == project].iloc[0]

# Display project details and buttons
st.write(f"Proponente: {selected_row['Proponente']}")
st.write(f"Processo: {selected_row['Processo']}")
st.write(f"CNPJ: {selected_row['CNPJ']}")
st.write(f"Manifestação Desportiva: {selected_row['Manifestação Desportiva']}")

# Create buttons
col1, col2 = st.columns(2)
with col1:
    st.button("Consultar deliberação",
              f"https://www.in.gov.br/consulta/-/buscar/dou?q=%22{quote(selected_row['Processo'])}%22&s=todos&exactDate=all&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+do+Esporte&orgSub=Secretaria+Executiva&artType=Delibera%C3%A7%C3%A3o",
              use_container_width=True)
with col2:
    st.button("Consultar CNPJ",
              f"https://casadosdados.com.br/solucao/cnpj?q={selected_row['CNPJ']}",
              use_container_width=True)

# FAQ section
st.write("### FAQ do Gemini")

# What is the Sports Incentive Law?
faq1 = st.button("O que diz a Lei de Incentivo ao Esporte?")
if faq1:
    response = model.generate_text(
        "A Lei de Incentivo ao Esporte (Lei 11.438/2006) permite que pessoas físicas e jurídicas destinem parte do imposto de renda devido a projetos esportivos, com deduções de até 7% para pessoas físicas e 2% para pessoas jurídicas. Essa lei visa incentivar o desenvolvimento do esporte no Brasil, tanto nas áreas de participação, educacional e de rendimento. O texto completo da lei pode ser encontrado neste link: https://www.planalto.gov.br/ccivil_03/_Ato2004-2006/2006/Lei/L11438compilado.htm. Uma atualização recente (Lei 11.439/2022) alterou os percentuais de dedução, que agora são de 7% para pessoas físicas e 2% para pessoas jurídicas. Você pode consultar essa atualização neste link: https://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2022/Lei/L14439.htm#art1")
    st.write(response)

# What are the different sport manifestations?
faq2 = st.button("O que significa cada manifestação desportiva?")
if faq2:
    response = model.generate_text(
        "A Lei de Incentivo ao Esporte reconhece três principais manifestações desportivas:\n\n1. Manifestação desportiva educacional: Relacionada a projetos que visam o desenvolvimento de atividades esportivas como parte do processo educacional e de formação do indivíduo.\n\n2. Manifestação desportiva de participação: Relacionada a projetos que visam a promoção da prática esportiva com finalidade de lazer, recreação, inclusão social e promoção da saúde.\n\n3. Manifestação desportiva de rendimento: Relacionada a projetos que visam o desenvolvimento de atletas, seleções e equipes esportivas, com o objetivo de obter resultados em competições."
    )
    st.write(response)

# What are the LIE seals?
faq3 = st.button("O que são os selos da Lei de Incentivo ao Esporte?")
if faq3:
    response = model.generate_text(
        "Você sabia que a Lei de Incentivo ao Esporte (LIE) premia proponentes, projetos e patrocinadores ou doadores do esporte brasileiro com selos de qualidade? Agora, essas instituições podem se diferenciar ainda mais, apresentando seu selo à comunidade, como prova de reconhecimento oficial da LIE. O EDITAL/MC/GM Nº 2/2021 tornou pública a criação dos selos, por meio da Portaria nº 712, de 16 de dezembro de 2021, destinada ao reconhecimento de entidades proponentes, projetos e patrocinadores/doadores, relacionados à Lei nº 11.438, de dezembro de 2006 - Lei de Incentivo ao Esporte (LIE) e alterações, que contribuem com o desenvolvimento e fortalecimento do desporto nacional. A classificação dos selos foi desenvolvida seguindo requisitos criteriosamente planejados pelo Ministério do Esporte, de acordo com as necessidades do espectro esportivo e social do Brasil. Você pode obter mais informações sobre os selos neste link: https://www.gov.br/esporte/pt-br/acoes-e-programas/lei-de-incentivo-ao-esporte/selo-lie/")
    st.write(response)

# How much can I donate to the projects?
faq4 = st.button("Qual é o valor que posso doar para os projetos?")
if faq4:
    response = model.generate_text(
        "De acordo com a Lei de Incentivo ao Esporte, as pessoas físicas podem deduzir até 7% do imposto de renda devido para realização de doações a projetos esportivos. Já as pessoas jurídicas podem deduzir até 2% do imposto devido. Para calcular o valor que você pode doar, existe um simulador disponibilizado pela Receita Federal, que você pode acessar neste link: https://www27.receita.fazenda.gov.br/simulador-irpf/")
    st.write(response)

# Streamlit UI
st.markdown("""
<style>
  .stButton button {
    background-color: #230023;
    color: #f2f2f2;
    font-family: 'Quicksand', sans-serif;
  }
  .stButton button:hover {
    background-color: #3e003e;
  }
</style>
""", unsafe_allow_html=True)

st.button("Limpar consulta", on_click=st.legacy_caching.clear_cache, use_container_width=True)
