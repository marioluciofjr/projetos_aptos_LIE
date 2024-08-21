import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configuração da API Key
api_key = st.text_input("""Insira sua API Key e aperte *ENTER* \n 
Saiba como gerar sua API Key ---> https://github.com/marioluciofjr/iabout#como-gerar-sua-api-key""", type="password")

# Configuração do modelo Gemini
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
                                      system_instruction="""Agora você é um especialista em FAQ, 
                                      responsável por fornecer respostas precisas e concisas a perguntas frequentes. 
                                      Você possui um profundo conhecimento sobre o assunto abordado no prompt e consegue sintetizar 
                                      informações complexas em respostas claras e fáceis de entender. Sua função principal é garantir que as dúvidas dos usuários 
                                      sejam respondidas de forma eficaz, utilizando linguagem clara e objetiva.""")

    # Título da Página
    st.title("Lei de Incentivo ao Esporte - FAQ e Consulta de Projetos")

    # Layout para Manifestação Desportiva
    st.subheader("Selecione a Manifestação Desportiva:")
    manifestacoes = ["Educacional", "Participação", "Rendimento"]
    manifestacao_selecionada = st.selectbox("Escolha a Manifestação Desportiva", manifestacoes)

    # Leitura da Planilha do Google Sheets
    sheet_url = "https://docs.google.com/spreadsheets/d/1N2QmLKcZ1QBLm3gbWoqrARCS8pklGUkMP4LJHCJP4Ek/export?format=csv"
    df = pd.read_csv(sheet_url)
    
    # Filtragem dos Projetos com Base na Manifestação Desportiva Selecionada
    df_filtrado = df[df['Manifestação Desportiva'] == manifestacao_selecionada]
    projeto_selecionado = st.selectbox("Escolha o Projeto", df_filtrado['Projeto'].tolist())

    # Exibição dos Botões para Deliberação e Consulta de CNPJ
    if st.button("Obter deliberação e consulta CNPJ"):
        processo = df_filtrado[df_filtrado['Projeto'] == projeto_selecionado]['Processo'].values[0]
        cnpj = df_filtrado[df_filtrado['Projeto'] == projeto_selecionado]['CNPJ'].values[0]
        
        link_deliberacao = f"https://www.in.gov.br/consulta/-/buscar/dou?q=%22{processo}%22&s=todos&exactDate=all&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+do+Esporte&orgSub=Secretaria+Executiva&artType=Delibera%C3%A7%C3%A3o"
        link_cnpj = f"https://casadosdados.com.br/solucao/cnpj?q={cnpj}"
        
        st.markdown(f"[**Consultar Deliberação**]({link_deliberacao})", unsafe_allow_html=True)
        st.markdown(f"[**Consultar CNPJ**]({link_cnpj})", unsafe_allow_html=True)

    # FAQ do Gemini
    st.subheader("Perguntas Frequentes")
    
    perguntas_faq = {
        "O que diz a Lei de Incentivo ao Esporte?": "Explique a Lei 11.438/2006 e mencione a Lei 11.439/2022, que atualiza as deduções de imposto.",
        "O que significa cada manifestação desportiva?": "Explique as diferenças entre manifestação desportiva educacional, de participação e de rendimento.",
        "O que são os selos da Lei de Incentivo ao Esporte?": "Fale sobre o Selo LIE e o reconhecimento das entidades.",
        "Qual é o valor que posso doar para os projetos?": "Explique o simulador da Receita Federal para calcular as doações."
    }
    
    for pergunta, contexto in perguntas_faq.items():
        if st.button(pergunta):
            try:
                # Geração da Resposta usando a API do Gemini
                response = model.generate_content(prompt=contexto)
                if response.generations:
                    resposta_gerada = response.generations[0].text
                    st.write(resposta_gerada)
                else:
                    st.error("Nenhuma resposta gerada. Tente novamente.")
            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar a resposta: {str(e)}")

    # Botão de Limpar a Consulta
    if st.button("Limpar consulta"):
        st.experimental_rerun()
