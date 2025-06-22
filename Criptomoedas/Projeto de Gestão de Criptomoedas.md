# Projeto: Sistema de Registro e Monitoramento de Estratégias em Criptomoedas

## 🎯 Objetivos Principais:

1. **Registrar compras e vendas** (simuladas ou reais) com todos os dados necessários.
2. **Analisar estratégias** (por par de moedas, período, tipo de estratégia, capital investido, etc.).
3. **Obter dados de mercado em tempo real** (via API da Binance: preço atual, book, volume, etc.).
4. **Permitir ajuste e criação de estratégias** (teto/base, capital alocado, gestão de lucro, etc.).
5. **Visualizar dashboards de performance** (gráficos por estratégia, lucro/prejuízo, drawdown, taxas, etc.).


### 📌 Princípios Operacionais para Proteção de Capital:

- Nunca vender no prejuízo só por evento de mercado (como saída de canal).
- Toda venda deve ser sempre **com lucro mínimo garantido após taxas**.
- O sistema deve sinalizar e acompanhar operações fora do canal, mas não forçar liquidação no prejuízo.
- Lucros não reinvestidos por padrão, a não ser que o operador configure manualmente.


## 🛠️ Tecnologias sugeridas:

- **Linguagem Backend:** Python (com Flask ou FastAPI) ou PHP (Laravel)
- **Banco de Dados:** MySQL ou PostgreSQL
- **Frontend:** React ou Vue.js (ou Blade/Laravel caso queira começar mais simples)
- **Integração API:** Binance REST API
- **Gráficos:** Chart.js ou ApexCharts
- **Agendamento de tarefas:** Celery + Redis (Python) ou Laravel Scheduler (PHP)


## 🧱 Estrutura do Banco de Dados (Exemplo Simplificado)

### Tabelas Principais:

- **moedas**  
    (Pares operados: BTC/USDT, ETH/USDT, etc.)
- **estrategias**  
    (Nome, tipo, parâmetros como teto/base, capital máximo, etc.)
- **operacoes**  
    (Tipo: compra/venda/simulação, par, quantidade, preço, taxa, data/hora, id da estratégia)
- **resultados**  
    (Lucro/Prejuízo por estratégia, saldo acumulado, capital disponível, capital separado, etc.)
- **cotacoes**  
    (Histórico de preço de mercado para consultas futuras e backtesting)


## 🧑‍💻 Funcionalidades Essenciais (MVP)

- Cadastro manual de operações (compra/venda/simulação)
- Consulta de cotações em tempo real via Binance API
- Registro automático das taxas de operação
- Relatório simples por estratégia e por par de moedas
- Exportação CSV dos resultados
- Gráficos básicos de desempenho no período


## 📈 Funcionalidades Desejáveis (Fase 2) – Estratégias e Análise:

- Cadastro e ajuste de estratégias (ex.: canal de teto/base, controle de capital)
- Simulação de estratégias em tempo real com base nos preços da Binance
- Separação de lucro realizado e capital alocado
- Análise de impacto das taxas da Binance nos lucros
- Gráficos de comparação entre estratégias
- Dashboard de performance por período (diário, semanal, mensal)


## 🚀 Funcionalidades Avançadas (Futuro) - Automações

- Envio automático de ordens reais para Binance
- Modo “Paper Trading” (simulação 100% automática com base nos preços ao vivo)
- Controle de risco por stop-loss, trailing stop, etc.
- Alertas por Telegram, Email ou WhatsApp
- Backtesting com histórico de anos anteriores


## ⚙️ Funcionalidades Estruturais – Garantia de Disponibilidade e Integridade Operacional

Para garantir o correto funcionamento do sistema e a integridade dos registros de operações, será implementado um **módulo de verificação automática de integridade e disponibilidade**, executado de forma programada (exemplo: diariamente ou em ciclos configuráveis).

### Verificações de Integridade das Operações

O sistema deverá executar um **check automático diário** com os seguintes critérios:

- ✅ **Toda compra registrada deve ter uma venda futura programada**, sempre que a estratégia exigir uma saída obrigatória (como no caso das posições fora do canal com lucro mínimo programado).
- ✅ **Toda venda registrada deve ter uma compra correspondente**, garantindo que não existam registros de vendas "órfãs" ou operações inconsistentes.
- ✅ **Nenhuma posição pode permanecer com status indefinido**.  
    Se houver qualquer operação com status inconsistente (ex.: sem status ou status inválido), o sistema deverá **registrar a falha e disparar um alerta para o operador corrigir manualmente**.

### Monitoramento de Disponibilidade da API da Binance

Como o sistema depende diretamente da **API da Binance para consultas de cotações em tempo real**, será implementado um mecanismo de **tolerância a falhas de conexão**.

Em caso de falha na consulta da cotação:

- ✅ O sistema deverá realizar **até X tentativas consecutivas de reconexão**, com um intervalo progressivo entre as tentativas (exemplo: estratégia de retry exponencial ou com backoff).
- ✅ Se todas as tentativas falharem, a posição que estiver em monitoramento ativo (ou aguardando venda programada) deverá ser **marcada com o status: "Monitoramento Suspenso Temporário"**.
- ✅ Além disso, o sistema deverá **disparar um alerta para o operador**, informando o motivo da suspensão e solicitando que o acompanhamento manual seja iniciado até a normalização da API.
- ✅ O sistema também deve registrar a falha em um **log de eventos críticos**, permitindo auditoria posterior e análise de estabilidade da integração com a Binance.

### Finalidade dessa Estrutura

Essas funcionalidades têm o objetivo de:

- **Garantir a disponibilidade contínua das operações**, mesmo em cenários de falha temporária da API externa.
- **Preservar a integridade dos dados**, evitando registros incompletos ou incoerentes.
- **Minimizar riscos operacionais** causados por falhas de comunicação, interrupções na API da Binance ou erros de execução de estratégia.
- **Fornecer visibilidade ao operador**, com alertas imediatos para qualquer anomalia.

---
## Exemplo de Estratégia a ser configurada no sistema

#### Estratégia: **Operação por Canal de Preço com Controle de Capital e Filtro de Valorização/Desvalorização**

### Objetivo da Estratégia

Operar dentro de um canal de preço previamente identificado, buscando maximizar a assertividade das entradas e saídas, utilizando uma parcela fixa do capital da banca, e **não reinvestindo os lucros gerados nas operações**.

### Parâmetros Operacionais

|Parâmetro|Valor|
|---|---|
|**Timeframe de Análise**|Gráfico de 4 horas (H4)|
|**Canal de Preço**|Mínimo: 100.489 / Máximo: 110.626|
|**Capital Alocado**|20% da banca disponível (valor fixo, sem reinvestimento de lucros)|
|**Cálculo de Lucro**|Lucros gerados nas operações não são incorporados ao capital de operação (lucro separado)|
|**Taxas**|Considerar as taxas de operação da Binance ao calcular os limites de venda|
### Regras de Compra (Entrada)

- A compra será disparada **apenas quando houver uma valorização significativa** a partir do **menor valor registrado dentro do canal no período recente**.
- O operador busca com isso **evitar compras em movimento lateral ou de queda contínua**, e só entrar após sinais de reversão positiva.
- Exemplo de critério (ajustável no sistema futuramente):
    - **% de valorização mínima** a partir do fundo: Exemplo: +1% ou +2% (definível por configuração).

### Regras de Venda (Saída)

- A venda será disparada quando houver uma **desvalorização percentual a partir do topo mais recente dentro do canal**, desde que:
    1. O valor atual **seja maior que o preço da compra + taxas** (para evitar saídas no prejuízo).
    2. Exemplo de critério de saída:
        - **Queda de -1% ou -2% a partir do topo**, ajustável via sistema.

### Gestão de Capital

- Capital **fixo por estratégia:** 20% da banca.
- Lucros acumulados **não são reaplicados**. O capital base permanece o mesmo até nova configuração.
- Caso o capital da banca sofra variação (por saques ou perdas em outras estratégias), o valor de 20% pode ser recalculado periodicamente.

Suponha:

- Banca atual: **10.000 USDT**
- Capital para a estratégia: **2.000 USDT**
- Compra: ocorre se o preço sobe **2% a partir do fundo das últimas horas no canal**.
- Venda: ocorre se o preço cai **2% a partir do topo**, desde que respeite o mínimo de lucro (superando taxas).

### Possíveis Campos no Sistema para essa Estratégia:

| Campo                            | Tipo     | Exemplo                        |
| -------------------------------- | -------- | ------------------------------ |
| Nome da Estratégia               | Texto    | Canal H4 - Controle de Capital |
| Par Operado                      | Seleção  | BTC/USDT                       |
| Capital Alocado (%)              | Número   | 20 (saldo da banca na config.) |
| Considera Lucros?                | Booleano | Não                            |
| Limite Inferior (Base)           | Número   | 100.489                        |
| Limite Superior (Teto)           | Número   | 110.626                        |
| % Valorização Mínima para Compra | Número   | 2                              |
| % Desvalorização para Venda      | Número   | 2                              |
| Critério de Venda Mínima         | Cálculo  | Preço Compra + Taxas           |
### Benefícios dessa Estratégia:

- **Proteção de Capital:** Uso de apenas uma parcela fixa da banca.
- **Evita operações impulsivas:** Entradas somente após confirmação de valorização.
- **Realização de Lucros Controlada:** Saídas programadas considerando oscilações de curto prazo dentro do canal.

### Problema Evitado:

Evitar a permanência de posições compradas abertas indefinidamente quando o preço **sai do canal de operação**, deixando o capital exposto ao risco sem uma saída programada.

### Relação entre Estratégia, Operações e Relatório

Estratégia → Gera → Operações → Gera → Relatórios

### Etapas

| Etapa | Ação                                                        |
| ----- | ----------------------------------------------------------- |
| 1     | Operador configura estratégia                               |
| 2     | Sistema monitora preço via Binance API                      |
| 3     | Sistema avalia critérios de entrada                         |
| 4     | Se critérios atingidos → Registra compra                    |
| 5     | Sistema acompanha posição (dentro ou fora do canal)         |
| 6     | Se preço atingir o alvo de venda com lucro → Registra venda |
| 7     | Sistema atualiza relatórios                                 |

---
### Nova Regra de Monitoramento: **Controle de Posições Abertas**

#### Para cada compra realizada (real ou simulada), o sistema deverá:

- Registrar os seguintes dados:
    - Par de moeda
    - Preço de compra
    - Quantidade
    - Data/hora
    - Taxas
    - Estratégia vinculada
    - Status da operação: **Aberta** ou **Encerrada**
- Manter a posição **marcada como "aberta"** até que:
    1. Uma venda seja executada de forma programada pela estratégia (ex: queda de % a partir do topo, dentro do canal), ou
    2. Uma venda de emergência (forçada) seja registrada caso o preço **ultrapasse o limite inferior ou superior do canal**.

### Nova Regra de Saída: **Venda por Saída de Canal (Stop Fora do Canal)**

Sempre que o preço da moeda **sair dos limites do canal (abaixo da base ou acima do teto)**, e existirem compras abertas associadas àquela estratégia/par, o sistema deverá:

**Jamais realizar uma venda no prejuízo só porque o preço saiu do canal.**

✅ Toda posição aberta só será encerrada com uma venda **acima do preço de compra + taxa mínima de lucro**. **Mesmo que o preço da moeda saia do canal de operação (rompa o teto ou a base), o sistema não fará venda imediata a preço de mercado.**  
✅ Se o preço estiver fora do canal, a estratégia deverá **registrar uma venda com o mínimo lucro esperado**. A estratégia será: **registrar uma venda futura, programada, no mínimo lucro esperado**, considerando o preço de compra + taxas + lucro mínimo.

### Regra de Gestão para Saída de Canal

|Situação|Ação|
|---|---|
|O preço rompe o limite inferior (base) ou superior (teto) do canal|O sistema verifica se há posições abertas daquela estratégia/par|
|Existe posição aberta e o preço atual ainda está abaixo do valor de venda com lucro|O sistema registra internamente que aquela posição está “fora do canal” e **agenda uma venda futura com o preço alvo mínimo de lucro**|
|O preço posteriormente atinge o valor de venda programado|A venda é executada e registrada com o status "Venda programada após saída do canal com lucro mínimo"|
### Campos Extras Necessários na Base de Dados:

|Campo|Tipo|Exemplo|
|---|---|---|
|Status da Posição|Enum|Aberta / Venda Programada / Encerrada|
|Motivo da Venda|Texto|Venda programada por saída do canal|
|Preço alvo da venda|Decimal|Exemplo: 102.300 USDT|
|Data da saída do canal|Datetime|Quando a cotação saiu do canal|
|Data de programação da venda|Datetime|Quando o sistema registrou a venda programada|
|Condição mínima de lucro|Decimal (ou %)|Exemplo: 0,5% acima do preço de compra + taxas|
### Fluxo Exemplo de Evento:

1. **Compra feita:**  
    Par BTC/USDT a 102.000 USDT.
2. **Cotação atual:**  
    Preço cai e rompe o limite inferior do canal: chega a 100.300 USDT.
3. **Ação do sistema:**  
    Detecta que há uma posição aberta fora do canal → Sistema calcula:  
    "Preço de venda mínima aceitável = Preço de compra + taxas + lucro mínimo = 102.300 USDT"
4. **Venda programada:**  
    O sistema registra a **venda programada**.
5. **Quando o preço atinge o alvo:**  
    Exemplo: o preço sobe para 102.350 USDT → **Venda é executada e registrada**.
6. **Resultado:**  
    O relatório da estratégia mostrará que a venda foi **pós saída de canal**, mas sempre **com lucro**.

### Novos Comportamentos Obrigatórios no Sistema:

- Sistema **nunca** executa vendas no prejuízo por rompimento de canal.
- Toda saída de canal dispara uma programação automática de venda com lucro mínimo.
- Possibilidade de listar no painel:  
    ✅ "Posições fora do canal aguardando venda com lucro mínimo".

Aqui está a lista de **relatórios esperados**, já considerando as regras atualizadas para **gestão de posições abertas, controle de saída de canal com venda programada e o acompanhamento das estratégias**:

---
# 📈 Relatórios Esperados – Sistema de Monitoramento de Criptomoedas


## 📊 Relatórios de Performance por Estratégia

- **Lucro/Prejuízo Total por Estratégia**
- **Quantidade total de operações por estratégia**
- **Taxa de acerto (% de operações com lucro)**
- **Lucro acumulado no período (Diário / Semanal / Mensal)**
- **Capital atualmente alocado em cada estratégia**
- **Capital total movimentado (volume operado)**


## 📉 Relatórios de Operações Individuais

- **Histórico detalhado de todas as operações (Compra/Venda)**
    - Data e hora
    - Par de moeda
    - Tipo de operação (Compra / Venda)
    - Estratégia utilizada
    - Preço de entrada
    - Preço de saída
    - Lucro ou prejuízo
    - Percentual de ganho por operação
    - Taxas pagas na operação
    - Motivo da venda (Venda por critério de estratégia / Venda programada por saída de canal / Outro motivo definido)


## 📋 Relatório de Posições Abertas

- **Lista de todas as posições atualmente abertas**
    - Data da compra
    - Preço de compra
    - Quantidade
    - Status (Dentro do canal / Fora do canal aguardando venda programada)
    - Preço alvo mínimo programado para venda
    - Tempo de exposição (dias desde a compra)


## 📉 KPIs Sugeridos

| Indicador                     | Descrição                                 |
| ----------------------------- | ----------------------------------------- |
| Total de Lucro Acumulado      | Por estratégia, período ou par            |
| % de Acerto                   | Operações lucrativas x total de operações |
| Lucro Médio por Operação      | Média de ganho                            |
| Tempo Médio de Posição Aberta | Tempo de exposição ao risco               |
| Lucro Total vs Taxas Pagas    | Para medir eficiência da operação         |


## 📌 Relatório de Posições Fora do Canal (Em Recuperação)

- Todas as posições que estão **fora do canal de operação**, mas que **ainda aguardam atingir o preço mínimo de lucro para venda**.

Campos sugeridos:

|Campo|Exemplo|
|---|---|
|Par|BTC/USDT|
|Data da Compra|2025-06-22 10:00|
|Preço de Compra|102.000 USDT|
|Preço atual|100.300 USDT|
|Preço Alvo Programado|102.300 USDT|
|Tempo fora do canal|3 dias|
|Status|Aguardando recuperação|


## 📊 Relatório Comparativo entre Estratégias

- **Comparativo de performance entre diferentes estratégias**
    - Lucro acumulado por estratégia
    - % de acerto por estratégia
    - Drawdown máximo por estratégia
    - Tempo médio de exposição das operações por estratégia


## 📅 Relatórios de Evolução Temporal

- **Gráfico de Evolução de Lucro no Tempo**
    - Linha de evolução diária, semanal ou mensal
- **Histórico de saldo de banca**
    - Exibir o crescimento ou queda do capital total ao longo do tempo
- **Histórico de Capital Alocado por Estratégia**


## 📈 Relatório de Impacto das Taxas

- **Total de taxas pagas por período**
- **% das taxas sobre o lucro total**
- **Estratégias com maior impacto de taxas**


## 📌 Relatório de Lucro por Par de Moedas

- Exibir **lucro/prejuízo acumulado por cada par de moedas operado**  
    (BTC/USDT, ETH/USDT, etc.)


## 🚩 Relatório de Riscos e Exposições

- **Tempo médio de permanência de posições abertas fora do canal**
- **Quantidade de operações que precisaram de venda programada por saída de canal**
- **Tempo médio para recuperação de preço após saída de canal**

---
## Glossário

|Termo|Definição|
|---|---|
|**Canal**|Limite de preço superior e inferior dentro de um timeframe. Define a faixa operacional da estratégia.|
|**Posição Aberta**|Compra (ou venda, no caso de posições short) que ainda não foi encerrada por uma operação de sentido contrário.|
|**Venda Programada**|Venda agendada para execução futura, somente quando o preço atingir o alvo mínimo de lucro estipulado pela estratégia.|
|**Banca**|Capital total disponível para operações. Pode ser dividido entre diferentes estratégias ou reservado parcialmente.|
|**Estratégia**|Conjunto de regras predefinidas que orientam quando comprar, vender, alocar capital e gerenciar risco.|
|**Fora do Canal**|Situação onde o preço atual está fora dos limites estabelecidos no canal de operação da estratégia.|
|**Mercado à Vista (Spot Market)**|Operações de compra e venda com liquidação imediata. A moeda é realmente adquirida ou vendida no momento da operação.|
|**Mercado Futuro (Futures Market)**|Operações baseadas em contratos que representam um ativo futuro. Permite alavancagem e posições short.|
|**Alavancagem (Leverage)**|Recurso que permite operar com valores maiores do que o capital disponível, aumentando potencial de ganho e risco.|
|**Cross Margin**|Modelo de margem onde todo o saldo disponível na conta é usado como garantia para todas as posições abertas, aumentando o risco de liquidação total.|
|**Isolated Margin**|Modelo de margem onde apenas o valor alocado na posição é considerado como garantia, limitando o risco àquela posição específica.|
|**Stop Loss**|Ordem automática para encerrar uma posição ao atingir um nível de perda predeterminado, evitando maiores prejuízos.|
|**Stop Gain / Take Profit**|Ordem automática para encerrar uma posição ao atingir um nível de lucro predeterminado, garantindo o ganho.|
|**Order Limit (Ordem Limitada)**|Ordem de compra ou venda com um preço específico definido. Só será executada se o mercado atingir esse preço ou melhor.|
|**Order Market (Ordem a Mercado)**|Ordem de compra ou venda executada imediatamente ao preço disponível no livro de ordens. Não há garantia de preço exato.|
|**Slippage**|Diferença entre o preço esperado de execução de uma ordem e o preço real executado, comum em ordens a mercado em momentos de alta volatilidade.|
|**Spread**|Diferença entre o preço de compra (ask) e o preço de venda (bid) no livro de ofertas. Quanto menor o spread, mais líquida é a moeda.|
|**Drawdown**|Medida da queda máxima do capital durante um período. Indica o risco e a volatilidade da estratégia.|
|**Volume**|Quantidade total de negociação de um ativo em determinado período. Importante para avaliar a liquidez de uma moeda.|
|**Book de Ofertas (Order Book)**|Lista pública de ordens de compra e venda abertas no mercado, mostrando preços e quantidades disponíveis.|
|**Liquidity (Liquidez)**|Facilidade com que um ativo pode ser comprado ou vendido no mercado sem afetar significativamente o preço.|
|**Volatilidade**|Grau de variação dos preços de um ativo ao longo do tempo. Estratégias podem ser mais ou menos sensíveis à volatilidade.|
|**Paper Trading**|Simulação de operações em ambiente virtual, utilizando dados reais de mercado, mas sem movimentação de capital real.|
|**Backtesting**|Processo de testar uma estratégia utilizando dados históricos para avaliar como ela teria se comportado no passado.|
|**Long Position (Posição Long)**|Operação que aposta na alta do ativo: compra a um preço esperando vender mais caro depois.|
|**Short Position (Posição Short)**|Operação que aposta na queda do ativo: vende primeiro para recomprar mais barato depois. Só disponível em mercados futuros ou com margens específicas.|
|**Realized P&L (Lucro/Prejuízo Realizado)**|Lucro ou perda efetivamente obtida após o encerramento de uma posição.|
|**Unrealized P&L (Lucro/Prejuízo Não Realizado)**|Lucro ou perda "em aberto", calculado com base no preço atual, mas ainda não efetivado.|
|**Taxa de Transação**|Valor cobrado pela corretora (ex.: Binance) em cada operação de compra ou venda, geralmente um percentual sobre o valor negociado.|