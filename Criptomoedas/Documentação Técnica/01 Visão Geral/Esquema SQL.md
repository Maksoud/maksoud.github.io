# Revisão do esquema SQL — Bot de Trading Binance (PostgreSQL)
Atualizado em 13/08/2025

A sua proposta **cobre parcialmente** os requisitos. Pontos fortes: entidades centrais (`clients`, `symbols`, `strategies`, `positions`, `trades`, `capital_allocations`) e índices básicos.  
Lacunas em relação aos requisitos funcionais já descritos no projeto:

1. **Múltiplas chaves/contas por cliente**: hoje há apenas `api_key`/`api_secret` em `clients`. Necessário **`accounts`** (n:1 com `clients`) para suportar várias contas por cliente, com `market` (spot/futures) e `testnet`.
2. **Compartilhamento de estratégias**: hoje `strategies` está amarrada a `client_id`. Para compartilhar, separe **template** de **instância**:
    - `strategy_templates` (parametrização reutilizável).
    - `strategies` (instâncias por conta/símbolo, referenciando o template).
3. **Modo demonstrativo (paper)**: falta o flag por estratégia/ordem/execução. Adicione `execution_mode` (`live|demo`) em `strategies` e propague para `positions`/`trades`.
4. **Parâmetros adicionais**: `candle`, `order_value`, `fee_pct`, `slippage`, etc. Sugestão: `params JSONB` nos templates e `params_override JSONB` nas instâncias.
5. **Precisão e timezone**: criptos exigem alta precisão; use `NUMERIC(38,18)` e `TIMESTAMPTZ`.
6. **Segurança**: não armazene chaves em texto claro. Use colunas `*_enc` para valores criptografados no app.
7. **Consistência de nomes**: o requisito fala em _preço mínimo/máximo_. Você usa `base_price/top_price`. Recomendo `min_price/max_price` (ou mantenha e documente o mapeamento).
8. **Índices/uniques**: incluir chaves únicas para evitar duplicidades de instâncias por conta/símbolo/template e melhorar consultas por período/estratégia.

A seguir, um **esquema inicial revisado** que incorpora esses pontos.

---

## Esquema revisado (DDL completo)

> Observação: se é um projeto novo, use o script abaixo “como está”. Se já houver dados, trate como migração planejada.

```sql
-- Banco (opcional se já criado)
-- CREATE DATABASE criptoren;
-- \c criptoren;

-- Extensões úteis
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
-- pgcrypto pode ser útil para hashes/geração de sal, mas a criptografia será feita na aplicação.

-- Tipos enumerados
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'market_type') THEN
        CREATE TYPE market_type AS ENUM ('spot','futures');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'exec_mode') THEN
        CREATE TYPE exec_mode AS ENUM ('live','demo');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'position_status') THEN
        CREATE TYPE position_status AS ENUM ('open','scheduled','closed');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'trade_side') THEN
        CREATE TYPE trade_side AS ENUM ('buy','sell');
    END IF;
END $$;

-- ====== Núcleo de clientes e contas ======

CREATE TABLE IF NOT EXISTS clients (
    id          BIGSERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL UNIQUE,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

-- Múltiplas contas por cliente (cada uma com credenciais próprias)
CREATE TABLE IF NOT EXISTS accounts (
    id              BIGSERIAL PRIMARY KEY,
    client_id       BIGINT NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    name            VARCHAR(100) NOT NULL,                -- apelido (ex.: "Conta Spot Principal")
    market          market_type NOT NULL DEFAULT 'spot',  -- spot/futures
    testnet         BOOLEAN NOT NULL DEFAULT FALSE,
    api_key_enc     TEXT NOT NULL,                        -- armazenar criptografado no app
    api_secret_enc  TEXT NOT NULL,                        -- armazenar criptografado no app
    is_active       BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT uq_account_per_client UNIQUE (client_id, name)
);

-- ====== Símbolos negociáveis ======
CREATE TABLE IF NOT EXISTS symbols (
    id          BIGSERIAL PRIMARY KEY,
    symbol      VARCHAR(20) NOT NULL UNIQUE,   -- ex.: BTCUSDT
    base_asset  VARCHAR(20) NOT NULL,
    quote_asset VARCHAR(20) NOT NULL,
    is_active   BOOLEAN DEFAULT TRUE,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ====== Estratégias: template reutilizável ======
CREATE TABLE IF NOT EXISTS strategy_templates (
    id              BIGSERIAL PRIMARY KEY,
    name            VARCHAR(100) NOT NULL UNIQUE,
    min_price       NUMERIC(38,18) NOT NULL,              -- preço mínimo (ex: canal inferior)
    max_price       NUMERIC(38,18) NOT NULL,              -- preço máximo (ex: canal superior)
    buy_threshold   NUMERIC(10,6)  NOT NULL,              -- % / fator para compra
    sell_threshold  NUMERIC(10,6)  NOT NULL,              -- % / fator para venda
    min_profit      NUMERIC(10,6)  NOT NULL,              -- lucro mínimo alvo (fração)
    params          JSONB          NOT NULL DEFAULT '{}'::jsonb, 
    -- params exemplo: {"candle":"1m","order_value":50.0,"fee_pct":0.0005,"slippage":0.0002}
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW(),
    CHECK (max_price > min_price)
);

-- ====== Estratégias instanciadas por conta/símbolo ======
CREATE TABLE IF NOT EXISTS strategies (
    id                  BIGSERIAL PRIMARY KEY,
    template_id         BIGINT NOT NULL REFERENCES strategy_templates(id) ON DELETE RESTRICT,
    account_id          BIGINT NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    symbol_id           BIGINT NOT NULL REFERENCES symbols(id) ON DELETE RESTRICT,
    execution_mode      exec_mode NOT NULL DEFAULT 'demo',   -- live|demo
    capital_percentage  NUMERIC(10,4) NOT NULL CHECK (capital_percentage > 0 AND capital_percentage <= 100),
    is_active           BOOLEAN DEFAULT TRUE,
    params_override     JSONB   NOT NULL DEFAULT '{}'::jsonb, -- sobrescritas do template
    created_at          TIMESTAMPTZ DEFAULT NOW(),
    updated_at          TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT uq_strategy_per_account UNIQUE (account_id, symbol_id, template_id)
);

CREATE INDEX IF NOT EXISTS idx_strategies_active ON strategies(is_active);
CREATE INDEX IF NOT EXISTS idx_strategies_account ON strategies(account_id);
CREATE INDEX IF NOT EXISTS idx_strategies_symbol ON strategies(symbol_id);

-- ====== Posições (ciclo de trade) ======
CREATE TABLE IF NOT EXISTS positions (
    id                  BIGSERIAL PRIMARY KEY,
    strategy_id         BIGINT NOT NULL REFERENCES strategies(id) ON DELETE CASCADE,
    symbol_id           BIGINT NOT NULL REFERENCES symbols(id) ON DELETE RESTRICT,
    execution_mode      exec_mode NOT NULL,               -- snapshot do modo no momento da abertura
    entry_price         NUMERIC(38,18) NOT NULL,
    quantity            NUMERIC(38,18) NOT NULL,
    fees                NUMERIC(38,18) DEFAULT 0,
    status              position_status NOT NULL DEFAULT 'open',
    exit_price          NUMERIC(38,18),
    scheduled_exit_price NUMERIC(38,18),
    channel_exit_date   TIMESTAMPTZ,
    closed_at           TIMESTAMPTZ,
    created_at          TIMESTAMPTZ DEFAULT NOW(),
    updated_at          TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_positions_strategy ON positions(strategy_id);
CREATE INDEX IF NOT EXISTS idx_positions_status ON positions(status);
CREATE INDEX IF NOT EXISTS idx_positions_symbol ON positions(symbol_id);

-- ====== Trades (execuções efetivas ou simuladas) ======
CREATE TABLE IF NOT EXISTS trades (
    id              BIGSERIAL PRIMARY KEY,
    position_id     BIGINT REFERENCES positions(id) ON DELETE SET NULL,
    strategy_id     BIGINT NOT NULL REFERENCES strategies(id) ON DELETE CASCADE,
    account_id      BIGINT NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    client_id       BIGINT NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    symbol_id       BIGINT NOT NULL REFERENCES symbols(id) ON DELETE RESTRICT,
    side            trade_side NOT NULL,                  -- buy|sell
    execution_mode  exec_mode   NOT NULL,                 -- live|demo (snapshot)
    price           NUMERIC(38,18) NOT NULL,
    quantity        NUMERIC(38,18) NOT NULL,
    fees            NUMERIC(38,18) DEFAULT 0,
    profit          NUMERIC(38,18),
    notes           TEXT,
    executed_at     TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_trades_symbol_executed ON trades(symbol_id, executed_at);
CREATE INDEX IF NOT EXISTS idx_trades_strategy_executed ON trades(strategy_id, executed_at);
CREATE INDEX IF NOT EXISTS idx_trades_client_executed ON trades(client_id, executed_at);

-- ====== Alocação de capital ======
CREATE TABLE IF NOT EXISTS capital_allocations (
    id              BIGSERIAL PRIMARY KEY,
    client_id       BIGINT NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    account_id      BIGINT NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    strategy_id     BIGINT NOT NULL REFERENCES strategies(id) ON DELETE CASCADE,
    amount          NUMERIC(38,18) NOT NULL,
    is_profit       BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_capital_client ON capital_allocations(client_id);
CREATE INDEX IF NOT EXISTS idx_capital_strategy ON capital_allocations(strategy_id);

-- ====== Gatilho genérico de updated_at ======
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar gatilhos onde há updated_at
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN SELECT table_name
             FROM information_schema.columns
             WHERE table_schema='public' AND column_name='updated_at'
    LOOP
        EXECUTE format($f$
            DO $inner$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM pg_trigger
                    WHERE tgname = 'update_%1$s_timestamp'
                ) THEN
                    CREATE TRIGGER update_%1$s_timestamp
                    BEFORE UPDATE ON %1$s
                    FOR EACH ROW EXECUTE FUNCTION update_timestamp();
                END IF;
            END
            $inner$;
        $f$, r.table_name);
    END LOOP;
END $$;
```

---

## Como isso cobre seus requisitos

- **Várias contas/credenciais por cliente**: `accounts(client_id, ...)` com `market` e `testnet`. Campos `api_key_enc`/`api_secret_enc` preparados para **armazenar chaves criptografadas** pela aplicação.
- **Estratégias compartilháveis**: defina uma vez em `strategy_templates`; reutilize em múltiplos clientes/contas via `strategies` (instâncias).
- **Parâmetros por estratégia**: mínimos explícitos (`min_price`, `max_price`, `min_profit`, thresholds) + `params JSONB` para `candle`, `order_value`, `fee_pct`, etc. Possíveis overrides por instância (`params_override`).
- **Modo demonstrativo**: `execution_mode` em `strategies` e **snapshot** em `positions`/`trades` para auditoria consistente.
- **Relatórios futuros**: índices por `strategy_id`, `client_id`, `executed_at` e normalização adequada (`capital_allocations`) facilitam agregações.
- **Precisão e fuso**: `NUMERIC(38,18)` e `TIMESTAMPTZ` adequados a cripto e auditoria.

---

## Se quiser evoluir a partir do seu script atual

Se preferir **minimizar mudanças**:

1. **Mover credenciais** de `clients` para uma nova `accounts` e preencher `accounts.client_id = clients.id`.
2. **Manter `strategies`** como está e adicionar:
    - `execution_mode exec_mode NOT NULL DEFAULT 'demo'`
    - `params JSONB NOT NULL DEFAULT '{}'::jsonb`
    - `CHECK (top_price > base_price)`  
        Depois, quando precisar compartilhar, introduza gradualmente `strategy_templates` e migre.
3. **Ajustar precisão/timezone**: alterar `DECIMAL(18,8)` → `NUMERIC(38,18)` e `TIMESTAMP` → `TIMESTAMPTZ` conforme necessário.

Exemplos de alterações rápidas:

```sql
ALTER TABLE clients DROP COLUMN IF EXISTS api_key, DROP COLUMN IF EXISTS api_secret;

-- 1) criar accounts e relacionar
-- (use INSERT ... SELECT para popular a partir das chaves existentes, se houver backup)

-- 2) complementar strategies
ALTER TABLE strategies
    ADD COLUMN IF NOT EXISTS execution_mode exec_mode NOT NULL DEFAULT 'demo',
    ADD COLUMN IF NOT EXISTS params JSONB NOT NULL DEFAULT '{}'::jsonb,
    ADD CONSTRAINT chk_price_channel CHECK (top_price > base_price);

-- 3) precisão e timezone (exemplo em uma coluna)
ALTER TABLE positions
    ALTER COLUMN entry_price TYPE NUMERIC(38,18),
    ALTER COLUMN created_at TYPE TIMESTAMPTZ USING created_at AT TIME ZONE 'UTC';
```

---

# Alembic — Migração inicial do esquema (PostgreSQL)

Abaixo estão os arquivos e passos para versionar **o DDL revisado** com Alembic.

## Passos de setup

```bash
# 1) Instalar
pip install alembic

# 2) Inicializar estrutura em src/alembic
alembic init src/alembic

# 3) Configurar URL do banco no alembic.ini (ou usar variável de ambiente)
# abra alembic.ini e ajuste:
# sqlalchemy.url = postgresql+psycopg://user:password@localhost:5432/criptoren

# 4) (Opcional) Deixe o env.py ler DB_URL do .env/ambiente
# substitua o conteúdo de src/alembic/env.py pelo fornecido abaixo

# 5) Criar a revisão inicial com ID fixo
alembic revision -m "init schema" --rev-id 0001_init

# 6) Substitua o conteúdo do arquivo src/alembic/versions/0001_init.py
# pelo código abaixo

# 7) Aplicar
alembic upgrade head
```

---

## `src/alembic/env.py` (mínimo, síncrono; lê `DB_URL` se `alembic.ini` estiver vazio)

```python
from logging.config import fileConfig
import os
from sqlalchemy import engine_from_config, pool
from alembic import context

# Config alembic.ini
config = context.config

# Permite usar variável de ambiente DB_URL como fallback
db_url_env = os.getenv("DB_URL")
if db_url_env:
    config.set_main_option("sqlalchemy.url", db_url_env)

# Logging Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Sem autogenerate neste passo (DDL manual)
target_metadata = None

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

---

## `src/alembic/versions/0001_init.py`

```python
"""init schema

Revision ID: 0001_init
Revises: 
Create Date: 2025-08-13 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as psql

# revision identifiers, used by Alembic.
revision = "0001_init"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Extensões úteis (idempotentes)
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

    # Tipos ENUM (PostgreSQL)
    market_type = psql.ENUM("spot", "futures", name="market_type")
    exec_mode = psql.ENUM("live", "demo", name="exec_mode")
    position_status = psql.ENUM("open", "scheduled", "closed", name="position_status")
    trade_side = psql.ENUM("buy", "sell", name="trade_side")

    bind = op.get_bind()
    market_type.create(bind, checkfirst=True)
    exec_mode.create(bind, checkfirst=True)
    position_status.create(bind, checkfirst=True)
    trade_side.create(bind, checkfirst=True)

    # Tabela: clients
    op.create_table(
        "clients",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=100), nullable=False, unique=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
    )

    # Tabela: accounts (múltiplas contas por cliente)
    op.create_table(
        "accounts",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column("client_id", sa.BigInteger(), sa.ForeignKey("clients.id", ondelete="CASCADE"), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("market", sa.Enum(name="market_type", native_enum=False), nullable=False, server_default="spot"),
        sa.Column("testnet", sa.Boolean(), nullable=False, server_default=sa.text("FALSE")),
        sa.Column("api_key_enc", sa.Text(), nullable=False),
        sa.Column("api_secret_enc", sa.Text(), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("TRUE")),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.UniqueConstraint("client_id", "name", name="uq_account_per_client"),
    )

    # Tabela: symbols
    op.create_table(
        "symbols",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column("symbol", sa.String(length=20), nullable=False, unique=True),
        sa.Column("base_asset", sa.String(length=20), nullable=False),
        sa.Column("quote_asset", sa.String(length=20), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("TRUE")),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
    )

    # Tabela: strategy_templates (reúso/compartilhamento)
    op.create_table(
        "strategy_templates",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=100), nullable=False, unique=True),
        sa.Column("min_price", sa.Numeric(38, 18), nullable=False),
        sa.Column("max_price", sa.Numeric(38, 18), nullable=False),
        sa.Column("buy_threshold", sa.Numeric(10, 6), nullable=False),
        sa.Column("sell_threshold", sa.Numeric(10, 6), nullable=False),
        sa.Column("min_profit", sa.Numeric(10, 6), nullable=False),
        sa.Column("params", psql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.CheckConstraint("max_price > min_price", name="chk_template_price"),
    )

    # Tabela: strategies (instâncias por conta/símbolo)
    op.create_table(
        "strategies",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column("template_id", sa.BigInteger(), sa.ForeignKey("strategy_templates.id", ondelete="RESTRICT"), nullable=False),
        sa.Column("account_id", sa.BigInteger(), sa.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False),
        sa.Column("symbol_id", sa.BigInteger(), sa.ForeignKey("symbols.id", ondelete="RESTRICT"), nullable=False),
        sa.Column("execution_mode", sa.Enum(name="exec_mode", native_enum=False), nullable=False, server_default="demo"),
        sa.Column("capital_percentage", sa.Numeric(10, 4), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("TRUE")),
        sa.Column("params_override", psql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.CheckConstraint("capital_percentage > 0 AND capital_percentage <= 100", name="chk_strategy_capital_pct"),
        sa.UniqueConstraint("account_id", "symbol_id", "template_id", name="uq_strategy_per_account"),
    )
    op.create_index("idx_strategies_active", "strategies", ["is_active"])
    op.create_index("idx_strategies_account", "strategies", ["account_id"])
    op.create_index("idx_strategies_symbol", "strategies", ["symbol_id"])

    # Tabela: positions
    op.create_table(
        "positions",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column("strategy_id", sa.BigInteger(), sa.ForeignKey("strategies.id", ondelete="CASCADE"), nullable=False),
        sa.Column("symbol_id", sa.BigInteger(), sa.ForeignKey("symbols.id", ondelete="RESTRICT"), nullable=False),
        sa.Column("execution_mode", sa.Enum(name="exec_mode", native_enum=False), nullable=False),
        sa.Column("entry_price", sa.Numeric(38, 18), nullable=False),
        sa.Column("quantity", sa.Numeric(38, 18), nullable=False),
        sa.Column("fees", sa.Numeric(38, 18), server_default=sa.text("0"), nullable=False),
        sa.Column("status", sa.Enum(name="position_status", native_enum=False), nullable=False, server_default="open"),
        sa.Column("exit_price", sa.Numeric(38, 18)),
        sa.Column("scheduled_exit_price", sa.Numeric(38, 18)),
        sa.Column("channel_exit_date", sa.TIMESTAMP(timezone=True)),
        sa.Column("closed_at", sa.TIMESTAMP(timezone=True)),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
    )
    op.create_index("idx_positions_strategy", "positions", ["strategy_id"])
    op.create_index("idx_positions_status", "positions", ["status"])
    op.create_index("idx_positions_symbol", "positions", ["symbol_id"])

    # Tabela: trades
    op.create_table(
        "trades",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column("position_id", sa.BigInteger(), sa.ForeignKey("positions.id", ondelete="SET NULL")),
        sa.Column("strategy_id", sa.BigInteger(), sa.ForeignKey("strategies.id", ondelete="CASCADE"), nullable=False),
        sa.Column("account_id", sa.BigInteger(), sa.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False),
        sa.Column("client_id", sa.BigInteger(), sa.ForeignKey("clients.id", ondelete="CASCADE"), nullable=False),
        sa.Column("symbol_id", sa.BigInteger(), sa.ForeignKey("symbols.id", ondelete="RESTRICT"), nullable=False),
        sa.Column("side", sa.Enum(name="trade_side", native_enum=False), nullable=False),
        sa.Column("execution_mode", sa.Enum(name="exec_mode", native_enum=False), nullable=False),
        sa.Column("price", sa.Numeric(38, 18), nullable=False),
        sa.Column("quantity", sa.Numeric(38, 18), nullable=False),
        sa.Column("fees", sa.Numeric(38, 18), server_default=sa.text("0"), nullable=False),
        sa.Column("profit", sa.Numeric(38, 18)),
        sa.Column("notes", sa.Text()),
        sa.Column("executed_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
    )
    op.create_index("idx_trades_symbol_executed", "trades", ["symbol_id", "executed_at"])
    op.create_index("idx_trades_strategy_executed", "trades", ["strategy_id", "executed_at"])
    op.create_index("idx_trades_client_executed", "trades", ["client_id", "executed_at"])

    # Tabela: capital_allocations
    op.create_table(
        "capital_allocations",
        sa.Column("id", sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column("client_id", sa.BigInteger(), sa.ForeignKey("clients.id", ondelete="CASCADE"), nullable=False),
        sa.Column("account_id", sa.BigInteger(), sa.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False),
        sa.Column("strategy_id", sa.BigInteger(), sa.ForeignKey("strategies.id", ondelete="CASCADE"), nullable=False),
        sa.Column("amount", sa.Numeric(38, 18), nullable=False),
        sa.Column("is_profit", sa.Boolean(), server_default=sa.text("FALSE")),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("NOW()"), nullable=False),
    )
    op.create_index("idx_capital_client", "capital_allocations", ["client_id"])
    op.create_index("idx_capital_strategy", "capital_allocations", ["strategy_id"])

    # Função e triggers de updated_at
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_timestamp()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        """
    )

    # Triggers por tabela com updated_at
    for table in ("clients","accounts","symbols","strategy_templates","strategies","positions"):
        op.execute(
            f"""
            CREATE TRIGGER update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_timestamp();
            """
        )


def downgrade() -> None:
    # Remover triggers (ordem inversa não é obrigatória, mas organiza)
    for table in ("positions","strategies","strategy_templates","symbols","accounts","clients"):
        op.execute(f"DROP TRIGGER IF EXISTS update_{table}_timestamp ON {table};")

    # Função
    op.execute("DROP FUNCTION IF EXISTS update_timestamp();")

    # Índices
    op.drop_index("idx_capital_strategy", table_name="capital_allocations")
    op.drop_index("idx_capital_client", table_name="capital_allocations")
    op.drop_index("idx_trades_client_executed", table_name="trades")
    op.drop_index("idx_trades_strategy_executed", table_name="trades")
    op.drop_index("idx_trades_symbol_executed", table_name="trades")
    op.drop_index("idx_positions_symbol", table_name="positions")
    op.drop_index("idx_positions_status", table_name="positions")
    op.drop_index("idx_positions_strategy", table_name="positions")
    op.drop_index("idx_strategies_symbol", table_name="strategies")
    op.drop_index("idx_strategies_account", table_name="strategies")
    op.drop_index("idx_strategies_active", table_name="strategies")

    # Tabelas (em ordem de dependência)
    op.drop_table("capital_allocations")
    op.drop_table("trades")
    op.drop_table("positions")
    op.drop_table("strategies")
    op.drop_table("strategy_templates")
    op.drop_table("symbols")
    op.drop_table("accounts")
    op.drop_table("clients")

    # Tipos ENUM
    bind = op.get_bind()
    psql.ENUM(name="trade_side").drop(bind, checkfirst=True)
    psql.ENUM(name="position_status").drop(bind, checkfirst=True)
    psql.ENUM(name="exec_mode").drop(bind, checkfirst=True)
    psql.ENUM(name="market_type").drop(bind, checkfirst=True)
```

---

## Notas

- `native_enum=False` faz com que as colunas referenciem o tipo já criado (nomeado) no banco. Mantém o controle explícito dos tipos via `psql.ENUM.create/drop`.
- Todos os `*_at` usam `TIMESTAMPTZ` (`sa.TIMESTAMP(timezone=True)`) com `NOW()` e recebem trigger de atualização.
- Precisões: valores monetários/quantidades usam `NUMERIC(38,18)`.
- Se você já possuir `alembic` com outro `script_location`, ajuste os caminhos de acordo.

---
## Próximos passos

- Definir contrato dos `params` (chaves obrigatórias, validações) no código (Pydantic).
- Implementar criptografia das chaves no app (ex.: `cryptography.Fernet`) antes de persistir em `accounts`.
- Criar **views**/materialized views para relatórios (ex.: PnL diário por estratégia).