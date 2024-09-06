# projetos_aptos_LIE
Este projeto foi desenvolvido graças a Imersão Dev_ Alura & Google

## Sumário

> [Introdução](https://github.com/marioluciofjr/projetos_aptos_LIE#introdu%C3%A7%C3%A3o)\
> [Como surgiu a ideia deste projeto?](https://github.com/marioluciofjr/projetos_aptos_LIE/blob/main/README.md#como-surgiu-a-ideia-deste-projeto)\
> [Por que doar para o esporte brasileiro?](https://github.com/marioluciofjr/projetos_aptos_LIE#por-que-doar-para-o-esporte-brasileiro)\
> [Como utilizar o site](https://github.com/marioluciofjr/projetos_aptos_LIE#como-utilizar-o-site)\
> [Estrutura do projeto](https://github.com/marioluciofjr/projetos_aptos_LIE#estrutura-do-projeto)\
> [Links úteis](https://github.com/marioluciofjr/projetos_aptos_LIE/edit/main/README.md#links-%C3%BAteis)\
> [Contribuições](https://github.com/marioluciofjr/projetos_aptos_LIE#contribui%C3%A7%C3%B5es)\
> [Licença](https://github.com/marioluciofjr/projetos_aptos_LIE#licen%C3%A7a)\
> [Contato](https://github.com/marioluciofjr/projetos_aptos_LIE#contato)

## Introdução

Este projeto tem como objetivo democratizar o acesso a informações sobre projetos esportivos aptos a receberem investimentos/doações pela Lei de Incentivo ao Esporte, facilitando a consulta de dados como agência, conta bancária e empresa proponente por meio do CNPJ. A plataforma foi construída com as linguagens HTML, CSS e JavaScript, sendo que o deploy foi feito tanto no GitHub Pages quanto no Vercel (algo que foi ensinado na aula 5 da Imersão Dev_). É uma página web simples que permite que pessoas físicas e jurídicas, interessadas em investir no esporte brasileiro, encontrem rapidamente oportunidades e compreendam melhor como funciona esse incentivo que pode gerar abatimento no imposto de renda.

Com poucos cliques, você terá acesso a informações que não estão disponíveis de forma centralizada no site oficial do Ministério do Esporte, agilizando o processo de decisão para quem busca apoiar iniciativas esportivas de fato.

## Como surgiu a ideia deste projeto?

Muito antes da Imersão Dev_ Alura & Google, eu já estava pesquisando sobre como incentivar o esporte brasileiro. As Olimpíadas de Paris foram bem emocionantes para mim, principalmente ao acompanhar as histórias de vida por trás das pessoas que estavam ali disputando medalhas. Sou entusiasta da ideia de que o esporte pode transformar vidas e que o Brasil tem grandes chances de melhorar a performance no ranking de medalhas se houver mais incentivo. 

Nas primeiras pesquisas que fiz, quis entender o funcionamento da [Lei de Incentivo ao Esporte](https://www.planalto.gov.br/ccivil_03/_Ato2004-2006/2006/Lei/L11438compilado.htm). Entrei no site do Ministério do Esporte e identifiquei a aba de "Projetos aptos à captação". Ao baixar a planilha em Excel e visualizar os dados, percebi a falta de informações sobre agência e conta para doar de fato e dados de contato (telefone e e-mail) dos projetos. É uma planilha com erros de preenchimento e sem muitos detalhes de como as pessoas podem se envolver com os projetos em si. 

Desbravando a internet em busca de respostas para esse problema, identifiquei que os projetos aprovados pela Lei de Incentivo ao Esporte são apresentados no Diário Oficial da União, que é um veículo de comunicação do governo federal que publica assuntos de interesse público e governamental. Lá identifiquei as agências e contas de cada projeto que eu pesquisava pelo código de processo.

Depois desse momento "Eureka", pensei em desenvolver uma plataforma simples para que as pessoas saibam quais são os projetos aptos para doação/investimento e como entrar em contato com essas organizações, uma vez que disponibilizo uma consulta ao CNPJ de cada proponente. Por conta de dúvidas sobre as nuances da LGPD, eu escolhi apenas divulgar os links onde têm as informações necessárias, isentando-me de quaisquer dados divulgados que supostamente não estejam devidamente públicos em órgãos oficiais. O filtro pela Manifestação Desportiva e os projetos foi a forma mais simples e menos burocrática que achei para entregar as informações rapidamente.

## Por que doar para o esporte brasileiro?

Além do abatimento na declaração de imposto, há vários outros fatores que podem ser decisivos para você doar recursos para fortalecer o esporte no Brasil, dentre eles:

+ **Desenvolvimento de Talentos:** Sua doação pode ajudar a descobrir e lapidar novos talentos, garantindo que o Brasil continue brilhando em competições internacionais.
+ **Inclusão Social:** O esporte é uma ferramenta poderosa para promover a inclusão social, oferecendo oportunidades para crianças, adolescentes e jovens de todas as origens.
+ **Saúde e Bem-estar:** A prática esportiva contribui para a promoção da saúde física e mental, combatendo o sedentarismo e prevenindo doenças.
+ **Formação de Cidadãos:** Por meio do esporte, valores como disciplina, trabalho em equipe e respeito são cultivados, formando cidadãos mais conscientes e engajados.
+ **Combate à Violência:** O esporte é um poderoso instrumento para tirar jovens da ociosidade e da violência, oferecendo alternativas saudáveis.
+ **Desenvolvimento Regional:** O investimento em infraestrutura esportiva e em projetos esportivos nas diversas regiões do país contribui para o desenvolvimento econômico e social.
+ **Legado Olímpico:** O esporte é um legado fundamental para o país, e sua doação pode ajudar a manter vivo o espírito olímpico e paraolímpico.
+ **Retorno Social:** Os investimentos em esporte geram um retorno social significativo, com melhorias na qualidade de vida e no desenvolvimento humano.
+ **Transformação Social:** O esporte tem o poder de transformar vidas e comunidades, promovendo a igualdade de oportunidades e a inclusão. Com isso, podemos ver possíveis atletas no nível de Rebeca Andrade, Isaquias Queiróz, Bia Souza, Rayssa Leal, Medina, Caio Bonfim, Fernanda Yara, Gabrielzinho, entre tantos outros atletas olímpicos/paralímpicos.

## Como utilizar o site

1. Acesse o site <a href="https://projetos-aptos-lie.vercel.app/" target="_blank">Projetos Aptos - Lei de Incentivo ao Esporte</a>;
2. Escolha uma das três manifestações desportivas (Educacional, Participação ou Rendimento);
3. Escolha um projeto apto para receber a Lei de Incentivo ao Esporte;
4. Clique no botão "🔍 Obter deliberação e cnpj";
5. Ao clicar no botão "Deliberação", abrirá uma outra aba que redireciona para o site do Diário Oficial da União. Coloquei um delay de 1,5 segundo para dar tempo de atualizar a página do Diário Oficial. Copie o código do processo que se inicia por "71000", clique no link de deliberação e pesquise na página pelo código de processo que acabou de copiar;
6. Ao clicar no botão CNPJ, abrirá uma outra aba que redireciona para o site Casa dos Dados. Coloquei um delay de 1,5 segundo para dar tempo de atualizar a página da Casa dos Dados. Lá você obterá as informações completas sobre o CNPJ da empresa que submeteu o projeto que escolheu;
7. Na parte das "Perguntas Frequentes" você pode saber um pouco mais sobre a Lei de Incentivo ao Esporte e demais informações a respeito;
8. Se clicar no botão "🧹 Limpar", a página volta do zero para você escolher outro projeto.

<div>
  <img align="center" src="https://github.com/marioluciofjr/projetos_aptos_LIE/blob/main/Imagens/tutorial_lie.gif?raw=true" />
</div>

## Estrutura do projeto
<div>
  <img align="center" height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg" />
  index.html<br><br>
</div>

1. **Interface de seleção de projetos desportivos**: A página permite aos usuários selecionar diferentes manifestações desportivas e projetos relacionados à Lei de Incentivo ao Esporte no Brasil.
2. **Interação dinâmica com botões**: Botões para consultar deliberações e CNPJ dos projetos são apresentados após a seleção dos itens relevantes, promovendo uma experiência de usuário mais interativa.
3. **Funcionalidade de FAQ com Acordeão**: Contém uma seção de perguntas frequentes (FAQ) que utiliza o estilo de acordeão para exibir informações sobre a Lei de Incentivo ao Esporte e outros detalhes importantes.
4. **Ícones e links para redes sociais**: Inclui ícones com links direcionando para perfis de LinkedIn e GitHub, permitindo a conexão direta com o desenvolvedor.
5. **Design responsivo e recursos Visuais**: A página utiliza fontes personalizadas do Google Fonts e ícones visuais para enriquecer a interface e garantir que o design seja responsivo e atraente.

<div>
  <br><br><img align="center" height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original-wordmark.svg" /> 
  styles.css<br><br>
</div>

1. **Definição de paleta de cores Personalizadas**: Utiliza variáveis CSS (`:root`) para definir uma paleta de cores personalizadas, facilitando o uso e a manutenção de cores consistentes no design da página.
2. **Estilos gerais para a página**: Estiliza elementos básicos como o corpo (`body`), contêiner principal (`.container`), cabeçalhos (`h1`, `h2`), e grupos de formulário, garantindo uma interface limpa e bem estruturada.
3. **Animação de ícones e Efeitos de transição**: Adiciona animações, como a rotação dos ícones dos logos dos jogos olímpicos e paralímpicos, bm como efeitos de transição para botões, melhorando a interatividade e a experiência do usuário.
4. **Estilo para componentes interativos**: Define estilos para elementos interativos, como botões e itens de acordeão, incluindo efeitos de hover, para melhorar a usabilidade.
5. **Design responsivo para diferentes tamanhos de tela**: Inclui regras de mídia (`@media`) para ajustar o design e os tamanhos de fonte em telas menores, garantindo que a página seja acessível e visualmente agradável em dispositivos móveis.

<div>
  <br><br><img align="center" height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" />
  sript.js<br><br>
</div>

1. **Carregamento dinâmico de dados**: Carrega dados de uma planilha do Google Sheets (que reúne 3911 projetos, com período de captação de recursos entre 2025 e 2026, selecionados a partir da planilha "Projetos aptos à captação", presente no site do [Ministério do Esporte](https://www.gov.br/esporte/pt-br/acoes-e-programas/lei-de-incentivo-ao-esporte/projetos-aptos-a-captacao-atualizada-27-10-23.xlsx/view)) utilizando o formato TSV, converte os dados para um formato JSON e armazena-os em uma variável para uso posterior na página.
2. **População de dropdowns interativos**: Utiliza os dados carregados para popular dinamicamente os dropdowns de "Manifestação Desportiva" e "Projeto", permitindo a seleção de diferentes categorias e projetos relacionados.
3. **Geração de links dinâmicos para consulta**: Baseado na seleção do usuário, gera links dinâmicos para consultar deliberações e CNPJs em sites externos, adicionando um atraso para abertura em novas abas do navegador.
4. **Funcionalidade de FAQ Interativa**: Implementa uma lógica de acordeão para a seção de perguntas frequentes (FAQ), permitindo que os usuários expandam e recolham o conteúdo com um clique.
5. **Reset de seleção e conteúdo dinâmico**: Fornece uma funcionalidade para limpar seleções e redefinir o conteúdo da página, mantendo a experiência de usuário limpa e fácil de gerenciar.

## Links Úteis
Durante o projeto utilizei várias ferramentas muito úteis e deixo aqui os links e alguns comentários de como foram importantes para mim neste projeto, até mesmo para quem deseja saber melhor ou mesmo compor seus próprios trabalhos:

+ [Milanote](https://app.milanote.com/) - para gerar toda a linha de raciocínio do projeto por meio da compilação de links, textos, imagens etc;
+ [Figma](https://www.figma.com/) - para trabalhar as imagens em svg;
+ [Projetos aptos à captação](https://www.gov.br/esporte/pt-br/acoes-e-programas/lei-de-incentivo-ao-esporte/projetos-aptos-a-captacao-atualizada-27-10-23.xlsx/@@download/file) - link da planilha oficial do Ministério do Esporte, que serviu como base dos dados em Google Sheets;
+ [PROJETOS_APTOS](https://docs.google.com/spreadsheets/d/1N2QmLKcZ1QBLm3gbWoqrARCS8pklGUkMP4LJHCJP4Ek/copy?gid=0#gid=0) - planilha em Google Sheets em que compilei os dados de 3911 projetos;
+ [Gemini](https://gemini.google.com/app) - explicação de funcionalidades no código, construção de trechos e comentários no código (dica importante da Aula 4 da Imersão Dev_ Alura & Google);
+ [OneCompiler](https://onecompiler.com/html) - testar os códigos html, css e javascript e verificar se estava responsivo;
+ [Olympic Brand Guidelines](https://stillmed.olympics.com/media/Documents/International-Olympic-Committee/Olympic-brand/Olympic-Brand-Guidelines.pdf) - para identificar a paleta de cores oficial dos Jogos Olímpicos;
+ [ScreenToGif](https://www.screentogif.com/) - serviu para fazer o gif do tutorial de como mexer no site;
+ [VS Code](https://code.visualstudio.com/download) - para estruturar o código em si e fazer mais testes;
+ [Badges Generator](https://badgesgenerator.com/) - para criar as badges presentes neste README;
+ [Devicon](https://devicon.dev/) - utilizar os ícones das linguagens html, css e javascript;
+ [Imersão Dev com Gemini [Guia de Mergulho]](https://grupoalura.notion.site/Imers-o-Dev-com-Gemini-Guia-de-Mergulho-7742af09c51649348a91f67157df8a41#4b72e0a2a43445abb490e252b8d5faed) - guia excelente para compreender cada detalhe da Imersão Dev_;
+ [Página da Lei de Incentivo ao Esporte](https://www.gov.br/esporte/pt-br/acoes-e-programas/lei-de-incentivo-ao-esporte) - foi essencial para eu compreender como funciona a Lei de Incentivo ao Esporte, quais são os projetos aptos para doação e investimento, quais são as etapas que cada projeto em período de captação deve seguir e assim por diante;
+ [Quer doar parte de seu Imposto de Renda para projetos da Lei de Incentivo ao Esporte? Saiba como](https://youtu.be/lutHIt0DC2Q?si=MPEiPnkbJ4JQdJCY) - vídeo didático do Ministério do Esporte que explica como funciona a doação para projetos aptos pela Lei de Incentivo ao Esporte;
+ [Guia básico de Markdown](https://docs.pipz.com/central-de-ajuda/learning-center/guia-basico-de-markdown#open) - a fim de construir um README coeso, organizado e didático;
+ [Sintaxe básica de gravação e formatação no GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) - documentação oficial do GitHub sobre o README e vários outros detalhes importantíssimos na construção de um repositório de qualidade;
+ [Vercel](https://vercel.com/) - plataforma para fazer o deploy da aplicação de maneira simples e rápida.

## Contribuições
Contribuições são bem-vindas! Se você tem sugestões para melhorar este projeto, sinta-se à vontade para criar um fork do repositório, fazer suas alterações e enviar um pull request.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo [![LICENSE](https://img.shields.io/badge/LICENSE-000000?style=plastic&link=https://github.com/marioluciofjr/projetos_aptos_LIE/blob/main/LICENSE)](https://github.com/marioluciofjr/projetos_aptos_LIE/blob/main/LICENSE) para mais detalhes.

## Contato
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
  
</div>
