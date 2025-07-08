# ✅ Primeiros Passos no Desenvolvimento – FastAPI + WebSocket Binance

---

## 🛠️ 1. Estruturação do Ambiente

#### **🐍 Python & Bibliotecas Principais**

|Pacote|Versão|Finalidade|
|---|---|---|
|`Python`|3.10+|Versão estável com suporte a async/await|
|`FastAPI`|0.95+|Framework para APIs (rápido e assíncrono)|
|`uvicorn`|0.22+|ASGI server para rodar o FastAPI|
|`python-binance`|1.0+|Integração com API Binance (REST/WebSocket)|
|`asyncpg`|0.27+|Driver assíncrono para PostgreSQL|
|`SQLAlchemy`|2.0+|ORM (opcional, para modelos de dados)|
|`pydantic`|2.0+|Validação de dados (obrigatório no FastAPI)|
|`apscheduler`|3.9+|Agendamento de tarefas (vendas programadas)|
|`python-dotenv`|1.0+|Gerenciamento de variáveis de ambiente|
|`httpx`|0.24+|Cliente HTTP assíncrono (para APIs externas)|
|`pytest`|7.3+|Testes unitários/integração|
|`pytest-asyncio`|0.21+|Suporte a testes assíncronos|

#### **🗃️ Banco de Dados**

|Componente|Versão|Detalhes|
|---|---|---|
|`PostgreSQL`|15+|Banco principal (suporte a JSONB e consultas complexas)|
|`pgAdmin`|7.0+|Interface gráfica (opcional)|
|`Alembic`|1.11+|Migrações de banco (se usar SQLAlchemy)|

#### **🛠️ Ferramentas Adicionais**

|Ferramenta|Finalidade|
|---|---|
|`Docker`|Containerização (PostgreSQL + App)|
|`Docker Compose`|Orquestração de containers|
|`Poetry`|Gerenciamento de dependências (ou `pipenv`)|
|`Git`|Controle de versão|
|`Redis`|Cache (opcional para tarefas assíncronas)|

#### **📋 Arquivo `requirements.txt`**


```text
fastapi==0.95.2
uvicorn==0.22.0
python-binance==1.0.19
asyncpg==0.27.0
sqlalchemy==2.0.15
pydantic==2.1.1
apscheduler==3.9.1
python-dotenv==1.0.0
httpx==0.24.1
pytest==7.3.1
pytest-asyncio==0.21.0
alembic==1.11.1
```

---

## 🧱 2. Estrutura Inicial do Projeto

```bash
├── /app
│   ├── /core
│   │   ├── config.py              # Configurações do canal (limites, % alvo)
│   │   ├── security.py            # Autenticação (opcional para MVP)
│   │   └── database.py            # Modelos PostgreSQL (Position, Strategy)
│   │
│   ├── /binance
│   │   ├── client.py              # Cliente Binance (WebSocket + REST)
│   │   ├── price_monitor.py       # Monitoramento em tempo real (H4)
│   │   └── trade_executor.py      # Execução de ordens (compra/venda)
│   │
│   ├── /strategies                # Lógica da estratégia de canal
│   │   ├── channel_strategy.py    # Regras de entrada/saída (ex: +2% base)
│   │   ├── capital_control.py     # Gestão do capital (20% da banca)
│   │   └── profit_handler.py      # Segregação de lucros (não reinveste)
│   │
│   ├── /models                    # Modelos de dados
│   │   ├── position.py            # Posições (status, preço, taxas)
│   │   └── strategy.py            # Config da estratégia (teto, base, %)
│   │
│   ├── main.py                    # Rotas FastAPI (ex: /strategies/{id}/status)
│   └── schemas.py                 # Validação com Pydantic (ex: OrderSchema)
│
├── /tests
│   ├── test_channel_strategy.py   # Testes das regras de canal
│   └── test_binance_integration.py
│
├── /scripts
│   └── init_db.py                 # Carga inicial de estratégias (ex: Canal H4)
│
└── requirements.txt
```

---

## 📊 3. Endpoints a Desenvolver (FastAPI)

#### **📌 Módulo: Configuração da Estratégia**

|Endpoint|Método|Descrição|Parâmetros (Request Body)|
|---|---|---|---|
|`/strategies/`|`POST`|Cria uma nova estratégia de canal|`{ "symbol": "BTCUSDT", "base_price": 100.489, "top_price": 110.626, "capital_percentage": 20, ... }`|
|`/strategies/{id}`|`GET`|Retorna detalhes de uma estratégia|-|
|`/strategies/{id}/activate`|`PATCH`|Ativa/desativa uma estratégia|`{ "is_active": true }`|
|`/strategies/client/{client_id}`|`GET`|Lista todas as estratégias de um cliente|-|

#### **📈 Módulo: Monitoramento de Preços**

|Endpoint|Método|Descrição|Parâmetros|
|---|---|---|---|
|`/prices/{symbol}/history`|`GET`|Retorna histórico de preços (H4)|`?limit=100`|
|`/prices/{symbol}/current`|`GET`|Preço atual do símbolo|-|
|`/prices/ws`|`WebSocket`|Stream em tempo real (WebSocket)|-|

#### **💰 Módulo: Gestão de Ordens**

|Endpoint|Método|Descrição|Parâmetros (Request Body)|
|---|---|---|---|
|`/orders/buy`|`POST`|Executa ordem de compra|`{ "strategy_id": 1, "quantity": 0.5 }`|
|`/orders/sell`|`POST`|Executa ordem de venda|`{ "position_id": 123, "is_scheduled": false }`|
|`/orders/scheduled`|`GET`|Lista vendas programadas|-|
|`/orders/{id}/cancel`|`DELETE`|Cancela uma ordem programada|-|

#### **🗂️ Módulo: Posições e Capital**

|Endpoint|Método|Descrição|Parâmetros|
|---|---|---|---|
|`/positions/`|`GET`|Lista todas as posições|`?status=open`|
|`/positions/{id}`|`GET`|Detalhes de uma posição|-|
|`/positions/{id}/schedule-sell`|`POST`|Agenda venda com lucro mínimo|`{ "min_profit": 0.5 }`|
|`/capital/balance`|`GET`|Saldo total (capital + lucros)|`?client_id=1`|

#### **📊 Módulo: Relatórios**

|Endpoint|Método|Descrição|Parâmetros|
|---|---|---|---|
|`/reports/profit`|`GET`|Lucro acumulado por estratégia|`?strategy_id=1`|
|`/reports/positions`|`GET`|Resumo de posições (abertas/fechadas)|`?days=30`|
|`/reports/trades`|`GET`|Histórico completo de trades|`?symbol=BTCUSDT`|

#### **🔐 Módulo: Autenticação (Opcional para MVP)**

|Endpoint|Método|Descrição|Parâmetros|
|---|---|---|---|
|`/auth/login`|`POST`|Gera token JWT|`{ "api_key": "xxx", "api_secret": "yyy" }`|
|`/auth/refresh`|`POST`|Renova token|`{ "refresh_token": "zzz" }`|

#### **🔧 Configuração Mínima do Ambiente**

1. **Instalação do PostgreSQL**:
```bash    
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql -c "CREATE DATABASE criptoren;"
```

2. **Setup do Python** (usando **Poetry**):
```bash
poetry init
poetry add fastapi uvicorn python-binance
```

3. **Variáveis de Ambiente (`.env`)**:
```env
    DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/criptoren
    BINANCE_API_KEY=xxx
    BINANCE_API_SECRET=yyy
```

---

## 🧩 6. Scripts SQL Iniciais

```sql
-- Criação do banco
CREATE DATABASE criptoren;
\c criptoren;

-- Extensão para UUID (opcional)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Tabela clients
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    api_key VARCHAR(100) UNIQUE,
    api_secret VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela symbols
CREATE TABLE symbols (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20) UNIQUE NOT NULL,
    base_asset VARCHAR(20) NOT NULL,
    quote_asset VARCHAR(20) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela strategies (núcleo da estratégia)
CREATE TABLE strategies (
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    base_price DECIMAL(18, 8) NOT NULL,
    top_price DECIMAL(18, 8) NOT NULL,
    capital_percentage DECIMAL(5, 2) NOT NULL CHECK (capital_percentage > 0 AND capital_percentage <= 100),
    buy_threshold DECIMAL(5, 2) NOT NULL,
    sell_threshold DECIMAL(5, 2) NOT NULL,
    min_profit DECIMAL(5, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela positions (gestão de posições)
CREATE TABLE positions (
    id SERIAL PRIMARY KEY,
    strategy_id INTEGER NOT NULL REFERENCES strategies(id) ON DELETE CASCADE,
    symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    entry_price DECIMAL(18, 8) NOT NULL,
    quantity DECIMAL(18, 8) NOT NULL,
    fees DECIMAL(18, 8) DEFAULT 0,
    status VARCHAR(20) NOT NULL CHECK (status IN ('open', 'scheduled', 'closed')),
    exit_price DECIMAL(18, 8),
    scheduled_exit_price DECIMAL(18, 8),
    channel_exit_date TIMESTAMP,
    closed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela trades (histórico de execuções)
CREATE TABLE trades (
    id SERIAL PRIMARY KEY,
    position_id INTEGER REFERENCES positions(id) ON DELETE SET NULL,
    client_id INTEGER NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    symbol_id INTEGER NOT NULL REFERENCES symbols(id) ON DELETE CASCADE,
    type VARCHAR(10) NOT NULL CHECK (type IN ('buy', 'sell')),
    price DECIMAL(18, 8) NOT NULL,
    quantity DECIMAL(18, 8) NOT NULL,
    fees DECIMAL(18, 8) DEFAULT 0,
    profit DECIMAL(18, 8),
    notes TEXT,
    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela capital_allocations (controle financeiro)
CREATE TABLE capital_allocations (
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    strategy_id INTEGER NOT NULL REFERENCES strategies(id) ON DELETE CASCADE,
    amount DECIMAL(18, 8) NOT NULL,
    is_profit BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para otimização
CREATE INDEX idx_positions_strategy ON positions(strategy_id);
CREATE INDEX idx_positions_status ON positions(status);
CREATE INDEX idx_trades_symbol_executed ON trades(symbol_id, executed_at);
CREATE INDEX idx_capital_client ON capital_allocations(client_id);

-- Gatilho para atualizar updated_at
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar gatilhos
CREATE TRIGGER update_strategies_timestamp
BEFORE UPDATE ON strategies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_positions_timestamp
BEFORE UPDATE ON positions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

---

### 🌱Dados Iniciais de Exemplo

```sql
-- Inserir um cliente
INSERT INTO clients (name, api_key, api_secret)
VALUES ('TradeBot XYZ', 'binance_key_123', 'binance_secret_456');

-- Inserir símbolos
INSERT INTO symbols (symbol, base_asset, quote_asset)
VALUES 
    ('BTCUSDT', 'BTC', 'USDT'),
    ('ETHUSDT', 'ETH', 'USDT');

-- Inserir estratégia (Canal H4)
INSERT INTO strategies (
    client_id, symbol_id, name, 
    base_price, top_price, capital_percentage,
    buy_threshold, sell_threshold, min_profit
) VALUES (
    1, 1, 'Canal H4 BTC/USDT',
    100.489, 110.626, 20.00,
    2.00, 2.00, 0.50
);

-- Alocar capital
INSERT INTO capital_allocations (client_id, strategy_id, amount)
VALUES (1, 1, 2000.00);
```

---

### 🔍 **Consultas Úteis**

1. **Posições Abertas**:
```sql
    SELECT p.*, s.symbol 
    FROM positions p
    JOIN symbols s ON p.symbol_id = s.id
    WHERE p.status = 'open';
```

2. **Vendas Programadas**:    
```sql
    SELECT p.*, s.symbol 
    FROM positions p
    JOIN symbols s ON p.symbol_id = s.id
    WHERE p.status = 'scheduled';
```    

2. **Saldo de Capital**:    
```sql
    SELECT 
        SUM(CASE WHEN is_profit = FALSE THEN amount ELSE 0 END) AS capital_principal,
        SUM(CASE WHEN is_profit = TRUE THEN amount ELSE 0 END) AS lucros_acumulados
    FROM capital_allocations
    WHERE client_id = 1;
```

---

## ▶️ 7. Inicialização do Projeto

Execute o servidor:

```bash
uvicorn main:app --reload
```

---

## 📆 8. Planejamento das Próximas Fases

### **📌 Sprint 0: Preparação (1-2 dias)**

**Objetivo**: Configuração inicial do ambiente e definições técnicas.
- Setup do ambiente (Python, PostgreSQL, Docker)
- Definir arquitetura do projeto (estrutura de pastas)
- Criar documento de visão do produto (Product Vision Board)

**Entregáveis**:
- Ambiente de desenvolvimento funcional
- Repositório Git inicializado

### **📌 Épico 1: Integração com Binance**

**Objetivo**: Conectar-se à API Binance para obter dados de mercado e executar ordens.

#### **Sprint 1: Leitura de Dados (1 semana)**

**User Stories**:
- Como usuário, quero consultar preços em tempo real via WebSocket (BTCUSDT)
- Como sistema, preciso armazenar candles H4 no banco de dados
- Como desenvolvedor, quero tratar erros de conexão com a Binance

**Entregáveis**:
- Módulo `binance/price_monitor.py` funcional
- Tabela `historical_prices` no PostgreSQL

#### **Sprint 2: Execução de Ordens (1 semana)**

**User Stories**:
- Como usuário, quero executar ordens de compra/venda via API Binance
- Como sistema, preciso validar saldo antes de operar
- Como desenvolvedor, quero registrar todas as ordens no banco (`trades`)

**Entregáveis**:
- Endpoints `POST /orders/buy` e `POST /orders/sell`
- Integração com tabela `capital_allocations`

### **📌 Épico 2: Estratégia de Canal**

**Objetivo**: Implementar a lógica de compra/venda baseada em canal de preço.

#### **Sprint 3: Lógica de Entrada (1 semana)**

**User Stories**:
- Como sistema, quero comprar automaticamente quando o preço subir +2% da base
- Como usuário, quero definir parâmetros do canal (base, teto, %) via API
- Como sistema, preciso calcular o capital alocado (20% da banca)

**Entregáveis**:
- Tabela `strategies` populável via `POST /strategies`
- Serviço `channel_strategy.py` com regras de entrada

#### **Sprint 4: Lógica de Saída (1 semana)**

**User Stories**:
- Como sistema, quero agendar vendas quando o preço cair -2% do teto
- Como usuário, quero listar vendas programadas (`GET /orders/scheduled`)
- Como sistema, nunca devo vender abaixo do preço mínimo (compra + taxas + 0.5%)

**Entregáveis**:
- Endpoint `POST /positions/{id}/schedule-sell`
- Módulo `profit_handler.py` para cálculos de lucro mínimo

### **📌 Épico 3: Gestão de Capital**

**Objetivo**: Garantir controle rígido do capital e lucros.

#### **Sprint 5: Alocação de Capital (3 dias)**

**User Stories**:
- Como sistema, preciso reservar 20% da banca para cada operação
- Como usuário, quero ver meu saldo disponível (`GET /capital/balance`)
- Como sistema, devo segregar lucros (não reinvestir automaticamente)

**Entregáveis**:
- Serviço `capital_control.py`
- Endpoint `GET /capital/balance`

### **📌 Épico 4: Relatórios e Dashboard**

**Objetivo**: Fornecer visibilidade das operações.

#### **Sprint 6: Relatórios Básicos (4 dias)**

**User Stories**:
- Como usuário, quero ver meu lucro acumulado por estratégia
- Como sistema, preciso gerar histórico de trades (`GET /reports/trades`)

**Entregáveis**:
- Endpoints `GET /reports/profit` e `GET /reports/positions`

### **📌 Sprint 7: Validação & Ajustes (3 dias)**

**Objetivo**: Testes e refinamentos.
- Testes de integração com a Binance (simulação de ordens)
- Ajustes na tolerância a falhas (retry mechanism)
- Documentação básica da API (Swagger/OpenAPI)

### **📌 Sprint 8: Preparação para Produção (2 dias)**

**Objetivo**: Deploy inicial.
- Configurar Docker Compose (PostgreSQL + App)
- Variáveis de ambiente para produção
- Script de backup automático do banco

### **🎯 Critérios de Aceitação por Épico**

1. **Binance**:
    - 99% de uptime na conexão WebSocket
    - Ordens executadas em < 500ms

2. **Estratégia**:
    - Compra/Venda respeitando canal em 100% dos casos
    - Zero vendas com prejuízo

3. **Capital**:
    - Alocação precisa (20% ± 0.1%)
    - Lucros corretamente segregados

---


<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>

