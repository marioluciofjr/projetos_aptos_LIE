import pandas as pd
import streamlit as st
import google.generativeai as genai

# Configuração da API Key
api_key = st.text_input("""Insira sua API Key e aperte *ENTER* \n 
Saiba como gerar sua API Key ---> https://github.com/marioluciofjr/iabout#como-gerar-sua-api-key""", type="password")

# Configuração do modelo
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest',
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

# Carregando a planilha PROJETOS_APTOS
df = pd.read_csv('https://docs.google.com/spreadsheets/d/1N2QmLKcZ1QBLm3gbWoqrARCS8pklGUkMP4LJHCJP4Ek/export?format=csv&gid=0')

# Streamlit app
st.title("Incentivo ao Esporte")

# Filtro por manifestação desportiva
manifestacao_options = df['Manifestação Desportiva'].unique()
selected_manifestacao = st.selectbox("Selecione a manifestação desportiva:", manifestacao_options)
filtered_df = df[df['Manifestação Desportiva'] == selected_manifestacao]

# Filtro por projeto
projeto_options = filtered_df['Projeto'].unique()
selected_projeto = st.selectbox("Selecione o projeto:", projeto_options)
selected_row = filtered_df[filtered_df['Projeto'] == selected_projeto].iloc[0]

# Consulta deliberação
delib_link = f"https://www.in.gov.br/consulta/-/buscar/dou?q=%22{selected_row['Processo']}%22&s=todos&exactDate=all&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+do+Esporte&orgSub=Secretaria+Executiva&artType=Delibera%C3%A7%C3%A3o"
st.markdown(f"[Consultar deliberação]({delib_link})", unsafe_allow_html=True)

# Consulta CNPJ
cnpj_link = f"https://casadosdados.com.br/solucao/cnpj?q={selected_row['CNPJ']}"
st.markdown(f"[Consultar CNPJ]({cnpj_link})", unsafe_allow_html=True)

# FAQ do Gemini
st.subheader("FAQ do Gemini")

# O que diz a Lei de Incentivo ao Esporte?
faq1 = model.generate(
    prompt=f"""
    O que diz a Lei de Incentivo ao Esporte?
    {model.system_instruction}
    """,
    max_tokens=500,
    num_generations=1
)[0]
st.markdown(f"**O que diz a Lei de Incentivo ao Esporte?**\n{faq1}")

# O que significa cada manifestação desportiva?
faq2 = model.generate(
    prompt=f"""
    O que significa cada manifestação desportiva (educacional, de participação e de rendimento)?
    {model.system_instruction}
    """,
    max_tokens=500,
    num_generations=1
)[0]
st.markdown(f"**O que significa cada manifestação desportiva?**\n{faq2}")

# O que são os selos da Lei de Incentivo ao Esporte?
faq3 = model.generate(
    prompt=f"""
    O que são os selos da Lei de Incentivo ao Esporte?
    {model.system_instruction}
    """,
    max_tokens=500,
    num_generations=1
)[0]
st.markdown(f"**O que são os selos da Lei de Incentivo ao Esporte?**\n{faq3}")

# Qual é o valor que posso doar para os projetos?
faq4 = model.generate(
    prompt=f"""
    Qual é o valor que posso doar para os projetos da Lei de Incentivo ao Esporte?
    {model.system_instruction}
    """,
    max_tokens=500,
    num_generations=1
)[0]
st.markdown(f"**Qual é o valor que posso doar para os projetos?**\n{faq4}")

# Botão para limpar a consulta
if st.button("Limpar consulta"):
    st.experimental_rerun()
