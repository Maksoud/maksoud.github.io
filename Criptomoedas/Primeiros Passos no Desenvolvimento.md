# ✅ Primeiros Passos no Desenvolvimento – FastAPI + WebSocket Binance

---

## 🛠️ 1. Estruturação do Ambiente

- Instale o [Python](https://www.python.org/downloads/) (versão 3.8+)
- Crie o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

- Instale os pacotes:

```bash
pip install fastapi uvicorn python-binance sqlalchemy psycopg2-binary websockets
```

---

## 🧱 2. Estrutura Inicial do Projeto

```bash
project-root/
├── app/
│   ├── api/                # Endpoints FastAPI
│   ├── models/             # Modelos SQLAlchemy
│   ├── services/           # Lógica de negócios
│   ├── binance_ws.py       # WebSocket Binance
│   ├── database.py         # Conexão com PostgreSQL
│   └── schemas.py          # Pydantic models (validação)
├── config.py               # Configurações do projeto
├── main.py                 # Inicializador da FastAPI
└── requirements.txt
```

---

## 🔑 3. Configuração da API Binance

**`config.py`:**

```python
import os

API_KEY = os.getenv("BINANCE_API_KEY", "")
API_SECRET = os.getenv("BINANCE_API_SECRET", "")
```

---

## 🌐 4. Conexão com WebSocket da Binance

**`binance_ws.py`:**

```python
from binance.streams import ThreadedWebsocketManager
from config import API_KEY, API_SECRET

def handle_price_message(msg):
    symbol = msg['s']
    price = msg['c']
    print(f"{symbol} → {price}")

def start_ticker(symbol: str):
    twm = ThreadedWebsocketManager(api_key=API_KEY, api_secret=API_SECRET)
    twm.start()
    twm.start_symbol_ticker_socket(callback=handle_price_message, symbol=symbol.lower())
```

---

## 📊 5. Endpoints a Desenvolver (FastAPI)

### 1. Monitoramento de Par de Moeda (GET)

```http
GET /monitorar-par/{symbol}
```

- Inicia WebSocket para monitoramento de um par (ex: BTCUSDT)

---

### 2. Posicionar Compra (POST)

```http
POST /posicionar-compra
```

**Body JSON:**

```json
{
  "cliente_id": 1,
  "symbol": "BTCUSDT",
  "preco_alvo": 62000.00,
  "quantidade": 0.005
}
```

- Armazena a intenção de compra em tabela intermediária
- Não executa a compra ainda

---

### 3. Registrar Compra Executada (POST)

```http
POST /registrar-compra
```

**Body JSON:**

```json
{
  "cliente_id": 1,
  "symbol": "BTCUSDT",
  "preco_executado": 62000.00,
  "quantidade": 0.005
}
```

- Executado pelo sistema quando o WebSocket identifica o preço alvo atingido

---

### 4. Registrar Venda Executada (POST)

```http
POST /registrar-venda
```

**Body JSON:**

```json
{
  "cliente_id": 1,
  "symbol": "BTCUSDT",
  "preco_executado": 63500.00,
  "quantidade": 0.005
}
```

---

## 🧩 6. Scripts SQL Iniciais

Use PostgreSQL com o seguinte comando:

```sql
CREATE DATABASE criptoren;
```

### Tabela `clients`

```sql
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    api_token VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabela `symbols`

```sql
CREATE TABLE symbols (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20) UNIQUE NOT NULL,
    base_asset VARCHAR(20),
    quote_asset VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabela `positioned_orders`

```sql
CREATE TABLE positioned_orders (
    id SERIAL PRIMARY KEY,
    client_id INT NOT NULL REFERENCES clients(id),
    symbol_id INT NOT NULL REFERENCES symbols(id),
    target_price DECIMAL(18,8) NOT NULL,
    quantity DECIMAL(18,8) NOT NULL,
    type VARCHAR(10) CHECK (type IN ('buy', 'sell')) NOT NULL,
    status VARCHAR(20) DEFAULT 'waiting',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabela `trades`

```sql
CREATE TABLE trades (
    id SERIAL PRIMARY KEY,
    client_id INT NOT NULL REFERENCES clients(id),
    symbol_id INT NOT NULL REFERENCES symbols(id),
    type VARCHAR(10) CHECK (type IN ('buy', 'sell')) NOT NULL,
    price DECIMAL(18,8) NOT NULL,
    quantity DECIMAL(18,8) NOT NULL,
    fee DECIMAL(18,8) DEFAULT 0.00000000,
    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ▶️ 7. Inicialização do Projeto

**`main.py`:**

```python
from fastapi import FastAPI
from app.api import routes  # criar um __init__.py para importar rotas

app = FastAPI()
app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"status": "OK"}
```

Execute o servidor:

```bash
uvicorn main:app --reload
```

---

## 📆 8. Planejamento das Próximas Fases

|Fase|Tarefas|
|---|---|
|MVP|Endpoints básicos de monitoramento, compra, venda|
|Fase 2|Monitoramento ativo por cliente|
|Fase 3|Interface web com painel|
|Fase 4|Estratégias automatizadas (ex: canais)|
|Fase 5|Alertas e auditoria de operações|

---

Se quiser, posso montar os **modelos Pydantic (`schemas.py`)** e o esqueleto de cada rota com base nas estruturas acima. Deseja seguir com isso agora?