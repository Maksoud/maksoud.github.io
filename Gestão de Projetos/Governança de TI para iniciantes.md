### [Sumário](<https://maksoud.github.io/Sumário>)

### Governança de TI: um guia para quem está começando

Toda empresa tem governança de TI. A diferença é se ela foi **escrita** ou se ela é apenas o hábito de quem grita mais alto.

Onde não existe uma regra formal sobre quem aprova a compra de um software, alguém aprova mesmo assim — normalmente o diretor com mais influência naquele mês. Onde não existe política de acesso, os acessos são concedidos assim mesmo: por mensagem, "só dessa vez", e nunca revogados. Onde não existe critério de priorização, as demandas são priorizadas assim mesmo — pela ordem de insistência de quem pediu.

Governança de TI não é sobre criar controle onde não havia. É sobre **tornar visível e intencional um controle que já existe de forma informal, invisível e, quase sempre, injusta**.

Este texto é um mapa para quem está entrando na área: o que a disciplina realmente é, o que estudar, como é o dia a dia de verdade, o que cai em entrevista e o que esperar do ambiente corporativo.

---

## 1. A distinção que define tudo: governança não é gestão

Se você guardar uma única ideia deste artigo, guarde esta. É também, com folga, a pergunta mais frequente em entrevistas da área.

**Governança decide. Gestão executa.**

| | **Governança** | **Gestão** |
| :--- | :--- | :--- |
| Pergunta central | *Estamos fazendo as coisas certas?* | *Estamos fazendo do jeito certo?* |
| Quem exerce | Conselho, alta direção, comitês | Gerentes, coordenadores, times |
| Ciclo (COBIT) | **EDM** — *Evaluate, Direct, Monitor* | **PBRM** — *Plan, Build, Run, Monitor* |
| Horizonte | Estratégico e plurianual | Tático e operacional |
| Produto do trabalho | Direção, política, alçada, decisão de investimento | Entrega, projeto, chamado, serviço no ar |
| Analogia | O conselho define o destino do navio | O comandante conduz o navio até lá |

Um exemplo prático da diferença: decidir que a empresa vai migrar para nuvem, com qual apetite de risco e qual teto de investimento, é **governança**. Executar a migração dentro do prazo e do orçamento é **gestão**. São duas pessoas diferentes, em duas reuniões diferentes, respondendo a duas perguntas diferentes.

> **Corolário importante:** governança de TI não é uma disciplina de TI. É um braço da **governança corporativa**. Ela existe porque a tecnologia virou risco de negócio — e risco de negócio é assunto de conselho, não de sala de servidores.

### Os três objetivos que justificam a área

Todo framework de governança, no fundo, persegue as mesmas três coisas:

1. **Entrega de valor** — a TI precisa produzir benefício mensurável para o negócio, não apenas funcionar.
2. **Otimização de risco** — o risco tecnológico precisa ser conhecido, aceito conscientemente por quem tem alçada e tratado.
3. **Otimização de recursos** — dinheiro, pessoas e capacidade são finitos e precisam ir para onde rendem mais.

Quando alguém perguntar "para que serve governança de TI?", essa é a resposta de três linhas.

---

## 2. O que pesquisar: o mapa dos frameworks

O maior erro do iniciante é tentar decorar uma sopa de siglas em ordem alfabética. O caminho melhor é entender **qual pergunta cada framework responde**.

### Governança propriamente dita

| Framework | Para que serve |
| :--- | :--- |
| **COBIT 2019** | O framework de governança por excelência. Traz 40 objetivos distribuídos em 5 domínios, separa explicitamente governança (EDM) de gestão (APO, BAI, DSS, MEA) e usa *design factors* para adaptar ao contexto da empresa |
| **ISO/IEC 38500** | A norma internacional de governança corporativa de TI. Curta, principiológica, boa para entender o "porquê" |
| **NIST CSF 2.0** | Framework de cibersegurança que, na versão 2, ganhou a função **Govern** ao lado de Identify, Protect, Detect, Respond e Recover |

### Gestão de serviços — o operacional

| Framework | Para que serve |
| :--- | :--- |
| **[[ITIL 4]]** | O vocabulário do dia a dia: incidente, problema, mudança, requisição, catálogo de serviços, SLA. É a porta de entrada mais acessível da área |
| **ISO/IEC 20000** | A norma certificável de gestão de serviços de TI |

### Segurança e privacidade

| Norma | Para que serve |
| :--- | :--- |
| **ISO/IEC 27001** | Sistema de Gestão de Segurança da Informação (SGSI) — a norma certificável |
| **ISO/IEC 27002** | O catálogo de controles que dá corpo à 27001 |
| **LGPD** | Lei 13.709/2018. Obrigatória no Brasil. Define bases legais, direitos do titular e o papel do encarregado (DPO) |
| **GDPR** | O equivalente europeu. Relevante se a empresa trata dados de residentes na União Europeia |

### Projetos, portfólio e requisitos

PMBOK/PMI e PRINCE2 cuidam da governança de projetos; a ponte com análise de negócio está em [[Entendendo o BABOK v3]], e a discussão sobre cadência e entrega em [[Fundamentos Ágeis]]. Vale saber que governança e agilidade **não são opostos** — o que muda é a frequência e o formato do controle, não a existência dele.

### Regulatório brasileiro — o diferencial que quase ninguém estuda

Este é o bloco que separa um candidato genérico de um candidato preparado para o mercado local:

- **SOX (Lei Sarbanes-Oxley)** e os controles **ITGC** — obrigatórios em empresas de capital aberto nos EUA e em suas subsidiárias brasileiras. Quem trabalha em multinacional convive com auditoria de ITGC todo ano.
- **Resolução BACEN nº 4.893/2021** — política de segurança cibernética e contratação de serviços em nuvem para instituições financeiras.
- **Normas setoriais** — SUSEP (seguros), ANS (saúde suplementar), ANEEL (energia).
- **Setor público** — IN SGD/ME nº 94/2022 sobre contratações de TI, acórdãos do TCU e o Marco Civil da Internet. Para quem mira concurso, este é o bloco mais cobrado.

> A regra que vale para todos eles: **ninguém implanta um framework inteiro**. O COBIT chama isso de *tailoring*; o ITIL, de "adotar e adaptar". Uma empresa de 80 pessoas que tentar implantar os 40 objetivos do COBIT vai produzir papel, não governança.

---

## 3. O que a governança vira na prática: os artefatos

Aqui a teoria encontra a mesa de trabalho. Estes são os documentos e mecanismos que você vai ler, escrever, revisar e cobrar.

### A hierarquia normativa

Confundir estes quatro níveis é o erro mais comum de quem está começando:

| Nível | O que é | Exemplo |
| :--- | :--- | :--- |
| **Política** | O "o quê" e o "por quê". Curta, estável, aprovada pela alta direção | "Todo acesso a sistemas corporativos é concedido pelo princípio do menor privilégio" |
| **Norma** | O "quanto" e o "quando". Define parâmetros mensuráveis | "Senhas devem ter no mínimo 12 caracteres e ser trocadas a cada 180 dias" |
| **Procedimento** | O "como". Passo a passo do processo | "Fluxo de solicitação de acesso: abertura de chamado, aprovação do gestor, provisionamento" |
| **Instrução de trabalho** | O "como", na tela | "Como criar um usuário no Active Directory" |

Política que desce ao nível de configuração de tela envelhece em três meses. Procedimento que não se ancora numa política não tem autoridade para ser cobrado.

### Comitês e alçadas

- **Comitê de TI** (ou Comitê Diretor) — prioriza investimento e portfólio. É onde a governança acontece de fato.
- **CAB** (*Change Advisory Board*) — avalia e aprova mudanças de maior risco.
- **Comitê de Segurança da Informação** — trata riscos, incidentes e exceções à política.

Comitê sem pauta preparada, sem ata e sem acompanhamento da deliberação anterior é reunião, não comitê.

### Matriz RACI

Define, para cada atividade, quem é **R**esponsável pela execução, quem **A**prova (e só pode haver um), quem é **C**onsultado antes e quem é **I**nformado depois. É a ferramenta que resolve a frase mais cara do mundo corporativo: *"achei que era você quem ia fazer"*.

### Serviços e níveis de serviço

- **Catálogo de serviços** — a lista do que a TI entrega, em linguagem de negócio.
- **SLA** (*Service Level Agreement*) — o acordo com o cliente ou com a área de negócio.
- **OLA** (*Operational Level Agreement*) — o acordo interno entre áreas de TI que sustenta o SLA.
- **UC** (*Underpinning Contract*) — o contrato com o fornecedor externo que sustenta os dois anteriores.

A cadeia importa: prometer 99,9% ao negócio quando o contrato do datacenter garante 99% é assumir um risco que não se pode cumprir.

### Gestão de riscos

O ciclo é sempre o mesmo: identificar, analisar, avaliar, tratar e monitorar. As quatro respostas possíveis a um risco:

| Resposta | Quando usar |
| :--- | :--- |
| **Mitigar** | Reduzir probabilidade ou impacto com um controle |
| **Transferir** | Passar o impacto financeiro adiante (seguro, contrato, terceirização) |
| **Evitar** | Não fazer a atividade que gera o risco |
| **Aceitar** | Conviver com ele — desde que formalmente, por quem tem alçada |

Para priorizar o que tratar primeiro, a [[Matriz GUT]] (Gravidade, Urgência, Tendência) funciona bem como apoio quando ainda não existe uma matriz de risco formal implantada.

### Controles de acesso

Três conceitos que caem em prova e em entrevista:

- **Menor privilégio** — cada pessoa recebe o mínimo de acesso necessário para o trabalho.
- **Segregação de funções (SoD)** — ninguém deve controlar sozinho um ciclo inteiro. Quem cadastra o fornecedor não pode ser quem aprova o pagamento; quem desenvolve não pode ser quem publica em produção.
- **Revisão periódica de acessos** — recertificação trimestral ou semestral em que cada gestor confirma quem ainda precisa de quê.

### Continuidade de negócio

- **BCP** (*Business Continuity Plan*) — como o negócio continua operando durante a crise.
- **DRP** (*Disaster Recovery Plan*) — como a TI se recupera tecnicamente.
- **RTO** (*Recovery Time Objective*) — quanto tempo o serviço pode ficar fora.
- **RPO** (*Recovery Point Objective*) — quanto de dado se pode perder.

RTO e RPO caem em entrevista com frequência quase garantida. A forma mais fácil de nunca mais confundir: **RTO é tempo de volta ao ar; RPO é tempo de dado perdido**. Um backup diário à meia-noite implica um RPO de até 24 horas, não importa quão rápida seja a restauração.

### Configuração e ativos

O **CMDB** é a base que registra os itens de configuração e suas relações. É a peça que permite responder "se esse servidor cair, quais serviços de negócio param?" — pergunta impossível de responder sem ela. Vale ver [[CMDB]] e [[CMDB - Terminology]] para o vocabulário.

### Financeiro de TI

| Conceito | Significado |
| :--- | :--- |
| **CAPEX** | Investimento em ativo, depreciado ao longo do tempo |
| **OPEX** | Despesa operacional recorrente — o modelo típico da nuvem |
| **TCO** | Custo total de propriedade, incluindo operação, licença, suporte e descomissionamento |
| ***Business case*** | O documento que justifica o investimento com benefício esperado |
| ***Chargeback / showback*** | Cobrar (ou apenas mostrar) às áreas de negócio o custo de TI que elas consomem |

### Indicadores

**KPI** mede desempenho (disponibilidade, tempo médio de atendimento, aderência a prazo). **KRI** mede exposição a risco (número de acessos privilegiados sem revisão, tempo médio de aplicação de correções críticas).

> A regra de ouro dos indicadores: **um indicador que não muda nenhuma decisão é apenas trabalho**. Antes de criar um, responda: quem vai olhar, com que frequência, e o que essa pessoa fará se o número piorar?

---

## 4. Como é o dia a dia de verdade

Esta é a parte que quase nenhum material de estudo conta, e é onde a expectativa do iniciante costuma se quebrar.

### O trabalho é articulação, não configuração

Você não vai configurar o firewall. Você vai garantir que exista **registro de quem configurou, com qual aprovação, sob qual justificativa e com qual data de revisão**. Cerca de 80% do tempo é conversa, documentação, evidência e acompanhamento; os outros 20% são análise técnica.

Para quem vem da operação, essa mudança é desconfortável no começo — a sensação de "não estar produzindo nada" é comum nos primeiros meses. O produto do seu trabalho é menos visível, mas aparece quando a auditoria passa sem apontamento, quando um incidente é contido porque o acesso já estava segregado, ou quando um projeto caro é barrado antes de começar porque o *business case* não se sustentava.

### Você será, estruturalmente, o "chato"

Governança pede documento, cobra prazo, barra exceção e faz perguntas incômodas em reunião. Isso gera atrito por definição — não por falha sua.

O que separa quem prospera de quem se queima na área não é o domínio das normas: é a **capacidade de negociar**. A postura que funciona é a de parceiro, não a de fiscal. Em vez de *"isso viola a política"*, o que abre porta é *"entendi a urgência; o caminho formal leva dois dias, e existe um procedimento de exceção emergencial — vamos por ele e registramos o risco?"*.

### A cadência do calendário

Governança tem um ritmo próprio, e entender esse ritmo ajuda muito a se organizar:

| Ritmo | Atividades típicas |
| :--- | :--- |
| **Diário / semanal** | Análise de mudanças (CAB), tratamento de exceções, apoio a demandas de auditoria, triagem de solicitações de acesso |
| **Mensal** | Comitê de TI, fechamento e publicação de indicadores, acompanhamento de planos de ação, revisão de incidentes relevantes |
| **Trimestral** | Revisão da matriz de riscos, recertificação de acessos, avaliação de desempenho de fornecedores |
| **Anual** | Auditoria externa, revisão do corpo normativo, ciclo orçamentário, teste do plano de recuperação de desastres, revisão do plano diretor de TI |

### Com quem você conversa

Governança é uma função-ponte. Suas contrapartes constantes serão auditoria interna, compliance, jurídico e o encarregado de dados (DPO), segurança da informação, financeiro (para orçamento e contratos), suprimentos (para fornecedores) e, o tempo todo, as áreas de negócio.

Isso significa que **vocabulário de negócio vale tanto quanto vocabulário técnico**. Saber traduzir "latência do banco de dados" em "o faturamento atrasa quatro horas e a equipe fiscal faz hora extra" é a habilidade mais valiosa da função.

### As ferramentas

- **ITSM**: ServiceNow, Jira Service Management, GLPI.
- **Indicadores**: Power BI, Excel — muito Excel, inclusive em empresas grandes.
- **Base normativa**: SharePoint, Confluence.
- **GRC**: Archer, MetricStream, SoftExpert — presentes em empresas de grande porte e no setor financeiro.

Não vale a pena estudar ferramenta antes do conceito. Ferramenta se aprende em duas semanas; critério, não.

---

## 5. Temas cruciais para uma entrevista

As perguntas abaixo cobrem a maior parte do que se pergunta a candidatos iniciantes e plenos. Mais importante do que a resposta certa é entender **o que o entrevistador está testando**.

| Pergunta | O que está sendo avaliado |
| :--- | :--- |
| *Qual a diferença entre governança e gestão de TI?* | A pergunta eliminatória. Responda com o par "decide × executa" e cite EDM × PBRM |
| *O que é o COBIT e quando você o usaria?* | Se você conhece o framework ou apenas a sigla |
| *Diferença entre política, norma e procedimento* | Maturidade documental |
| *O que é segregação de funções e por que importa?* | Noção de controle interno e prevenção a fraude |
| *Explique RTO e RPO* | Fundamento de continuidade |
| *Como você mediria se a TI está entregando valor?* | Se você pensa em negócio ou só em disponibilidade |
| *O que é um ITGC?* | Preparo para ambiente auditado (SOX) |
| *Como priorizar demandas com orçamento limitado?* | Raciocínio de portfólio: valor, risco, custo e capacidade |

### A pergunta que separa os candidatos

> *"Um diretor pede uma exceção à política de acesso, com urgência, para fechar o mês. O que você faz?"*

Essa pergunta não testa conhecimento — testa **postura**. A resposta fraca é "eu nego, a política é clara". A resposta igualmente fraca é "eu libero, ele é diretor".

A resposta forte reconhece que governança não é obstrução e que **exceção é um instituto legítimo, desde que formal**: entender a real necessidade, verificar se existe um caminho dentro da política e, se não existir, acionar o procedimento de exceção — com registro do risco, aceite formal de quem tem alçada para aceitá-lo, escopo mínimo necessário e **prazo de reversão definido**. Depois, levar o caso ao comitê: se a exceção se repete todo mês, o problema não é o pedido, é a política, que precisa ser revista.

### Perguntas comportamentais

Use o método **STAR** — Situação, Tarefa, Ação, Resultado — e tenha três histórias prontas: uma sobre conflito com uma área de negócio, uma sobre um erro seu e o que aprendeu com ele, e uma sobre uma melhoria que você propôs por conta própria. Vale revisar [[Perguntas e Respostas - Job Interview]] e [[Skills - Analista de TI]].

### O que perguntar ao entrevistador

Perguntar bem sinaliza senioridade. Três boas opções: *Qual o nível de maturidade atual da governança aqui?*; *A área responde à TI, ao compliance ou diretamente à diretoria?*; *Existe patrocínio da alta direção ou a governança ainda está sendo construída de baixo para cima?* — a resposta a esta última diz mais sobre o seu futuro cotidiano do que qualquer descrição de vaga.

---

## 6. Erros comuns de quem está começando

- **Tratar governança como burocracia.** Todo controle deve poder ser justificado por um risco concreto. Controle que não protege nada é custo puro — e o primeiro a ser abandonado.
- **Achar que a ferramenta implanta a governança.** Uma ferramenta cara sobre um processo ruim apenas executa o processo ruim mais rápido e com relatório bonito.
- **Copiar o framework inteiro.** Adapte ao porte, ao setor e à maturidade da empresa.
- **Criar política sem patrocínio da alta direção.** Sem alçada acima, a política é ignorada na primeira pressão de prazo e morre em três meses.
- **Medir o que é fácil em vez do que importa.** Número de chamados fechados não diz nada sobre valor entregue.
- **Escrever documento que ninguém lê.** Uma página que as pessoas seguem vale mais do que quarenta que ninguém abre.
- **Confundir formalismo com rigor.** O objetivo é que a decisão seja rastreável, não que o formulário esteja bonito.

---

## 7. Trilha de estudo e certificações

A ordem importa. Esta é uma escada, não uma lista de compras:

| Etapa | Certificação | Por quê |
| :--- | :--- | :--- |
| **1** | **ITIL 4 Foundation** | Porta de entrada mais acessível e a mais citada em vagas de nível júnior. Dá o vocabulário do dia a dia |
| **2** | **COBIT 2019 Foundation** | O salto para governança de fato. Consolida a distinção governança × gestão |
| **3** | **ISO/IEC 27001 Foundation** | Segurança da informação é hoje a maior fatia da agenda de governança |
| **4** | Especialização | **CISA** (auditoria de sistemas), **CRISC** (risco), **CGEIT** (governança sênior), **PMP/CAPM** (projetos) |

Além das certificações, três hábitos rendem mais do que parecem: ler as normas na fonte (a ISO/IEC 38500 tem poucas páginas), acompanhar acórdãos do TCU sobre contratações de TI (didáticos e gratuitos, mesmo para quem não visa o setor público) e ler relatórios de auditoria reais quando houver acesso a eles — nada ensina mais rápido do que ver um apontamento bem escrito.

---

## Resumo prático

- **Governança decide, gestão executa.** Governança pergunta *se estamos fazendo as coisas certas*; gestão, *se estamos fazendo do jeito certo*.
- Ela existe para três coisas: **entregar valor, otimizar risco e otimizar recursos**.
- Estude por função, não por sigla: **COBIT** para governar, **[[ITIL 4]]** para operar, **ISO 27001 e LGPD** para proteger, **SOX e normas do BACEN** para o contexto regulado brasileiro.
- Os artefatos do dia a dia são poucos e se repetem: **política, comitê, RACI, SLA, matriz de risco, revisão de acesso, indicador e plano de ação**.
- O trabalho é **80% articulação e evidência**, não configuração. Habilidade de negociação vale mais que norma decorada.
- Em entrevista, domine a diferença governança × gestão, a hierarquia normativa, segregação de funções e RTO × RPO. E prepare uma resposta madura para o pedido de exceção.
- Comece pelo **ITIL 4 Foundation** e suba a escada a partir dali.

> Nenhum controle sobrevive sem propósito. Antes de criar qualquer regra, política ou indicador, aplique as sete perguntas do [[5W2H]] — especialmente o **porquê**. Governança que não sabe responder por que existe vira exatamente aquilo que seus críticos dizem que ela é.

[Sumário](<https://maksoud.github.io/Sumário>)

[link de compartilhamento](<https://maksoud.github.io/Gest%C3%A3o%20de%20Projetos/Governan%C3%A7a%20de%20TI%20para%20iniciantes>)

<sup><sub>
Renée Maksoud - agosto de 2026
</sub></sup>
