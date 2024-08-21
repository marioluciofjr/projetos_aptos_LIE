import streamlit as st
import google.generativeai as genai
import pandas as pd
import textwrap
from IPython.display import Markdown

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
                                          "top_k": 60,
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
    st.title("Lei de Incentivo ao Esporte - Projetos Aptos")

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

   # Perguntas Frequentes (FAQ)
    st.subheader("Perguntas Frequentes")

    # Definição das perguntas
    pergunta1 = "O que diz a Lei de Incentivo ao Esporte?"
    pergunta2 = "O que significa cada manifestação desportiva?"
    pergunta3 = "O que são os selos da Lei de Incentivo ao Esporte?"
    pergunta4 = "Qual é o valor que posso doar para os projetos?"

    # Botão para a primeira pergunta
    if st.button(pergunta1):
        try:
            resposta = model.generate_content(f"""{pergunta1}. Explique a Lei 11.438/2006, cujo texto completo é possível visualizar neste link: https://www.planalto.gov.br/ccivil_03/_Ato2004-2006/2006/Lei/L11438compilado.htm. 
            É importante ressaltar que as deduções de imposto agora são 2% para pessoa jurídica e 7% para pessoa física, atualização presente na Lei 11.439/2022 que é possível visualizar neste link: https://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2022/Lei/L14439.htm#art1""")
            def to_markdown(text):
              text = text.replace('•', '  *')
              return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

            st.markdown(f'{resposta.text}')

        except Exception as e:
            st.error(f"Erro ao gerar resposta: {str(e)}")

    # Botão para a segunda pergunta
    if st.button(pergunta2):
        try:
            resposta = model.generate_content(f"""{pergunta2}. Explique as diferenças entre manifestação desportiva educacional, de participação e de rendimento""")
            def to_markdown(text):
              text = text.replace('•', '  *')
              return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

            st.markdown(f'{resposta.text}')
        except Exception as e:
            st.error(f"Erro ao gerar resposta: {str(e)}")

    # Botão para a terceira pergunta
    if st.button(pergunta3):
        try:
            resposta = model.generate_content(f"""{pergunta3}. Faça um disclaimer sobre o Selo LIE: 
            “Você sabia que a Lei de Incentivo ao Esporte (LIE) premia proponentes, projetos e patrocinadores ou doadores do esporte brasileiro com selos de qualidade? 
            Agora, essas instituições podem se diferenciar ainda mais, apresentando seu selo à comunidade, como prova de reconhecimento oficial da LIE. 
            O EDITAL/MC/GM Nº 2/2021 tornou pública a criação dos selos, por meio da Portaria nº 712, de 16 de dezembro de 2021, destinada ao reconhecimento de entidades proponentes, projetos e patrocinadores/doadores, 
            relacionados à Lei nº 11.438, de dezembro de 2006 - Lei de Incentivo ao Esporte (LIE) e alterações, que contribuem com o desenvolvimento e fortalecimento do desporto nacional. 
            A classificação dos selos foi desenvolvida seguindo requisitos criteriosamente planejados pelo Ministério do Esporte, de acordo com as necessidades do espectro esportivo e social do Brasil.” 
            Indique o seguinte link para obter mais informações: https://www.gov.br/esporte/pt-br/acoes-e-programas/lei-de-incentivo-ao-esporte/selo-lie/""")
            def to_markdown(text):
              text = text.replace('•', '  *')
              return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

            st.markdown(f'{resposta.text}')
        except Exception as e:
            st.error(f"Erro ao gerar resposta: {str(e)}")

    # Botão para a quarta pergunta
    if st.button(pergunta4):
        try:
            resposta = model.generate_content(f"""{pergunta4}. Explique que existe um simulador da Receita Federal para calcular quanto a pessoa física deve doar de imposto de acordo com a regra percentual estabelecida pela Lei de Incentivo ao Esporte 
            (abatimento de 7% do imposto devido para pessoas físicas). Indique o link do simulador: https://www27.receita.fazenda.gov.br/simulador-irpf/""")
            def to_markdown(text):
              text = text.replace('•', '  *')
              return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

            st.markdown(f'{resposta.text}')
        except Exception as e:
            st.error(f"Erro ao gerar resposta: {str(e)}")

    

    # Botão de Limpar a Consulta
    if st.button("Limpar consulta"):
        st.session_state['resposta_faq'] = ""  # Limpar a resposta armazenada
