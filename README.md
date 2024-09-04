# projetos_aptos_LIE
Este projeto foi desenvolvido graças a Imersão Dev_ Alura & Google

## Sumário

> [Introdução](https://github.com/marioluciofjr/projetos_aptos_LIE#introdu%C3%A7%C3%A3o)\
> [Por que doar para o esporte brasileiro?](https://github.com/marioluciofjr/projetos_aptos_LIE#por-que-doar-para-o-esporte-brasileiro)\
> [Como utilizar o site](https://github.com/marioluciofjr/projetos_aptos_LIE#como-utilizar-o-site)\
> [Estrutura do projeto](https://github.com/marioluciofjr/projetos_aptos_LIE#estrutura-do-projeto)\
> [Contribuições](https://github.com/marioluciofjr/projetos_aptos_LIE#contribui%C3%A7%C3%B5es)\
> [Licença](https://github.com/marioluciofjr/projetos_aptos_LIE#licen%C3%A7a)\
> [Contato](https://github.com/marioluciofjr/projetos_aptos_LIE#contato)

## Introdução

Este projeto tem como objetivo democratizar o acesso a informações sobre projetos esportivos aptos a receberem investimentos/doações pela Lei de Incentivo ao Esporte, facilitando a consulta de dados como agência, conta bancária e empresa proponente por meio do CNPJ. A plataforma, construída com HTML, CSS e JavaScript, tem o deploy no GitHub Pages, permite que pessoas físicas e jurídicas interessadas em investir no esporte brasileiro encontrem rapidamente oportunidades e compreendam melhor como funciona esse incentivo que pode gerar abatimento no imposto de renda.

Com poucos cliques, você terá acesso a informações que não estão disponíveis de forma centralizada no site oficial do Ministério do Esporte, agilizando o processo de decisão para quem busca apoiar iniciativas esportivas de fato.

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

1. Acesse o site <a href="https://marioluciofjr.github.io/projetos_aptos_LIE" target="_blank">Projetos Aptos - Lei de Incentivo ao Esporte</a>;
2. Escolha uma das três manifestações desportivas (Educacional, Participação ou Rendimento);
3. Escolha um projeto apto para receber a Lei de Incentivo ao Esporte;
4. Clique no botão "🔍 Obter deliberação e cnpj";
5. Ao clicar no botão "Deliberação", abrirá uma outra aba que redireciona para o site do Diário Oficial da União. Pode ser que esse link leve um tempinho para atualizar. Copie o código do processo que se inicia por "71000", clique no link de deliberação e pesquise na página pelo código de processo que acabou de copiar;
6. Ao clicar no botão CNPJ, abrirá uma outra aba que redireciona para o site Casa dos Dados. Lá você obterá as informações completas sobre o CNPJ da empresa que submeteu o projeto que escolheu;
7. Na parte das "Perguntas Frequentes" você pode saber um pouco mais sobre a Lei de Incentivo ao Esporte e demais informações a respeito;
8. Se clicar no botão "🧹 Limpar", a página volta do zero para você escolher outro projeto.

[AQUI TERÁ UM GIF DEMONSTRATIVO]

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

1. **Carregamento dinâmico de dados**: Carrega dados de uma planilha do Google Sheets utilizando o formato TSV, converte os dados para um formato JSON e armazena-os em uma variável para uso posterior na página.
2. **População de dropdowns interativos**: Utiliza os dados carregados para popular dinamicamente os dropdowns de "Manifestação Desportiva" e "Projeto", permitindo a seleção de diferentes categorias e projetos relacionados.
3. **Geração de links dinâmicos para consulta**: Baseado na seleção do usuário, gera links dinâmicos para consultar deliberações e CNPJs em sites externos, adicionando um atraso para abertura em novas abas do navegador.
4. **Funcionalidade de FAQ Interativa**: Implementa uma lógica de acordeão para a seção de perguntas frequentes (FAQ), permitindo que os usuários expandam e recolham o conteúdo com um clique.
5. **Reset de seleção e conteúdo dinâmico**: Fornece uma funcionalidade para limpar seleções e redefinir o conteúdo da página, mantendo a experiência de usuário limpa e fácil de gerenciar.

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
