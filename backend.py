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

    # CSS para estilizar os botões
    # Defina os estilos CSS para os botões
    button_style = """
    <style>
      div.stButton > button {{
        background-color: {bg_color};
        color: {fg_color};
        padding: 10px 20px;
        border: 2px solid {border_color};
        border-radius: 4px;
        cursor: pointer;
        width: 200px;
        transition: background-color 0.3s, color 0.3s;
      }}

      div.stButton > button:hover {{
        background-color: {hover_bg_color};
        color: {hover_fg_color};
      }}

      div.stButton > button:active {{
        background-color: {active_bg_color};
        color: {active_fg_color};
      }}
    </style>
    """

    # Função para criar um botão colorido
    def colored_button(label, bg_color, fg_color, border_color, hover_bg_color, hover_fg_color, active_bg_color, active_fg_color):
        st.markdown(button_style.format(bg_color=bg_color, fg_color=fg_color, border_color=border_color, 
                                   hover_bg_color=hover_bg_color, hover_fg_color=hover_fg_color,
                                   active_bg_color=active_bg_color, active_fg_color=active_fg_color), unsafe_allow_html=True)
        return st.button(label)

    
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
    if colored_button("Obter deliberação e consulta CNPJ", "#dc3545", "green", "#dc3545", "white", "#dc3545", "#dc3545", "white")
    # st.button("Obter deliberação e consulta CNPJ"):
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
            resposta = model.generate_content(f"""{pergunta1}. Explique a Lei 11.438/2006: LEI Nº 11.438, DE 29 DE DEZEMBRO DE 2006.

Dispõe sobre incentivos e benefícios para fomentar as atividades de caráter desportivo e dá outras providências.

O PRESIDENTE DA REPÚBLICA Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:

CAPÍTULO I

DOS INCENTIVOS AO DESPORTO

Art. 1º A partir do ano-calendário de 2007, até o ano-calendário de 2027, inclusive, poderão ser deduzidos do imposto de renda devido, apurado na Declaração de Ajuste Anual pelas pessoas físicas ou em cada período de apuração, trimestral ou anual, pela pessoa jurídica tributada com base no lucro real, os valores despendidos a título de patrocínio ou doação no apoio direto a projetos desportivos e paradesportivos previamente aprovados pelo Ministério da Cidadania.      (Redação dada pela Lei nº 11.439, de 2022)    Produção de efeitos

§ 1º As deduções de que trata o caput deste artigo ficam limitadas:

I - relativamente à pessoa jurídica, a 2% (dois por cento) do imposto devido, observado o disposto no § 4º do art. 3º da Lei nº 9.249, de 26 de dezembro de 1995, em cada período de apuração;        (Redação dada pela Lei nº 11.439, de 2022)    Produção de efeitos

II - relativamente à pessoa física, a 7% (sete por cento) do imposto devido na Declaração de Ajuste Anual, conjuntamente com as deduções a que se referem os incisos I, II e III do art. 12 da Lei nº 9.250, de 26 de dezembro de 1995.           (Redação dada pela Lei nº 11.439, de 2022)    Produção de efeitos

§ 2º As pessoas jurídicas não poderão deduzir os valores de que trata o caput deste artigo para fins de determinação do lucro real e da base de cálculo da Contribuição Social sobre o Lucro Líquido - CSLL.

§ 3º Os benefícios de que trata este artigo não excluem ou reduzem outros benefícios fiscais e deduções em vigor.

§ 4º Não são dedutíveis os valores destinados a patrocínio ou doação em favor de projetos que beneficiem, direta ou indiretamente, pessoa física ou jurídica vinculada ao doador ou patrocinador.

§ 5º Consideram-se vinculados ao patrocinador ou ao doador:

I - a pessoa jurídica da qual o patrocinador ou o doador seja titular, administrador, gerente, acionista ou sócio, na data da operação ou nos 12 (doze) meses anteriores;

II - o cônjuge, os parentes até o terceiro grau, inclusive os afins, e os dependentes do patrocinador, do doador ou dos titulares, administradores, acionistas ou sócios de pessoa jurídica vinculada ao patrocinador ou ao doador, nos termos do inciso I deste parágrafo;

III - a pessoa jurídica coligada, controladora ou controlada, ou que tenha como titulares, administradores acionistas ou sócios alguma das pessoas a que se refere o inciso II deste parágrafo.

§ 6º O limite previsto no inciso I do § 1º deste artigo será de 4% (quatro por cento) quando o projeto desportivo ou paradesportivo for destinado a promover a inclusão social por meio do esporte, preferencialmente em comunidades em situação de vulnerabilidade social, nos termos do § 1º do art. 2º desta Lei, conjuntamente com as deduções a que se referem o art. 26 da Lei nº 8.313, de 23 de dezembro de 1991, e o art. 1º da Lei nº 8.685, de 20 de julho de 1993.          (Incluído pela Lei nº 11.439, de 2022)    Produção de efeitos

§ 7º (VETADO).         (Incluído pela Lei nº 11.439, de 2022)    Produção de efeitos

Art. 2º Os projetos desportivos e paradesportivos, em cujo favor serão captados e direcionados os recursos oriundos dos incentivos previstos nesta Lei, atenderão a pelo menos uma das seguintes manifestações, nos termos e condições definidas em regulamento: (Redação dada pela Lei nº 11.472, de 2007)

I - desporto educacional;

II - desporto de participação;

III - desporto de rendimento.

§ 1º Poderão receber os recursos oriundos dos incentivos previstos nesta Lei os projetos desportivos destinados a promover a inclusão social por meio do esporte, preferencialmente em comunidades de vulnerabilidade social.

§ 2º É vedada a utilização dos recursos oriundos dos incentivos previstos nesta Lei para o pagamento de remuneração de atletas profissionais, nos termos da Lei nº 9.615, de 24 de março de 1998, em qualquer modalidade desportiva.

§ 3º O proponente não poderá captar, para cada projeto, entre patrocínio e doação, valor superior ao aprovado pelo Ministério do Esporte, na forma do art. 4º desta Lei.

Art. 3º Para fins do disposto nesta Lei, considera-se:

I - patrocínio:

a) a transferência gratuita, em caráter definitivo, ao proponente de que trata o inciso V do caput deste artigo de numerário para a realização de projetos desportivos e paradesportivos, com finalidade promocional e institucional de publicidade; (Redação dada pela Lei nº 11.472, de 2007)

b) a cobertura de gastos ou a utilização de bens, móveis ou imóveis, do patrocinador, sem transferência de domínio, para a realização de projetos desportivos e paradesportivos pelo proponente de que trata o inciso V do caput deste artigo; (Redação dada pela Lei nº 11.472, de 2007)

II - doação:

a) a transferência gratuita, em caráter definitivo, ao proponente de que trata o inciso V do caput deste artigo de numerário, bens ou serviços para a realização de projetos desportivos e paradesportivos, desde que não empregados em publicidade, ainda que para divulgação das atividades objeto do respectivo projeto; (Redação dada pela Lei nº 11.472, de 2007)

b) a distribuição gratuita de ingressos para eventos de caráter desportivo e paradesportivo por pessoa jurídica a empregados e seus dependentes legais ou a integrantes de comunidades de vulnerabilidade social; (Redação dada pela Lei nº 11.472, de 2007)

III - patrocinador: a pessoa física ou jurídica, contribuinte do imposto de renda, que apóie projetos aprovados pelo Ministério do Esporte nos termos do inciso I do caput deste artigo;

IV - doador: a pessoa física ou jurídica, contribuinte do imposto de renda, que apóie projetos aprovados pelo Ministério do Esporte nos termos do inciso II do caput deste artigo;

V - proponente: a pessoa física ou a pessoa jurídica de direito público, ou de direito privado com fins não econômicos, de natureza esportiva, bem como as instituições de ensino fundamental, médio e superior, que tenham projeto aprovado nos termos desta Lei.    (Redação dada pela Lei nº 14.933, de 2024)

Art. 4º A avaliação e a aprovação do enquadramento dos projetos apresentados na forma prevista no art. 5º desta Lei cabem a uma Comissão Técnica vinculada ao Ministério do Esporte, garantindo-se a participação de representantes governamentais, designados pelo Ministro do Esporte, e representantes do setor desportivo, indicados pelo Conselho Nacional de Esporte.

Parágrafo único. A composição, a organização e o funcionamento da comissão serão estipulados e definidos em regulamento.

Art. 5º Os projetos desportivos e paradesportivos de que trata o art. 1º desta Lei serão submetidos ao Ministério do Esporte, acompanhados da documentação estabelecida em regulamento e de orçamento analítico.

§ 1º A aprovação dos projetos de que trata o caput deste artigo somente terá eficácia após a publicação de ato oficial contendo o título do projeto aprovado, a instituição responsável, o valor autorizado para captação e o prazo de validade da autorização.

§ 2º Os projetos aprovados e executados com recursos desta Lei serão acompanhados e avaliados pelo Ministério do Esporte.

CAPÍTULO II

DISPOSIÇÕES GERAIS

Art. 6º A divulgação das atividades, bens ou serviços resultantes dos projetos desportivos e paradesportivos financiados nos termos desta Lei mencionará o apoio institucional, com inserção da Bandeira Nacional, nos termos da Lei nº 5.700, de 1º de setembro de 1971.

Art. 7º A prestação de contas dos projetos beneficiados pelos incentivos previstos nesta Lei fica a cargo do proponente e será apresentada ao Ministério do Esporte, na forma estabelecida pelo regulamento.

Art. 8º O Ministério do Esporte informará à Secretaria da Receita Federal do Brasil - RFB os valores correspondentes a doação ou patrocínio destinados ao apoio direto a projetos desportivos e paradesportivos, no ano-calendário anterior. (Redação dada pela Lei nº 13.043, de 2014)

Parágrafo único. A RFB estabelecerá, em ato normativo próprio, a forma, o prazo e as condições para o cumprimento da obrigação acessória a que se refere o caput deste artigo. (Redação dada pela Lei nº 13.043, de 2014)

Art. 9º Compete à Secretaria da Receita Federal, no âmbito de suas atribuições, a fiscalização dos incentivos previstos nesta Lei.

Art. 10. Constituem infração aos dispositivos desta Lei:

I - o recebimento pelo patrocinador ou doador de qualquer vantagem financeira ou material em decorrência do patrocínio ou da doação que com base nela efetuar;

II - agir o patrocinador, o doador ou o proponente com dolo, fraude ou simulação para utilizar incentivo nela previsto;

III - desviar para finalidade diversa da fixada nos respectivos projetos dos recursos, bens, valores ou benefícios com base nela obtidos;

IV - adiar, antecipar ou cancelar, sem justa causa, atividade desportiva beneficiada pelos incentivos nela previstos;

V - o descumprimento de qualquer das suas disposições ou das estabelecidas em sua regulamentação.

Art. 11. As infrações aos dispositivos desta Lei, sem prejuízo das demais sanções cabíveis, sujeitarão:

I - o patrocinador ou o doador ao pagamento do imposto não recolhido, além das penalidades e demais acréscimos previstos na legislação;

II - o infrator ao pagamento de multa correspondente a 2 (duas) vezes o valor da vantagem auferida indevidamente, sem prejuízo do disposto no inciso I do caput deste artigo.

Parágrafo único. O proponente é solidariamente responsável por inadimplência ou irregularidade verificada quanto ao disposto no inciso I do caput deste artigo.

Art. 12. Os recursos provenientes de doações ou patrocínios efetuados nos termos do art. 1º desta Lei serão depositados e movimentados em conta bancária específica, no Banco do Brasil S.A. ou na Caixa Econômica Federal, que tenha como titular o proponente do projeto aprovado pelo Ministério do Esporte.

Parágrafo único. Não são dedutíveis, nos termos desta Lei, os valores em relação aos quais não se observe o disposto neste artigo.

Art. 13. Todos os recursos utilizados no apoio direto a projetos desportivos e paradesportivos previstos nesta Lei deverão ser disponibilizados na rede mundial de computadores, de acordo com a Lei nº 9.755, de 16 de dezembro de 1998.

Parágrafo único. Os recursos a que se refere o caput deste artigo ainda deverão ser disponibilizados, mensalmente, no sítio do Ministério do Esporte, constando a sua origem e destinação.

Art. 13-A. O valor máximo das deduções de que trata o art. 1º desta Lei será fixado anualmente em ato do Poder Executivo, com base em um percentual da renda tributável das pessoas físicas e do imposto sobre a renda devido por pessoas jurídicas tributadas com base no lucro real. (Incluído pela Lei nº 11.472, de 2007)

Parágrafo único. Do valor máximo a que se refere o caput deste artigo o Poder Executivo fixará os limites a serem aplicados para cada uma das manifestações de que trata o art. 2º desta Lei. (Incluído pela Lei nº 11.472, de 2007)

Art. 13-B. A divulgação das atividades, bens ou serviços resultantes de projetos desportivos e paradesportivos, culturais e de produção audiovisual e artística financiados com recursos públicos mencionará o apoio institucional com a inserção da Bandeira Nacional, nos termos da Lei nº 5.700, de 1º de setembro de 1971. (Incluído pela Lei nº 11.472, de 2007)

Art. 13-C. Sem prejuízo do disposto no art. 166 da Constituição Federal, os Ministérios da Cultura e do Esporte encaminharão ao Congresso Nacional relatórios detalhados acerca da destinação e regular aplicação dos recursos provenientes das deduções e benefícios fiscais previstos nas Leis nºs 8.313, de 23 de dezembro de 1991, e 11.438, de 29 de dezembro de 2006, para fins de acompanhamento e fiscalização orçamentária das operações realizadas. (Incluído pela Lei nº 11.472, de 2007)

Art. 14. Esta Lei entra em vigor na data de sua publicação.

Brasília, 29 de dezembro de 2006; 185º da Independência e 118º da República.

LUIZ INÁCIO LULA DA SILVA
Orlando Silva de Jesus Júnior""")
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
if colored_button("Limpar consulta", "#dc3545", "white", "#dc3545", "white", "#dc3545", "#dc3545", "white"):
    st.session_state['resposta_faq'] = ""
