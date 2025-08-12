Gostaria de fazer um sistema para operação de criptomoedas. Algo que eu possa ter várias contas da corretora Binance operando em diversas estratégias configuráveis para compra e venda de criptoativos. Negociando assim vários pares e gravando todas as operações em um banco de dados onde eu possa acompanhar relatórios de desempenho. Penso em colocar a estratégia para rodar em modo demonstrativo e assim me ajudar a escolher uma estratégia mais segura para operar com o meu capital da corretor. 

Já fiz um documento com o detalhamento do que preciso para a primeira estratégia, onde eu vou comprar na baixa e vender na alta em um determinado canal. Para isso, será necessário acompanhar a valorização e desvalorização do marcado para marcar o preço de compra e preço de venda, garantindo assim um maior ganho nas negociações. 

Inicialmente eu pretendo criar um MVP para gerar dados para o banco onde eu vou acompanhar posteriormente nos relatórios. O código será gerado em Python, pois assim eu vou reforçar o meu conhecimento inicial e também possibilitará o uso de bibliotecas de análise de dados no futuro.

Como a IA consegue me ajudar a alcançar esse desejo e como eu deveria seguir com a preparação dos prompts e futuras interações com bots que irão me auxiliar no desenvolvimento desse sistema que possui uma certa complexidade. Um grande impedimento que eu percebi foi a quantidade de informações que estou passando no prompt e gerando com isso muita informação inútil ou duplicada. Como eu posso dividir esse sistema em partes menores para que a IA me auxilie na criação sem que eu perca muito tempo preparando prompts que muitas vezes são mal compreendidos?

---

Adorei o plano — é ambicioso, mas super viável se a gente quebrar em pedaços pequenos e “ensináveis” pra IA. Vou te mostrar 3 coisas, bem objetivas:

1. um recorte de MVP com arquitetura mínima;
2. como dividir o trabalho em “tickets” que a IA entende;
3. modelos de prompt prontos (copiar/colar) pra você iterar rápido sem ruído.

Se quiser, já posso gerar o esqueleto do projeto em Python na próxima mensagem.

---

# 1) MVP técnico (primeira iteração enxuta)

**Objetivo do MVP:** rodar 1 estratégia de “compra na baixa / venda na alta dentro de um canal” em **paper trading** (ou testnet da Binance), em poucos pares, salvando tudo no banco e gerando métricas básicas.

**Stack sugerida (simples e robusta):**

- Python 3.11+
- **ccxt** (acesso Binance spot/testnet)
- **pandas** (manipulação de dados)
- **SQLAlchemy + Alembic** (ORM + migrações)
- **PostgreSQL** (ou **SQLite** pra começar local)
- **pydantic** (validação de configs)
- **loguru** (logs)
- (Opcional) **FastAPI** + **Uvicorn** só pra expor relatórios/healthcheck depois

**Módulos do MVP:**

- `exchange_adapter/`
    - baixa candles (klines), saldo (paper), envia ordens (paper/testnet), normaliza erros

- `marketdata/`
    - cacheia candles por par/timeframe; persistência em DB

- `strategy/`
    - sua lógica do canal: parâmetros (timeframe, largura do canal, z-score/ATR, alvos e stops), sinais de buy/sell

- `order_manager/`
    - simula execução (paper) com taxas/slippage; gerencia posição por par

- `risk/`
    - sizing (p.ex. % do saldo), stop-loss, max posição por par, max perdas por dia

- `persistence/`
    - schema (tabelas: accounts, pairs, candles, orders, trades, positions, equity_curve, runs, configs)

- `reporting/`
    - métricas: PnL, win rate, drawdown, sharpe simplificado, curva de capital

- `scheduler/runner/`
    - loop: fetch → sinal → ordens → persistir → métricas

**Loop (pseudocódigo):**

```
a cada N segundos:
  para cada par:
    candles = get_candles(par, timeframe)
    sinal = strategy(candles, params)  # BUY / SELL / HOLD
    ordens = order_manager.decidir(sinal, risco, posição_atual)
    execuções = exchange_adapter.executar(ordens, paper_mode=True)
    salvar(candles novos, ordens, execuções, posição, equity)
```

**Schema mínimo (tabelas):**

- `candles(symbol, timeframe, ts, open, high, low, close, volume, PRIMARY KEY(symbol,timeframe,ts))`
- `orders(id, symbol, side, type, qty, price, status, created_at, run_id)`
- `trades(id, order_id, symbol, qty, price, fee, ts)`
- `positions(symbol, qty, avg_price, unrealized_pnl, updated_at)`
- `equity_curve(ts, equity)`
- `strategy_runs(id, started_at, params_json, commit_hash)`
- `configs(id, key, value_json, updated_at)`

**Backtest rápido (fase 2 do MVP):**

- Reusar a mesma `strategy()` em um motor de backtest simples (candles históricos + simulação de ordens com fee/slippage).
- Exportar relatório comparando parâmetros do canal (grid de hiperparâmetros).

---

# 2) Como a IA pode ajudar (sem “encher” o prompt)

A chave é trabalhar por **tickets pequenos**, com **entradas/saídas claras** e **critérios de aceite**. Sempre passe **só o contexto necessário** daquele ticket, referenciando o restante por **ID/numeração** (ex.: “Requisito R1…R7”). Mantenha um **documento vivo** (pode ser um README/Spec.md) numerado; quando pedir algo à IA, inclua apenas os itens relevantes.

### Formato de “ticket” (copiar/colar)

Use esta estrutura sempre (reduz ruído e duplicação):

**Título:** [Módulo] Tarefa curta e específica  
**Objetivo:** o que deve existir ao final  
**Contexto mínimo:** 3–5 bullets (referencie “R1…R5” do seu Spec se precisar)  
**Entradas:** dados, tipos, origem  
**Saídas:** artefatos, tipos, destino  
**Restrições:** libs, estilo, performance, erros a tratar  
**Critérios de aceite (testáveis):** lista clara  
**Entregáveis:** arquivos/assinaturas de função/migrações esperadas  
**Formato da resposta:** (ex.: “código + testes + instruções de execução”)

Exemplo de **critérios de aceite** bons:

- “`get_klines(symbol, timeframe, since)` retorna `List[Candle]` sem buracos de tempo; reconecta na falha; limita 1200 req/min.”
- “Migração Alembic cria PK composta em `candles` (symbol,timeframe,ts).”
- “Teste unitário cobre fee e slippage.”

---

# 3) Modelos de prompt prontos

### 3.1. Arquitetura inicial

> **Papel:** Você é um arquiteto de software Python.  
> **Objetivo:** Propor a arquitetura mínima para um bot de cripto em paper trading na Binance.  
> **Contexto:** (liste 5 bullets: estratégia do canal, pares, timeframe, DB, paper mode)  
> **Restrições:** Python 3.11, ccxt, SQLAlchemy, Alembic, pandas; logs com loguru.  
> **Entregáveis:** árvore de pastas, dependências (requirements.txt), diagrama textual dos módulos, fluxo do loop.  
> **Critérios de aceite:** componentes separados; estratégia plugável; persistência de candles/ordens/trades; instruções de setup.  
> **Formato da resposta:** Markdown conciso com árvore do projeto e passos de instalação/execução.

### 3.2. Adapter Binance (ticket)

> **Título:** [exchange_adapter] Funções básicas (klines, saldo, ordem paper)  
> **Objetivo:** Implementar `get_klines`, `get_balance_paper`, `place_order_paper` usando ccxt ou simulador próprio.  
> **Entradas:** `symbol: str`, `timeframe: str`, `limit: int`, `since: int|None` (ms epoch).  
> **Saídas:** lista de `Candle` (pydantic), `Order`, `Trade`.  
> **Restrições:** lidar com rate limit/reenfileiramento; normalizar exceções; timezone UTC.  
> **Critérios de aceite:** testes unitários com dados mockados; recuperação automática em falha; docstrings.  
> **Formato da resposta:** código + testes + instruções de execução.

### 3.3. Estratégia do canal (ticket)

> **Título:** [strategy] Canal de preço: compra na banda inferior, vende na superior  
> **Objetivo:** Função pura `signal(candles, params)->{"BUY"|"SELL"|"HOLD"}`  
> **Contexto:** params = {timeframe, lookback, método do canal (Donchian/ATR/bandas fixas), alvo, stop}.  
> **Critérios de aceite:** teste com séries sintéticas que disparem BUY/SELL; sem dependência de I/O.

### 3.4. Order Manager + risco (ticket)

> **Título:** [order_manager] Sizing + simulação paper com fee/slippage  
> **Objetivo:** Dado `signal` e `position`, gerar ordens e atualizar posição.  
> **Critérios:** fee configurável, slippage em bps, tamanho máximo por trade, no overbuy/oversell.

### 3.5. Persistência e migrações (ticket)

> **Título:** [persistence] Schema + Alembic inicial  
> **Objetivo:** Tabelas listadas acima e PKs corretas; índices por `symbol,timeframe,ts`.  
> **Critérios:** migração reversível; teste de inserção/consulta.

### 3.6. Relatórios iniciais (ticket)

> **Título:** [reporting] Métricas básicas + curva de capital  
> **Objetivo:** Função que calcula PnL, win rate, max drawdown, Sharpe simples; exporta CSV/PNG.  
> **Critérios:** aceita um `run_id`; roda sem internet; testes com dataset pequeno.

---

## Dicas práticas para seus prompts

- **Curto e numerado:** “R1…R7”. Evite narrativa longa.
- **Peça “output format” específico:** “retorne apenas código + explicações de 5 linhas”.
- **Exija testes e exemplos de uso** (economiza idas e voltas).
- **Peça o modelo para listar ambiguidades** no final (e decidir defaults razoáveis).
- **Itere em ciclos curtos:** Planejo → Código → Testes → Revisão (“faça code review e proponha melhorias de robustez/performance”).
- **Cole trechos de log/erro** quando necessário (sempre o menor recorte que reproduz).
- **Mantenha um Spec.md versionado** com requisitos numerados. Quando mudar algo, atualize R# e mencione nos prompts (“R3 atualizado para delta=2*ATR”).

---

## Considerações de risco (essenciais)

- Use **paper trading/testnet** até acumular evidência (métricas).
- Simule **taxas e slippage** sempre; sem isso o PnL vira fantasia.
- Limite **exposição por par** e **perda diária** no `risk/`.
- Salve **commit_hash** (ou versão do código) em cada `strategy_run` pra reprodutibilidade.

---

## Quer que eu já entregue o esqueleto?

Posso gerar agora:

- `pyproject.toml` + `requirements.txt`
- árvore de pastas
- migração Alembic inicial
- modelos pydantic/SQLAlchemy
- um loop mínimo em paper mode que lê 1 par e grava candles/ordens/trades

Se topar, me diga:

1. quais pares e timeframe (ex.: BTC/USDT, ETH/USDT, 1m/5m/15m),
2. banco (SQLite local ou Postgres),
3. se quer **ccxt** ou simulador puro para o paper (eu recomendo ccxt).

A partir daí seguimos por tickets usando os modelos de prompt acima.