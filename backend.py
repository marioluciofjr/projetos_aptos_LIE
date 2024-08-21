import streamlit as st
import google.generativeai as genai
import pandas as pd
import requests

# Configuração da API Key
api_key = st.text_input("""Insira sua API Key e aperte *ENTER* \n 
Saiba como gerar sua API Key ---> https://github.com/marioluciofjr/iabout#como-gerar-sua-api-key""", type="password")

# Carregamento da planilha
@st.cache_data
def carregar_planilha():
    url = "https://docs.google.com/spreadsheets/d/1N2QmLKcZ1QBLm3gbWoqrARCS8pklGUkMP4LJHCJP4Ek/export?format=csv&gid=0"
    planilha = pd.read_csv(url)
    return planilha

planilha = carregar_planilha()

# Interface do Streamlit
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
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
        system_instruction="Agora você é um especialista em FAQ, responsável por fornecer respostas precisas e concisas a perguntas frequentes. Você possui um profundo conhecimento sobre o assunto abordado no prompt e consegue sintetizar informações complexas em respostas claras e fáceis de entender. Sua função principal é garantir que as dúvidas dos usuários sejam respondidas de forma eficaz, utilizando linguagem clara e objetiva."
    )

    st.title("Consulta de Projetos Aptos - Lei de Incentivo ao Esporte")
    st.write("Selecione a manifestação desportiva e o projeto para obter as informações.")
    
    # Filtros de manifestação desportiva e projeto
    manifestacao = st.selectbox("Escolha a Manifestação Desportiva:", planilha['Manifestação Desportiva'].unique())
    projetos_filtrados = planilha[planilha['Manifestação Desportiva'] == manifestacao]['Projeto'].unique()
    projeto = st.selectbox("Escolha o Projeto:", projetos_filtrados)
    
    if st.button("Obter deliberação e consulta CNPJ"):
        st.info("Carregando... 0%")
        
        # Obter dados do projeto selecionado
        dados_projeto = planilha[planilha['Projeto'] == projeto].iloc[0]
        processo = dados_projeto['Processo']
        cnpj = dados_projeto['CNPJ']
        
        # Links para deliberação e consulta CNPJ
        link_deliberacao = f"https://www.in.gov.br/consulta/-/buscar/dou?q=%22{processo}%22&s=todos&exactDate=all&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+do+Esporte&orgSub=Secretaria+Executiva&artType=Delibera%C3%A7%C3%A3o"
        link_cnpj = f"https://casadosdados.com.br/solucao/cnpj?q={cnpj}"
        
        st.markdown(f"[**Consultar deliberação**]({link_deliberacao})", unsafe_allow_html=True)
        st.markdown(f"[**Consultar CNPJ**]({link_cnpj})", unsafe_allow_html=True)

        st.success("Consulta concluída. Links gerados com sucesso.")
    
    # FAQ do Gemini
    st.markdown("### Perguntas Frequentes (FAQ)")

    faqs = {
        "O que diz a Lei de Incentivo ao Esporte?": "Lei 11.438/2006 com alterações da Lei 11.439/2022. Confira o texto completo no link: https://www.planalto.gov.br/ccivil_03/_Ato2004-2006/2006/Lei/L11438compilado.htm.",
        "O que significa cada manifestação desportiva?": "Explicação das manifestações desportivas: Educacional, Participação e Rendimento.",
        "O que são os selos da Lei de Incentivo ao Esporte?": "Informações sobre os selos da LIE, criados pela Portaria nº 712/2021. Mais detalhes em: https://www.gov.br/esporte/pt-br/acoes-e-programas/lei-de-incentivo-ao-esporte/selo-lie/",
        "Qual é o valor que posso doar para os projetos?": "O simulador da Receita Federal ajuda a calcular quanto doar, de acordo com a regra percentual da LIE. Acesse: https://www27.receita.fazenda.gov.br/simulador-irpf/"
    }
    
    for pergunta, resposta in faqs.items():
        if st.button(pergunta):
            resposta_gerada = model.generate(prompt=pergunta).candidates[0]['text']
            st.write(resposta_gerada)
            st.markdown(f"[Leia mais aqui]({resposta})", unsafe_allow_html=True)
    
    # Botão de reiniciar
    if st.button("Limpar consulta"):
        st.experimental_rerun()
