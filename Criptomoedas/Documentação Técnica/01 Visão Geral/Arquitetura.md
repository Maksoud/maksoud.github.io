# 🪙 Criptoren - Sistema Automatizado de Operações com Criptomoedas

## 📌 Visão Geral

Este projeto é o MVP de um sistema de negociação automatizada baseado na estratégia **Canal de Preço com Controle de Capital e Venda Programada com Lucro**. O sistema monitora os preços de criptomoedas em tempo real via WebSocket da Binance, identifica oportunidades de compra conforme valorização sobre o fundo do canal e agenda vendas com lucro após desvalorização controlada.

## 🧱 Arquitetura

```
frontend/          → Interface Web simples (HTML, JS, CSS)
main.py            → Inicialização da aplicação FastAPI
config.py          → Configurações gerais
db_config.py       → Parâmetros de conexão com banco
app/
├── api/           → Rotas da API REST
├── services/      → Serviços de execução da estratégia e WebSocket
├── models.py      → Definição das tabelas SQLAlchemy
├── database.py    → Conexão e sessão com banco PostgreSQL
├── schemas.py     → Schemas de entrada/saída (Pydantic)
├── utils.py       → Funções auxiliares
├── create_tables.py → Script de criação das tabelas
```

## ⚙️ Configurações

### `config.py`

Contém variáveis globais e parâmetros usados ao longo da aplicação, como chave da Binance, porcentagens de operação, limites do canal e lucros mínimos.

### `db_config.py`

Define as credenciais de conexão com banco PostgreSQL. A conexão é ajustada dinamicamente com base nas variáveis de ambiente (armazenadas no arquivo `.env`, ainda em construção).

## 🚀 Inicialização da API

### `main.py`

- Instancia a FastAPI
- Conecta o roteador da API (`routes.py`)
- Executa servidor ASGI

## 🔄 Rotas da API

### `routes.py`

Rotas disponíveis:

- `/start` → inicia o monitoramento
- `/stop` → encerra o monitoramento
- `/status` → verifica status da conexão

## 🗃️ Banco de Dados

### `models.py`

Define as tabelas principais:

- `Operacao`: operação realizada (compra ou venda)
- `Estrategia`: configurações da estratégia utilizada
- `Log`: eventos e status registrados

### `database.py`

- Cria engine SQLAlchemy para PostgreSQL
- Gera sessão de banco

### `schemas.py`

Este módulo define os schemas utilizados pela API para validação e serialização de dados com **Pydantic**. Ele garante que as estruturas recebidas e retornadas pelas rotas sigam um formato padronizado e validado.

**Principais schemas definidos:**

- `OperacaoSchema`:
    - Representa uma operação de compra ou venda.
    - Campos: `id`, `preco_compra`, `preco_venda`, `quantidade`, `data_compra`, `data_venda`, `status`, `estrategia_id`
- `EstrategiaSchema`:
    - Utilizado para criação e leitura de estratégias de operação.
    - Campos: `id`, `nome`, `par`, `capital_alocado`, `considera_lucro`, `limite_inferior`, `limite_superior`, `pct_valorizacao_compra`, `pct_desvalorizacao_venda`, `lucro_minimo`
- `LogSchema`:
    - Representa uma entrada de log do sistema.
    - Campos: `id`, `mensagem`, `tipo`, `data`

**Utilização:**  
Esses schemas são usados como modelos de entrada e saída nas rotas **FastAPI** (`routes.py`), garantindo validação de dados automática e documentação automática com **OpenAPI/Swagger**.

### `create_tables.py`

- Script usado para gerar todas as tabelas definidas em `models.py` no banco PostgreSQL local

## 📈 Execução da Estratégia

### `trade_service.py`

Este módulo é responsável pela lógica de negócios relacionada à execução das estratégias de compra e venda.

**Principais responsabilidades:**

- Verificar se o preço atual permite uma **compra** conforme critérios de valorização.
- Verificar se o preço atual permite uma **venda** com lucro conforme critérios definidos.
- Registrar operações no banco de dados.

**Funções principais:**

- `check_buy_opportunity(current_price: float)`
    - Verifica se há uma oportunidade de compra com base na valorização do fundo do canal.
    - Calcula o percentual de valorização desde o fundo e compara com o limite configurado.
    - Em caso positivo, executa a compra e registra no banco.
- `check_sell_opportunity(current_price: float)`
    - Verifica se há uma posição aberta e se o preço atual permite uma venda com lucro.
    - Considera o preço de compra, taxas, lucro mínimo e desvalorização relativa ao topo.
    - Em caso positivo, executa a venda e atualiza o status no banco.
- `register_buy(price: float, quantidade: float)`
    - Insere uma nova entrada de operação com status 'Aberta'.
- `register_sell(price: float)`
    - Atualiza a operação atual com status 'Encerrada' e registra os detalhes da venda.

**Dependências:**

- `database` para persistência
- `config` para parâmetros da estratégia
- `models` para manipulação dos dados

**Observação:**  
Este serviço é chamado continuamente com base nas atualizações do WebSocket e atua como executor das decisões operacionais do sistema. após valorização de X% do fundo

- Programa venda com lucro mínimo após desvalorização Y% do topo
- Nunca vende com prejuízo (regra essencial)

### `binance_ws_client.py`

- Conecta ao WebSocket da Binance
- Recebe dados em tempo real para o par configurado (ex: BTC/USDT)
- Atualiza o preço atual para a estratégia

### `websocket_manager.py`

- Controla o estado de execução do WebSocket
- Evita múltiplas conexões simultâneas

## 🔁 Fluxo de Execução

1. Operador inicia o sistema via `/start`
2. WebSocket é conectado
3. Sistema monitora o preço atual e identifica valorização X% sobre fundo
4. Realiza compra e registra no banco
5. Monitora se ocorre queda Y% a partir do topo com lucro
6. Realiza venda programada com lucro

## 🧠 Integração com Estratégia

- **Canal de preço:** limite inferior e superior são respeitados
- **Compra após valorização:** evita lateralizações e quedas contínuas
- **Venda após desvalorização:** só com lucro (nunca vende com prejuízo)
- **Capital alocado:** 20% da banca
- **Lucros não reinvestidos automaticamente**

---

## 🔍 Avaliação da Implementação da Estratégia

Com base na lógica documentada e na análise do código atual no arquivo `trade_service.py`, identificamos os seguintes pontos em relação à estratégia definida:

### 🎯 Estratégia Definida

- Monitorar cotações em tempo real
- **Comprar** quando houver valorização de 2% a partir do fundo do canal
- **Vender** com lucro quando houver desvalorização de 2% a partir do teto do canal, desde que haja lucro mínimo de 0,5%
- **Rompimento para baixo:** programar venda com 0,5% de lucro sobre o preço de compra
- Nunca realizar venda com prejuízo
- Toda compra deve resultar em uma venda programada, mesmo em rompimento



### ✍️ Recomendação

Esses pontos devem ser descritos como tarefas de backlog no desenvolvimento e incluídos na documentação da estratégia, garantindo que o comportamento automatizado esteja alinhado com a lógica de controle de risco e capital planejada.

---
## 📌 Próximos Passos

- Implementar controle visual de posições abertas/vendidas
- Adicionar testes automatizados
- Documentar melhor os logs e falhas de operação
- Possibilitar uso com múltiplos pares e múltiplas estratégias

---


[link de compartilhamento](https://correiarodrigues.com.br/notas/criptomoedas/documentacao-tecnica/01-visao-geral/arquitetura/)

<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>