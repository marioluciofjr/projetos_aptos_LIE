import pandas as pd
import streamlit as st
import google.generativeai as genai
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import webbrowser

# Configuração da API Key do Gemini
api_key = st.text_input("""Insira sua API Key e aperte *ENTER* \n 
Saiba como gerar sua API Key ---> https://github.com/marioluciofjr/iabout#como-gerar-sua-api-key""", type="password")

if api_key:
    import genai
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

# Conexão com a planilha do Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('caminho/para/seu/arquivo/de/credenciais.json', scope)
client = gspread.authorize(creds)
sheet = client.open("PROJETOS_APTOS").sheet1

# Obter os dados da planilha
data = sheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])

# Filtrar os projetos por manifestação desportiva
st.title("Projetos Aptos à Lei de Incentivo ao Esporte")
manifestacao = st.selectbox("Filtrar por manifestação desportiva:", df["Manifestação Desportiva"].unique())
filtered_df = df[df["Manifestação Desportiva"] == manifestacao]

# Permitir que o usuário selecione um projeto
projeto = st.selectbox("Selecione um projeto:", filtered_df["Projeto"])
projeto_row = filtered_df[filtered_df["Projeto"] == projeto].iloc[0]

# Criar os botões de consulta
st.markdown(f"<div style='background-color: #230023; color: #f2f2f2; font-family: Quicksand;'>", unsafe_allow_html=True)
if st.button("Consultar deliberação"):
    deliberacao_link = f"https://www.in.gov.br/consulta/-/buscar/dou?q=%22{projeto_row['Processo']}%22&s=todos&exactDate=all&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+do+Esporte&orgSub=Secretaria+Executiva&artType=Delibera%C3%A7%C3%A3o"
    webbrowser.open(deliberacao_link)

if st.button("Consultar CNPJ"):
    cnpj_link = f"https://casadosdados.com.br/solucao/cnpj?q={projeto_row['CNPJ']}"
    webbrowser.open(cnpj_link)
st.markdown("</div>", unsafe_allow_html=True)

# Criar a FAQ do Gemini
st.markdown("## FAQ do Gemini")

def faq_lei_incentivo_esporte():
    return """
A Lei de Incentivo ao Esporte (Lei 11.438/2006) permite que pessoas físicas e jurídicas apoiem projetos esportivos por meio de doações ou patrocínios, obtendo incentivos fiscais. As deduções são de 7% do imposto devido para pessoas físicas e 2% para pessoas jurídicas. 

A lei abrange diferentes manifestações esportivas, como esporte educacional, de participação e de rendimento. Para saber mais, acesse:
https://www.planalto.gov.br/ccivil_03/_Ato2004-2006/2006/Lei/L11438compilado.htm
https://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2022/Lei/L14439.htm#art1
"""

def faq_manifestacoes_desportivas():
    return """
As manifestações desportivas contempladas pela Lei de Incentivo ao Esporte são:

Esporte Educacional: Praticado nos sistemas de ensino e em formas assistemáticas de educação, evitando a seletividade e a hipercompetitividade de seus praticantes, com a finalidade de alcançar o desenvolvimento integral do indivíduo e a sua formação para o exercício da cidadania e a prática do lazer.

Esporte de Participação: Praticado de modo voluntário, caracterizado pela realização de atividades físicas, recreativas e esportivas, com a finalidade de contribuir para a integração dos praticantes na plenitude da vida social, na promoção da saúde e da educação, e na preservação do meio ambiente.

Esporte de Rendimento: Praticado segundo normas e regras nacionais e internacionais, com a finalidade de obter resultados e integrar pessoas e comunidades do País e estas com as de outras nações.
"""

def faq_selos_lie():
    return """
Você sabia que a Lei de Incentivo ao Esporte (LIE) premia proponentes, projetos e patrocinadores ou doadores do esporte brasileiro com selos de qualidade? Agora, essas instituições podem se diferenciar ainda mais, apresentando seu selo à comunidade, como prova de reconhecimento oficial da LIE.

O EDITAL/MC/GM Nº 2/2021 tornou pública a criação dos selos, por meio da Portaria nº 712, de 16 de dezembro de 2021, destinada ao reconhecimento de entidades proponentes, projetos e patrocinadores/doadores, relacionados à Lei nº 11.438, de dezembro de 2006 - Lei de Incentivo ao Esporte (LIE) e alterações, que contribuem com o desenvolvimento e fortalecimento do desporto nacional.

A classificação dos selos foi desenvolvida seguindo requisitos criteriosamente planejados pelo Ministério do Esporte, de acordo com as necessidades do espectro esportivo e social do Brasil.

Para obter mais informações, acesse: https://www.gov.br/esporte/pt-br/acoes-e-programas/lei-de-incentivo-ao-esporte/selo-lie/
"""

def faq_valor_doacao():
    return """
De acordo com a Lei de Incentivo ao Esporte, pessoas físicas podem deduzir até 7% do imposto de renda devido, e pessoas jurídicas podem deduzir até 2% do imposto devido.

Para calcular o valor que você pode doar, você pode utilizar o simulador da Receita Federal:
https://www27.receita.fazenda.gov.br/simulador-irpf/
"""

st.markdown(f"<div style='background-color: #230023; color: #f2f2f2; font-family: Quicksand;'>", unsafe_allow_html=True)
if st.button("O que diz a Lei de Incentivo ao Esporte?"):
    st.markdown(faq_lei_incentivo_esporte(), unsafe_allow_html=True)

if st.button("O que significa cada manifestação desportiva?"):
    st.markdown(faq_manifestacoes_desportivas(), unsafe_allow_html=True)

if st.button("O que são os selos da Lei de Incentivo ao Esporte?"):
    st.markdown(faq_selos_lie(), unsafe_allow_html=True)

if st.button("Qual é o valor que posso doar para os projetos?"):
    st.markdown(faq_valor_doacao(), unsafe_allow_html=True)

if st.button("Limpar consulta"):
    st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)
