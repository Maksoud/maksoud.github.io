### Sumário > Projeto de Gestão de Criptomoedas

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

- Python 3.11+
- **ccxt** (acesso Binance spot/testnet)
- **pandas** (manipulação de dados)
- **SQLAlchemy + Alembic** (ORM + migrações)
- **PostgreSQL** (ou **SQLite** pra começar local)
- **pydantic** (validação de configs)
- **loguru** (logs)
- (Opcional) **FastAPI** + **Uvicorn** só pra expor relatórios/healthcheck depois


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



> **Papel:** Você é um arquiteto de software Python especialista em operações com criptoativos na corretora Binance.
> **Objetivo:** Propor a arquitetura mínima para um bot de cripto em trading na Binance.  
> **Contexto:** Identifique as bibliotecas que serão necessárias para criação desse ambiente, esperando que atenda a todos os requisitos de software esperados. Sistema com o gerenciamento diversas chaves de APIs (diferentes contas da Binance), diversas estratégias poderão ser iniciadas na mesma conta. As estratégias serão configuráveis para que melhor se adaptem a necessidade do cliente. As estratégias poderão ser compartilhadas entre clientes. Cada estratégia precisa informar se sua execução está em modo demonstrativo, ou seja, não irá executar as compras e vendas na corretora, apenas registrar em banco de dados como simulação das operações. Uma estratégia irá precisar de informações como preço máximo, preço mínimo, valor de operação, par da moeda em operação, candle utilizado, valor mínimo de lucro, percentual da taxa operacional, etc. Relatórios serão criados posteriormente para acompanhamento do desempenho de cada estratégia. 
> **Restrições:** Python em sua versão mais atualizada. Versionamento no Github. Banco de dados PostgreSQL.
> **Entregáveis:** árvore de pastas, dependências (requirements.txt), listagem das bibliotecas utilizadas com uma breve descrição da sua aplicação com exemplos estruturados.
> **Critérios de aceite:** componentes separados; instruções detalhadas de setup.
> **Formato da resposta:** Markdown conciso com árvore do projeto e passos de instalação/execução; não utilizar emojis ou explicações simplificadas sobre o material exposto.


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/prompts/prompt-de-requisitos/)

<sup><sub>
Criptoren - Renée Maksoud - agosto de 2025
</sub></sup>
