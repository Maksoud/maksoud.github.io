# Primeiros Passos no Desenvolvimento
Atualizado em 13/08/2025

### **📋 Arquivo `requirements.txt`**


```text
binance-connector==3.6.0
websockets==12.0
pydantic==2.8.2
pydantic-settings==2.3.4
sqlalchemy==2.0.32
alembic==1.13.2
psycopg[binary]==3.2.1
pandas==2.2.2
typer==0.12.3
structlog==24.1.0
python-dotenv==1.0.1
tenacity==9.0.0
APScheduler==3.10.4
cryptography==43.0.0
uvloop==0.20.0 ; platform_system != "Windows"
pytest==8.3.2
```

---

### Estrutura Inicial do Projeto

```shell
binance-bot/
├─ README.md
├─ pyproject.toml
├─ requirements.txt
├─ .env.example
├─ .gitignore
├─ src/
│  ├─ bot/
│  │  ├─ __init__.py
│  │  ├─ config.py                 # Pydantic settings (env/.env)
│  │  ├─ logging.py                # structlog + JSON logging
│  │  ├─ db/
│  │  │  ├─ __init__.py
│  │  │  ├─ base.py                # engine + session factory
│  │  │  ├─ models.py              # ORM models
│  │  │  └─ repositories.py        # consultas/escritas
│  │  ├─ security/
│  │  │  ├─ __init__.py
│  │  │  └─ secrets.py             # criptografia de chaves API (Fernet)
│  │  ├─ binance/
│  │  │  ├─ __init__.py
│  │  │  ├─ client.py              # criação de clientes (Spot/Futures) por conta
│  │  │  ├─ market_data.py         # candles/ordem/livro via REST/WebSocket
│  │  │  └─ execution.py           # execução de ordens (live/paper)
│  │  ├─ strategies/
│  │  │  ├─ __init__.py
│  │  │  ├─ base.py                # ABC Strategy + config pydantic
│  │  │  ├─ registry.py            # registro/descoberta de estratégias
│  │  │  ├─ mean_reversion.py      # exemplo 1
│  │  │  └─ breakout.py            # exemplo 2
│  │  ├─ runtime/
│  │  │  ├─ scheduler.py           # agenda de jobs (APScheduler/asyncio)
│  │  │  ├─ orchestrator.py        # orquestra múltiplas estratégias/contas
│  │  │  └─ paper_trade.py         # simulador de fills/fees para demo
│  │  ├─ reporting/
│  │  │  ├─ __init__.py
│  │  │  └─ metrics.py             # KPIs base (P&L bruto, fees, hit-rate)
│  │  └─ cli.py                    # Typer CLI
│  └─ alembic/
│     ├─ env.py
│     ├─ script.py.mako
│     └─ versions/
│        └─ 2025_01_init.py        # migração inicial
└─ tests/
   ├─ conftest.py
   ├─ test_strategy_flow.py
   └─ test_paper_trade.py
```

---

### Bibliotecas e aplicação (com exemplos)

### 1) `binance-connector`

- **Uso**: acesso REST/WebSocket; múltiplas credenciais; Spot/Futures.
- **Exemplo (criar cliente por conta)**:

```python
# src/bot/binance/client.py
from binance.spot import Spot
from pydantic import BaseModel

class ApiCreds(BaseModel):
    key: str
    secret: str

def build_spot(creds: ApiCreds, testnet: bool=False) -> Spot:
    base_url = "https://testnet.binance.vision" if testnet else None
    return Spot(api_key=creds.key, api_secret=creds.secret, base_url=base_url)
```
### 2) `websockets` (quando precisar de raw WS ou streams custom)

- **Uso**: consumo de trades/candles em baixa latência (ou via WS do `binance-connector`).
- **Exemplo (esqueleto de listener)**:

```python
# src/bot/binance/market_data.py
import asyncio, json, websockets

async def kline_stream(symbol: str, interval: str):
    url = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@kline_{interval}"
    async with websockets.connect(url) as ws:
        async for msg in ws:
            data = json.loads(msg)
            yield data["k"]
```
### 3) `pydantic` + `pydantic-settings`

- **Uso**: tipagem/validação de configs e estratégias.
- **Exemplo (Settings e StrategyConfig)**:

```python
# src/bot/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str
    ENCRYPTION_KEY: str  # chave Fernet base64
    LOG_LEVEL: str = "INFO"
    class Config: env_file = ".env"

# src/bot/strategies/base.py
from pydantic import BaseModel, Field

class StrategyConfig(BaseModel):
    symbol: str
    candle: str = Field(pattern=r"^\d+[smhd]$")
    min_price: float
    max_price: float
    order_value: float
    min_profit: float
    fee_pct: float
    demo_mode: bool = True
```

### 4) `SQLAlchemy` + `Alembic` + `psycopg`

- **Uso**: persistência (contas, estratégias, execuções, ordens simuladas/reais).
- **Exemplo (engine/modelos)**:


```python
# src/bot/db/base.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from bot.config import Settings

settings = Settings()
engine = create_engine(settings.DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase): pass
```

```python
# src/bot/db/models.py
from sqlalchemy import String, Integer, Float, Boolean, ForeignKey, JSON, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship
from bot.db.base import Base
import enum

class Market(enum.Enum): spot="spot"; futures="futures"

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    api_key_enc: Mapped[str] = mapped_column(String)
    api_secret_enc: Mapped[str] = mapped_column(String)
    testnet: Mapped[bool] = mapped_column(Boolean, default=False)

class Strategy(Base):
    __tablename__ = "strategies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    market: Mapped[Market]
    config: Mapped[dict] = mapped_column(JSON)  # StrategyConfig
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)
```
### 5) `cryptography`

- **Uso**: criptografar API keys no banco.
- **Exemplo**:

```python
# src/bot/security/secrets.py
from cryptography.fernet import Fernet

class SecretBox:
    def __init__(self, key_b64: str):
        self.fernet = Fernet(key_b64)
    def enc(self, s: str) -> str:
        return self.fernet.encrypt(s.encode()).decode()
    def dec(self, s: str) -> str:
        return self.fernet.decrypt(s.encode()).decode()
```
### 6) `structlog`

- **Uso**: logging estruturado (facilita auditoria/reporting).

```python
# src/bot/logging.py
import structlog, logging, sys
def setup_logging(level: str="INFO"):
    logging.basicConfig(stream=sys.stdout, level=level)
    structlog.configure(processors=[structlog.processors.JSONRenderer()])
    return structlog.get_logger()
```
### 7) `APScheduler` (ou `asyncio`)

- **Uso**: agendamento de execução/checagens de estratégias.

```python
# src/bot/runtime/scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler

def build_scheduler():
    sch = AsyncIOScheduler()
    sch.start()
    return sch
```
### 8) `tenacity`

- **Uso**: retries em chamadas de rede/ordens.

```python
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(wait=wait_exponential(min=1, max=30), stop=stop_after_attempt(5))
def place_order(client, **kwargs):
    return client.new_order(**kwargs)
```
### 9) `pandas`

- **Uso**: manipulação de candles e métricas de performance (para relatórios futuros).

### 10) `typer`

- **Uso**: CLI operacional.

```python
# src/bot/cli.py
import typer
from bot.runtime.orchestrator import run_all

app = typer.Typer()

@app.command()
def start():
    """Inicia orquestração de estratégias habilitadas."""
    run_all()

if __name__ == "__main__":
    app()
```
---

### Execução: modo live vs. demonstrativo

- **Live**: `execution.py` envia ordens reais via `Spot.new_order(...)`.
- **Demo**: `paper_trade.py` calcula fills simulados com base no candle/last trade, aplica `fee_pct`, grava em `orders` e `trades` sem chamar a API.

Exemplo de “execution service” com comutação por `demo_mode`:

```python
# src/bot/binance/execution.py
from bot.runtime.paper_trade import paper_order

def execute_order(ctx, side: str, qty: float, price: float|None):
    if ctx.config.demo_mode:
        return paper_order(ctx, side, qty, price)
    return ctx.client.new_order(symbol=ctx.config.symbol, side=side,
                                type="MARKET" if price is None else "LIMIT",
                                quantity=qty, price=price, timeInForce="GTC")
```
---

### Estratégias (interface e exemplo)

```python
# src/bot/strategies/base.py
from abc import ABC, abstractmethod
from bot.strategies.base import StrategyConfig

class Strategy(ABC):
    name: str
    def __init__(self, config: StrategyConfig, services):
        self.config = config
        self.services = services  # market_data, execution, repo, logger

    @abstractmethod
    async def on_tick(self, kline: dict): ...
```
```python
# src/bot/strategies/mean_reversion.py
from .base import Strategy
import statistics as stats

class MeanReversion(Strategy):
    name = "mean_reversion"
    window = 20
    def __init__(self, config, services):
        super().__init__(config, services)
        self.closes = []

    async def on_tick(self, k):
        if not k["x"]:  # candle fechado
            return
        close = float(k["c"]); self.closes.append(close)
        if len(self.closes) < self.window: return
        ma = sum(self.closes[-self.window:]) / self.window
        if close < self.config.min_price or close > self.config.max_price: return
        if close < ma*(1-0.005):
            qty = self.services.calc_qty(self.config.order_value, close)
            await self.services.buy(qty)  # delega a execução (live/paper)
```
> Estratégias podem ser **compartilhadas** via `registry.py`, recebendo apenas `StrategyConfig` parametrizada por cliente/conta.

---

## Modo demonstrativo (paper-trade)

- Simula execução com:
    - Preço de fill: midpoint/último trade do candle.
    - Slippage configurável (opcional).
    - Taxa operacional `fee_pct` aplicada no registro.
    - Persistência de ordens/trades em tabelas próprias.

```python
# src/bot/runtime/paper_trade.py
from datetime import datetime, timezone

def paper_order(ctx, side, qty, price):
    fill_price = price or ctx.services.last_price()
    fee = fill_price * qty * ctx.config.fee_pct
    ctx.repo.save_order(side=side, qty=qty, price=fill_price,
                        fee=fee, demo=True, ts=datetime.now(timezone.utc))
    return {"status":"FILLED","price":fill_price,"qty":qty,"fee":fee}
```
---

### Banco de dados: migração inicial (Alembic)

Estruturas mínimas:

- `accounts(id, name, api_key_enc, api_secret_enc, testnet)`
- `strategies(id, name, account_id, market, config, enabled)`
- `orders(id, strategy_id, side, qty, price, fee, demo, ts)`
- `trades(id, order_id, pnl, ts_close)` (futuro)
- Índices: por `strategy_id`, `ts`, `demo`.

O arquivo `alembic/versions/2025_01_init.py` deve criar essas tabelas e índices.

---

### Instruções de setup (detalhadas)

### 1) Pré‑requisitos

- Python 3.12+
- PostgreSQL 14+ em execução e com um database criado (ex.: `binance_bot`)

### 2) Clonar e instalar

```bash
git clone <seu-fork-ou-repo> binance-bot
cd binance-bot

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```
### 3) Configuração de ambiente

Crie `.env` a partir de `.env.example`:

```ini
DB_URL=postgresql+psycopg://user:password@localhost:5432/binance_bot
ENCRYPTION_KEY=<chave_fernet_base64>  # gerar: python -c "from cryptography.fernet import Fernet;print(Fernet.generate_key().decode())"
LOG_LEVEL=INFO
```
### 4) Inicializar banco e migrações

```bash
alembic upgrade head
```
### 5) Registrar contas (criptografadas)

- Use um script/CLI para salvar `api_key`/`api_secret` com `SecretBox.enc(...)` nas colunas `api_key_enc`/`api_secret_enc`.
- Exemplo CLI (pseudo):

```bash
python -m src.bot.cli add-account --name minha_conta --api-key xxx --api-secret yyy --testnet true
```
### 6) Criar/ativar estratégias

- Inserir registro em `strategies` com `config` (JSON conforme `StrategyConfig`), vinculado à `account_id`.
- Exemplo de `config`:

```json
{
  "symbol": "BTCUSDT",
  "candle": "1m",
  "min_price": 50000.0,
  "max_price": 75000.0,
  "order_value": 50.0,
  "min_profit": 0.002,
  "fee_pct": 0.0005,
  "demo_mode": true
}
```
### 7) Iniciar o orquestrador

```bash
python -m src.bot.cli start
```
- O **orquestrador**:
    - Carrega `strategies.enabled = true`.
    - Para cada estratégia, cria contexto com cliente Binance da **conta** correspondente.
    - Conecta no stream de `kline` do `symbol`/`candle`.
    - Encaminha candles para `strategy.on_tick`.
    - Executa ordens via `execution` (live/paper conforme `demo_mode`).
    - Persiste ordens e métricas.

---

## Boas práticas e separação de componentes (critérios de aceite)

- **Componentes separados**:
    - Acesso à exchange (`bot/binance/*`)
    - Estratégias (`bot/strategies/*`)
    - Persistência (`bot/db/*`)
    - Segurança de segredos (`bot/security/*`)
    - Orquestração/agendamento (`bot/runtime/*`)
    - CLI operacional (`bot/cli.py`)
    - Telemetria/logging (`bot/logging.py`)
- **Configuração por ambiente** via `.env`/variáveis.
- **Múltiplas contas/estratégias** suportadas por design (tabelas `accounts`, `strategies`).
- **Modo demonstrativo** suportado nativamente, sem alterar a lógica das estratégias.
- **Base para relatórios**: dados normalizados (`orders`/`trades`) e módulo `reporting/metrics.py`.

---

## `pyproject.toml` (mínimo)

```toml
[project]
name = "binance-bot"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []

[tool.pytest.ini_options]
testpaths = ["tests"]
```
---

## Próximos passos (opcional)

- Implementar rotinas de **risk management** (max drawdown por estratégia/conta).
- Adicionar **limpeza/rotação** de logs e **dashboards** (FastAPI + SQLite para cache de métricas).
- Implementar **relatórios** com consultas `pandas` ou views SQL materializadas.

> Esta entrega fornece a estrutura mínima funcional, com instruções de setup e exemplos de uso dos principais componentes, atendendo às restrições e critérios de aceite.

---

## Inicialização do Projeto

Execute o servidor:

```bash
uvicorn main:app --reload
```

---

# Adições: rotação/limpeza de logs e dashboards (FastAPI + SQLite)

## Alterações de arquitetura

```
binance-bot/
├─ .env.example                       # + variáveis de log e dashboard
├─ requirements.txt                   # + fastapi, uvicorn, jinja2, aiofiles, orjson
├─ var/
│  └─ log/                            # destino padrão de logs rotacionados
├─ src/
│  ├─ bot/
│  │  ├─ logging.py                   # atualizado: handlers com rotação/retention
│  │  ├─ reporting/
│  │  │  ├─ metrics.py
│  │  │  └─ cache/
│  │  │     ├─ sqlite.py             # conexão e schema de cache (SQLite)
│  │  │     └─ aggregator.py         # job que agrega do Postgres -> SQLite
│  │  └─ api/
│  │     ├─ main.py                   # FastAPI app
│  │     ├─ deps.py                   # dependências (paths, DBs)
│  │     ├─ routers/
│  │     │  ├─ health.py
│  │     │  └─ metrics.py             # endpoints de métricas (via SQLite)
│  │     ├─ templates/
│  │     │  └─ index.html             # dashboard simples (Chart.js)
│  │     └─ static/
│  │        ├─ app.js
│  │        └─ styles.css
└─ tests/
   └─ test_dashboard_api.py
```

---

## Novas dependências (append em `requirements.txt`)

```
fastapi==0.115.0
uvicorn[standard]==0.30.6
jinja2==3.1.4
aiofiles==24.1.0
orjson==3.10.7
```

---

## Variáveis de ambiente (`.env.example`)

```
# Logging
LOG_DIR=var/log
LOG_ROTATION=DAILY             # DAILY | SIZE
LOG_MAX_BYTES=10485760         # 10MB (se SIZE)
LOG_BACKUP_COUNT=14            # retenção
LOG_LEVEL=INFO

# Dashboard/Cache
DASHBOARD_SQLITE_PATH=var/cache/metrics.sqlite3
DASHBOARD_REFRESH_SECONDS=60
API_HOST=0.0.0.0
API_PORT=8000
```

---

## Rotação e limpeza de logs (`src/bot/logging.py`)

```python
import logging, sys, os, gzip, shutil
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import structlog
from bot.config import Settings

def _compress(path: str):
    gz = f"{path}.gz"
    with open(path, "rb") as f_in, gzip.open(gz, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    os.remove(path)

class GzipTimedHandler(TimedRotatingFileHandler):
    def doRollover(self):
        super().doRollover()
        for s in self.getFilesToDelete():
            _compress(s)

class GzipSizedHandler(RotatingFileHandler):
    def doRollover(self):
        super().doRollover()
        # compacta arquivos .1, .2... recém-rotacionados
        base = self.baseFilename
        for i in range(1, self.backupCount + 1):
            candidate = f"{base}.{i}"
            if os.path.exists(candidate):
                _compress(candidate)

def setup_logging():
    st = Settings()
    os.makedirs(st.LOG_DIR, exist_ok=True)
    log_path = os.path.join(st.LOG_DIR, "bot.log")

    root = logging.getLogger()
    root.handlers.clear()
    root.setLevel(st.LOG_LEVEL)

    stream = logging.StreamHandler(sys.stdout)
    stream.setLevel(st.LOG_LEVEL)

    if st.LOG_ROTATION.upper() == "DAILY":
        fileh = GzipTimedHandler(log_path, when="midnight", backupCount=int(st.LOG_BACKUP_COUNT))
    else:
        fileh = GzipSizedHandler(log_path, maxBytes=int(st.LOG_MAX_BYTES),
                                 backupCount=int(st.LOG_BACKUP_COUNT))
    fileh.setLevel(st.LOG_LEVEL)

    fmt = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    stream.setFormatter(fmt); fileh.setFormatter(fmt)
    root.addHandler(stream); root.addHandler(fileh)

    structlog.configure(processors=[structlog.processors.add_log_level,
                                    structlog.processors.TimeStamper(fmt="iso"),
                                    structlog.processors.JSONRenderer()])
    return structlog.get_logger("bot")
```

> Resultado: rotação diária (ou por tamanho), retenção por `backupCount` com compressão `.gz`.

---

## Cache de métricas em SQLite

### Schema e conexão (`src/bot/reporting/cache/sqlite.py`)

```python
import os, sqlite3
from bot.config import Settings

def get_sqlite():
    st = Settings()
    os.makedirs(os.path.dirname(st.DASHBOARD_SQLITE_PATH), exist_ok=True)
    conn = sqlite3.connect(st.DASHBOARD_SQLITE_PATH, check_same_thread=False)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS kpi_snapshots(
        ts INTEGER NOT NULL,
        strategy_id INTEGER NOT NULL,
        symbol TEXT NOT NULL,
        pnl REAL NOT NULL,
        gross REAL NOT NULL,
        fees REAL NOT NULL,
        win_rate REAL NOT NULL,
        open_trades INTEGER NOT NULL,
        closed_trades INTEGER NOT NULL,
        PRIMARY KEY (ts, strategy_id)
    ) WITHOUT ROWID;
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS ix_kpi_ts ON kpi_snapshots(ts);")
    conn.commit()
    return conn
```

### Agregador Postgres → SQLite (`src/bot/reporting/cache/aggregator.py`)

```python
from datetime import datetime, timezone, timedelta
from bot.db.base import SessionLocal
from bot.db import models
from bot.reporting.metrics import compute_kpis_for_strategy  # você já possui cálculos base
from .sqlite import get_sqlite
from bot.config import Settings
import time

def run_aggregation_loop():
    st = Settings()
    sqlite = get_sqlite()
    while True:
        with SessionLocal() as s:
            strategies = s.query(models.Strategy).filter(models.Strategy.enabled == True).all()
            now = int(datetime.now(timezone.utc).timestamp())
            for strat in strategies:
                k = compute_kpis_for_strategy(s, strat.id)  # retorna dict com métricas
                sqlite.execute(
                    "INSERT OR REPLACE INTO kpi_snapshots(ts,strategy_id,symbol,pnl,gross,fees,win_rate,open_trades,closed_trades) "
                    "VALUES (?,?,?,?,?,?,?,?,?)",
                    (now, strat.id, strat.config["symbol"], k["pnl"], k["gross"], k["fees"],
                     k["win_rate"], k["open_trades"], k["closed_trades"])
                )
            sqlite.commit()
        time.sleep(int(st.DASHBOARD_REFRESH_SECONDS))
```

> Execução: como processo separado (systemd/PM2) ou dentro do orquestrador via `APScheduler` (job em background).

---

## API/Dashboard (FastAPI)

### App e montagem (`src/bot/api/main.py`)

```python
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from .routers import health, metrics

app = FastAPI(title="Binance Bot Dashboard")
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(metrics.router, prefix="/metrics", tags=["metrics"])

app.mount("/static", StaticFiles(directory="src/bot/api/static"), name="static")
templates = Jinja2Templates(directory="src/bot/api/templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
```

### Endpoints (`src/bot/api/routers/metrics.py`)

```python
from fastapi import APIRouter, Query
from ..deps import get_sqlite_conn

router = APIRouter()

@router.get("/strategies")
def strategies_snapshot(limit: int = Query(200)):
    conn = get_sqlite_conn()
    cur = conn.execute("""
        SELECT ts, strategy_id, symbol, pnl, gross, fees, win_rate, open_trades, closed_trades
        FROM kpi_snapshots
        ORDER BY ts DESC
        LIMIT ?;
    """, (limit,))
    cols = [c[0] for c in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]

@router.get("/strategy/{strategy_id}/series")
def strategy_series(strategy_id: int, since_ts: int | None = None, limit: int = 1440):
    conn = get_sqlite_conn()
    if since_ts:
        cur = conn.execute("""
            SELECT ts, pnl, gross, fees, win_rate, open_trades, closed_trades
            FROM kpi_snapshots
            WHERE strategy_id = ? AND ts >= ?
            ORDER BY ts ASC LIMIT ?;
        """, (strategy_id, since_ts, limit))
    else:
        cur = conn.execute("""
            SELECT ts, pnl, gross, fees, win_rate, open_trades, closed_trades
            FROM kpi_snapshots
            WHERE strategy_id = ?
            ORDER BY ts ASC LIMIT ?;
        """, (strategy_id, limit))
    cols = [c[0] for c in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]
```

### Dependência de conexão (`src/bot/api/deps.py`)

```python
from bot.reporting.cache.sqlite import get_sqlite
_sqlite = None
def get_sqlite_conn():
    global _sqlite
    if _sqlite is None:
        _sqlite = get_sqlite()
    return _sqlite
```

### Front-end mínimo (Chart.js)

`src/bot/api/templates/index.html`

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8"><title>Dashboard</title>
		<link rel="stylesheet" href="/static/styles.css">
	</head>
	<body>
		<h1>Dashboard</h1>
		<canvas id="equity"></canvas>
		<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
		<script src="/static/app.js"></script>
	</body>
</html>
```

`src/bot/api/static/app.js`

```js
async function load(strategyId=1){
  const r = await fetch(`/metrics/strategy/${strategyId}/series?limit=500`);
  const data = await r.json();
  const labels = data.map(d=>new Date(d.ts*1000).toLocaleString());
  const pnl = data.map(d=>d.pnl);
  const ctx = document.getElementById('equity').getContext('2d');
  new Chart(ctx,{type:'line',data:{labels,
    datasets:[{label:'PnL',data:pnl,fill:false}]},
    options:{responsive:true,maintainAspectRatio:false}});
}
load();
```

---

## Integração operacional

### 1) Instalação/atualização

```bash
pip install -r requirements.txt
```

### 2) Ajustes de `.env`

- Defina `LOG_DIR`, `LOG_ROTATION` e `LOG_BACKUP_COUNT`.
- Defina `DASHBOARD_SQLITE_PATH` e `DASHBOARD_REFRESH_SECONDS`.

### 3) Habilitar rotação de logs

- Garanta que `setup_logging()` seja chamado no bootstrap do orquestrador/CLI:

```python
# src/bot/cli.py
from bot.logging import setup_logging
logger = setup_logging()
```

### 4) Iniciar agregador de cache

- Como processo dedicado (recomendado):

```bash
python -c "from src.bot.reporting.cache.aggregator import run_aggregation_loop; run_aggregation_loop()"
```

- Alternativa (APScheduler no orquestrador): agendar `run_aggregation_loop` como job em thread separada.

### 5) Subir a API/Dashboard

```bash
uvicorn src.bot.api.main:app --host ${API_HOST:-0.0.0.0} --port ${API_PORT:-8000}
```

### 6) Acesso

- Navegue até `http://<host>:8000/` para o dashboard.
- Endpoints JSON: `GET /metrics/strategies`, `GET /metrics/strategy/{id}/series`.

---

## Notas de projeto

- **Isolamento de escrita**: SQLite apenas para leitura pela API; escrita é exclusiva do agregador.
- **Retenção de cache**: opcionalmente, crie um job de limpeza no SQLite, por exemplo:
    ```sql
    DELETE FROM kpi_snapshots WHERE ts < strftime('%s','now','-30 days');
    ```
- **Segurança**: publicar a API atrás de um reverse proxy com autenticação (ex.: Basic Auth no proxy).
- **Escalabilidade**: para maior throughput, migrar Chart.js para consultas assíncronas paginadas e introduzir downsampling no agregador.

---


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/01-visao-geral/primeiros-passos-no-desenvolvimento/)

<sup><sub>
Renée Maksoud - julho de 2025
</sub></sup>

