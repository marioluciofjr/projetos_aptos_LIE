// Configuração do canvas
const canvas = document.getElementById('olympicRings');
const ctx = canvas.getContext('2d');
canvas.width = 1000;
canvas.height = 200;

// Cores dos anéis olímpicos
const colors = ['#0081C8', '#000000', '#EE334E', '#FCB131', '#00A651'];

// Posições iniciais dos anéis
const positions = [
  {x: 275, y: 70},
  {x: 395, y: 70},
  {x: 515, y: 70},
  {x: 335, y: 120},
  {x: 455, y: 120}
];

// Função para desenhar um anel
function drawRing(x, y, color, progress) {
  ctx.beginPath();
  ctx.arc(x, y, 50, 0, progress * Math.PI * 2);
  ctx.strokeStyle = color;
  ctx.lineWidth = 10;
  ctx.stroke();
}

// Função de animação
function animate(time) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  const progress = (time % 2000) / 2000; // 2 segundos por ciclo
  
  positions.forEach((pos, index) => {
    drawRing(pos.x, pos.y, colors[index], progress);
  });
  
  requestAnimationFrame(animate);
}

// Iniciar a animação
requestAnimationFrame(animate);

let sheetData = [];

function loadSheetData() {
    const sheetUrl = 'https://docs.google.com/spreadsheets/d/1N2QmLKcZ1QBLm3gbWoqrARCS8pklGUkMP4LJHCJP4Ek/export?format=tsv';

    fetch(sheetUrl)
        .then(response => response.text())
        .then(tsvData => {
            const lines = tsvData.split('\n');
            const headers = lines[0].split('\t');
            sheetData = lines.slice(1).map(line => {
                const values = line.split('\t');
                let entry = {};
                headers.forEach((header, index) => {
                    entry[header.trim()] = values[index].trim();
                });
                return entry;
            });
            populateManifestacao(sheetData);
        })
        .catch(error => console.error('Erro ao carregar a planilha:', error));
}

function populateManifestacao(data) {
    const manifestacaoDropdown = document.getElementById('manifestacao');
    manifestacaoDropdown.addEventListener('change', function () {
        populateProjetos(data, this.value);
    });
}

function populateProjetos(data, manifestacao) {
    const projetoDropdown = document.getElementById('projeto');
    projetoDropdown.innerHTML = '<option value="">Selecione</option>';
    projetoDropdown.disabled = manifestacao === '';

    data.forEach(row => {
        if (row['Manifestação Desportiva'] === manifestacao) {
            const option = document.createElement('option');
            option.value = row['Projeto'];
            option.textContent = row['Projeto'];
            projetoDropdown.appendChild(option);
        }
    });

    projetoDropdown.disabled = false;
    projetoDropdown.addEventListener('change', function () {
        document.getElementById('obterDados').disabled = this.value === '';
    });
}

document.getElementById('obterDados').addEventListener('click', function () {
    const projetoSelecionado = document.getElementById('projeto').value;
    const projetoInfo = sheetData.find(row => row['Projeto'] === projetoSelecionado);

    const processo = projetoInfo['Processo'];
    const cnpj = projetoInfo['CNPJ'];

    const deliberacaoLink = `https://www.in.gov.br/consulta/-/buscar/dou?q=%22${processo}%22&s=todos&exactDate=all&sortType=0&delta=20&orgPrin=Minist%C3%A9rio+do+Esporte&orgSub=Secretaria+Executiva&artType=Delibera%C3%A7%C3%A3o`;
    const cnpjLink = `https://casadosdados.com.br/solucao/cnpj?q=${cnpj}`;

    document.getElementById('consultarDeliberacao').onclick = function () {
        window.open(deliberacaoLink, '_blank');
    };
    document.getElementById('consultarCNPJ').onclick = function () {
        window.open(cnpjLink, '_blank');
    };

    document.getElementById('resultados').classList.remove('hidden');
});

document.getElementById('reset').addEventListener('click', function () {
    document.getElementById('manifestacao').value = '';
    document.getElementById('projeto').innerHTML = '<option value="">Selecione a Manifestação primeiro</option>';
    document.getElementById('projeto').disabled = true;
    document.getElementById('obterDados').disabled = true;
    document.getElementById('resultados').classList.add('hidden');
    document.getElementById('faqContent').classList.add('hidden');
});

document.getElementById('faq1').addEventListener('click', function () {
    showFaqContent(`A Lei de Incentivo ao Esporte (Lei nº 11.438/2006) visa fomentar as atividades esportivas no Brasil, concedendo incentivos fiscais para pessoas físicas e jurídicas que apoiarem projetos esportivos e paradesportivos.<br><br>
    <strong>Principais pontos da Lei:</strong><br><br>
    <ul>
        <li>Dedução do Imposto de Renda: Pessoas físicas e jurídicas podem deduzir do imposto devido os valores investidos em patrocínio ou doação a projetos esportivos aprovados pelo Ministério do Esporte.</li>
        <li>Limites da Dedução: A dedução é limitada a 2% do imposto devido para pessoas jurídicas e 7% para pessoas físicas.</li>
        <li>Tipos de Projetos: Os projetos devem se enquadrar em pelo menos uma das seguintes categorias: desporto educacional, desporto de participação ou desporto de rendimento.</li>
        <li>Inclusão Social: A Lei incentiva projetos que promovam a inclusão social por meio do esporte, especialmente em comunidades em situação de vulnerabilidade.</li>
        <li>Proibição de Remuneração de Atletas Profissionais: Os recursos da Lei não podem ser utilizados para pagar salários de atletas profissionais.</li>
        <li>Aprovação dos Projetos: Os projetos são avaliados e aprovados por uma Comissão Técnica vinculada ao Ministério do Esporte.</li>
        <li>Prestação de Contas: Os proponentes dos projetos são responsáveis por prestar contas ao Ministério do Esporte sobre a utilização dos recursos.</li>
        <li>Fiscalização: A Secretaria da Receita Federal do Brasil (RFB) é responsável por fiscalizar os incentivos previstos na Lei.</li>
    </ul>
    <br>
    Em resumo, a Lei de Incentivo ao Esporte oferece um mecanismo para que pessoas físicas e jurídicas contribuam para o desenvolvimento do esporte no Brasil, obtendo benefícios fiscais em troca.<br><br>
    <a href="https://www.planalto.gov.br/ccivil_03/_Ato2004-2006/2006/Lei/L11438compilado.htm" target="_blank">Confira a lei na íntegra aqui.</a>`);
});

document.getElementById('faq2').addEventListener('click', function () {
    showFaqContent(`<strong>As manifestações desportivas englobam uma gama de atividades que envolvem o esporte, desde a prática recreativa até o alto rendimento. Cada tipo de manifestação possui características e objetivos próprios, que definem seu papel no contexto social e cultural.</strong><br><br>
    <strong>Tipos de Manifestações Desportivas:</strong><br><br>
    <strong>1. Manifestação Desportiva Educacional:</strong><br><br>
    <ul>
        <li><strong>Objetivo:</strong> Desenvolver habilidades motoras, cognitivas e socioemocionais por meio do esporte, promovendo a inclusão, o respeito e a cidadania.</li>
        <li><strong>Características:</strong> Prioriza o aprendizado, a socialização e o desenvolvimento integral do indivíduo, sem foco em resultados competitivos.</li>
        <li><strong>Exemplos:</strong> Aulas de Educação Física escolar, programas esportivos em escolas e comunidades, atividades recreativas e lúdicas.</li>
    </ul><br>
    <strong>2. Manifestação Desportiva de Participação:</strong><br><br>
    <ul>
        <li><strong>Objetivo:</strong> Incentivar a prática esportiva de forma prazerosa e acessível, promovendo a saúde, o bem-estar e a integração social.</li>
        <li><strong>Características:</strong> Foco na participação, na diversão e na saúde, sem a necessidade de alto nível técnico ou competição formal.</li>
        <li><strong>Exemplos:</strong> Corridas populares, caminhadas, jogos recreativos em parques, campeonatos amadores e eventos esportivos para todos.</li>
    </ul><br>
    <strong>3. Manifestação Desportiva de Rendimento:</strong><br><br>
    <ul>
        <li><strong>Objetivo:</strong> Buscar o máximo desempenho e alcançar resultados competitivos de alto nível, com foco na excelência técnica e na busca por recordes.</li>
        <li><strong>Características:</strong> Treinamento intenso, profissionalismo, competição formal, busca por resultados e reconhecimento.</li>
        <li><strong>Exemplos:</strong> Jogos olímpicos, campeonatos profissionais, eventos esportivos de elite, seleções nacionais e clubes de alto nível.</li>
    </ul><br>
    <strong>Diferenças Essenciais:</strong><br><br>
    <table>
        <thead>
            <tr>
                <th>Tipo de Manifestação</th>
                <th>Objetivo Principal</th>
                <th>Foco</th>
                <th>Características</th>
                <th>Exemplos</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Educacional</td>
                <td>Desenvolvimento integral do indivíduo</td>
                <td>Aprendizado, socialização</td>
                <td>Sem foco em resultados competitivos</td>
                <td>Aulas de Educação Física, programas esportivos em escolas</td>
            </tr>
            <tr>
                <td>Participação</td>
                <td>Incentivo à prática esportiva</td>
                <td>Participação, saúde, bem-estar</td>
                <td>Diversão, acessibilidade</td>
                <td>Corridas populares, caminhadas, jogos recreativos</td>
            </tr>
            <tr>
                <td>Rendimento</td>
                <td>Busca por resultados competitivos</td>
                <td>Excelência técnica, performance</td>
                <td>Treinamento intenso, competição formal</td>
                <td>Jogos olímpicos, campeonatos profissionais</td>
            </tr>
        </tbody>
    </table>
    <br>
    É importante ressaltar que as manifestações desportivas não são estanques e podem se interligar. Por exemplo, um atleta de alto rendimento pode ter iniciado sua trajetória em um programa esportivo educacional, e um evento de participação pode ter um caráter educativo, promovendo a inclusão social. A diversidade de manifestações desportivas garante que o esporte atenda às necessidades e interesses de diferentes públicos, contribuindo para uma sociedade mais saudável, justa e engajada.`);
});

document.getElementById('faq3').addEventListener('click', function () {
    showFaqContent(`Os selos da Lei de Incentivo ao Esporte (LIE) são um reconhecimento oficial concedido pelo Ministério do Esporte a proponentes, projetos e patrocinadores/doadores que contribuem para o desenvolvimento do esporte no Brasil.<br><br>
    <ul>
        <li>Demonstram a qualidade e o impacto dos projetos e iniciativas esportivas.</li>
        <li>Incentivam a participação e o investimento no esporte nacional.</li>
        <li>Fortalecem a imagem e a reputação das entidades e empresas que os recebem.</li>
    </ul><br>
    Para obter mais informações sobre os selos da LIE, acesse: <a href="https://www.gov.br/esporte/pt-br/acoes-e-programas/lei-de-incentivo-ao-esporte/selo-lie/" target="_blank">Selo LIE - Mais Informações</a>.`);
});

document.getElementById('faq4').addEventListener('click', function () {
    showFaqContent(`O valor que você pode doar para projetos esportivos depende do seu imposto de renda devido. A Lei de Incentivo ao Esporte permite que pessoas físicas abatam até 7% do imposto devido com doações para projetos esportivos.<br><br>
    Para calcular o valor máximo que você pode abater, utilize o simulador da Receita Federal: <a href="https://www27.receita.fazenda.gov.br/simulador-irpf/" target="_blank">Simulador IRPF</a>.<br><br>
    Exemplo: Se você tiver 1000 reais de imposto devido, poderá abater 70 reais (7% de 1000), restando 930 reais a pagar no final da declaração.`);
});

function showFaqContent(content) {
    const faqContentDiv = document.getElementById('faqContent');
    faqContentDiv.innerHTML = content;
    faqContentDiv.classList.remove('hidden');
}

// Carrega os dados ao iniciar
window.onload = loadSheetData;
