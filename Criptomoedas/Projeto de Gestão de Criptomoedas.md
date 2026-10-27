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
- **Integração API:** Binance REST API (https://python-binance.readthedocs.io/en/latest/)
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
## Estratégias Segueridas

### - Estratégia Inicial: [Canal de Preço com Controle de Capital e Venda Programada com Lucro](https://correiarodrigues.com.br/notas/criptomoedas/estrategia-canal-de-preco-com-controle-de-capital-e-venda-programada-com-lucro/)

---
### 📈 [Relatórios](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/07-painel-e-relatorio/relatorios-sistema-de-monitoramento-de-criptomoedas/)

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

---


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/projeto-de-gestao-de-criptomoedas/)

<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>