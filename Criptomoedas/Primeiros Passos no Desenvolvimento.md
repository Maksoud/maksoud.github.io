# ✅ Primeiros Passos no Desenvolvimento – Sistema de Monitoramento de Criptomoedas


## 🛠️ 1. Estruturação do Ambiente de Desenvolvimento

- Instalar o Python (versão 3.8 ou superior recomendada)
- Criar um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

- Instalar as bibliotecas iniciais:

```bash
pip install python-binance mysql-connector-python flask sqlalchemy
```

_(Pode ajustar para FastAPI ou outro framework depois, se quiser)_

---

## 🧱 2. Estrutura Inicial do Projeto (Pasta / Arquivos)

```bash
project-root/
├── app/
│   ├── api/                # Endpoints Flask ou FastAPI
│   ├── binance_client.py   # Conexão com API da Binance
│   ├── models.py           # Modelos de banco de dados (SQLAlchemy)
│   ├── services/           # Lógicas de negócios (estratégias, cálculo de lucro, etc.)
│   └── utils.py            # Funções auxiliares
├── config.py               # Configurações gerais (chaves da Binance, dados do banco)
├── requirements.txt
└── run.py                  # Arquivo inicial da aplicação
```

---

## 🔑 3. Configuração das Credenciais da Binance

No arquivo `config.py`, defina:

```python
API_KEY = 'SUA_API_KEY'
API_SECRET = 'SEU_API_SECRET'
```

_(Recomendo usar variáveis de ambiente no futuro para segurança)_

---

## 🌐 4. Conexão Inicial com a Binance API

Criar o arquivo `binance_client.py`:

```python
from binance.client import Client
from config import API_KEY, API_SECRET

client = Client(API_KEY, API_SECRET)
```

Testar com uma simples chamada:

```python
print(client.get_symbol_ticker(symbol="BTCUSDT"))
```

---

## 🕒 5. Escolha Inicial: REST ou Websocket?

👉 **Para o MVP, comece com as consultas REST da Binance:**  
Exemplo: Preço de cotação atual, book, etc.

👉 **Depois evoluir para WebSocket**, apenas quando quiser monitoramento em tempo real.

### ✅ Passo a Passo Inicial – Usando WebSocket da Binance

#### 1. Instalação das Bibliotecas Necessárias:

`pip install python-binance websockets mysql-connector-python sqlalchemy flask`

#### 2. Conexão com WebSocket – Exemplo básico (Binance `depth`, `trade`, ou `kline`)

#### Exemplo para ouvir o ticker em tempo real (preço do último trade):

```python
from binance.streams import ThreadedWebsocketManager
from config import API_KEY, API_SECRET

def handle_socket_message(msg):
    print(f"Mensagem recebida: {msg}")

twm = ThreadedWebsocketManager(API_KEY, API_SECRET)
twm.start()

twm.start_symbol_ticker_socket(callback=handle_socket_message, symbol='btcusdt')
```

_(Você pode começar ouvindo só um par, e depois abrir múltiplas conexões para vários pares.)_

---

## 🧱 6. Definição e Criação das Primeiras Tabelas no Banco de Dados

### Tabelas para o início:

- **strategies**
- **trades (operacoes)**
- **symbols (pares de moedas)**
- **price_history (para logar cotações se quiser fazer backtesting depois)**

### Estrutura das Tabelas SQL – Criação Inicial

Aqui estão os **scripts SQL iniciais**, já considerando o uso de **estratégias**, **operações (trades)**, **pares de moedas (símbolos)** e **histórico de cotações (opcional para backtesting ou análise futura)**.

#### 📌 Tabela: `symbols` (pares de moedas)

```sql
CREATE TABLE symbols (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL UNIQUE,
    base_asset VARCHAR(20),
    quote_asset VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 📌 Tabela: `strategies`

```sql
CREATE TABLE strategies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    capital_percentage DECIMAL(5,2) DEFAULT 0.00,
    consider_profits BOOLEAN DEFAULT FALSE,
    lower_limit DECIMAL(18,8),
    upper_limit DECIMAL(18,8),
    min_profit_percentage DECIMAL(8,4),
    min_gain_to_buy_percentage DECIMAL(8,4),
    max_fall_to_sell_percentage DECIMAL(8,4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 📌 Tabela: `trades` (operações)

```sql
CREATE TABLE trades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    strategy_id INT NOT NULL,
    symbol_id INT NOT NULL,
    type ENUM('buy', 'sell', 'simulation') NOT NULL,
    quantity DECIMAL(18,8) NOT NULL,
    price DECIMAL(18,8) NOT NULL,
    fee DECIMAL(18,8) DEFAULT 0.00000000,
    trade_datetime DATETIME NOT NULL,
    status ENUM('open', 'planned_sell', 'closed') DEFAULT 'open',
    sell_target_price DECIMAL(18,8),
    exit_reason VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (strategy_id) REFERENCES strategies(id),
    FOREIGN KEY (symbol_id) REFERENCES symbols(id)
);
```

#### 📌 Tabela: `price_history` (opcional para backtesting ou estatísticas)

```sql
CREATE TABLE price_history (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    symbol_id INT NOT NULL,
    price DECIMAL(18,8) NOT NULL,
    event_time DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (symbol_id) REFERENCES symbols(id)
);
```


#### 📌 Tabela: `api_failures` (controle de falhas de API ou WebSocket)

```sql
CREATE TABLE api_failures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service VARCHAR(50) NOT NULL,
    error_message TEXT,
    event_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved BOOLEAN DEFAULT FALSE
);
```

---

## 🔁 7. Rotina de Coleta de Preço Atual

- Criar uma função tipo:
    

```python
def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])
```

---

## ✅ 8. Função de Registro Manual de Operação (Simulação ou Real)

Criar um endpoint Flask/FastAPI como:

```python
@app.route('/register_trade', methods=['POST'])
def register_trade():
    data = request.json
    # Salvar no banco: tipo, par, preço, quantidade, taxa, data/hora, status, etc.
```

---

## 📈 9. Primeira Página Web: Listagem das Operações Cadastradas

- Fazer uma rota simples com Flask para listar as operações.
- Exemplo: `/trades`

_(Pode usar Jinja2 templates ou começar com um JSON puro se quiser trabalhar a UI depois com React/Vue)_

---

## 🚩 10. Planejamento das Próximas Fases:

|Fase|Tarefas|
|---|---|
|✅ Fase 1|Coleta de preços e registro manual de operações|
|Próxima|Cadastro de estratégias|
|Próxima|Programação de vendas futuras|
|Próxima|Monitoramento automático de cotações|
|Próxima|Implementação de WebSocket para cotação em tempo real|
|Próxima|Dashboards e relatórios|


<sup><sub>
Renée Maksoud - junho de 2025
</sub></sup>