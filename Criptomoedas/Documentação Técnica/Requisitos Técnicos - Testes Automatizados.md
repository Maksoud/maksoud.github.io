# 🧪 Requisitos Técnicos - Testes Automatizados

Este documento define os requisitos e escopo dos testes automatizados necessários para garantir o correto funcionamento do sistema Criptoren, com foco na estratégia de negociação, integridade dos dados e robustez da lógica de operação.

---

## 🎯 Objetivos dos Testes

- Verificar o comportamento da estratégia em cenários diversos
- Assegurar que operações não sejam executadas fora das regras
- Garantir integridade das decisões tomadas com base nas cotações

---

## 🧩 Tipos de Testes

### 🔹 Testes Unitários

- Testar funções isoladas do `trade_service.py`, incluindo:
    - `check_buy_opportunity`
    - `check_sell_opportunity`
    - `register_buy`
    - `register_sell`
- Simular entrada de dados com preços variados e validar decisões esperadas

### 🔹 Testes de Estratégia

- Testar lógica completa de:
    - Compra após valorização de X% sobre o fundo
    - Venda após desvalorização Y% com lucro ≥ lucro mínimo
    - Rompimento do canal com venda programada
- Validar campos calculados como `preco_alvo_venda`, `data_saida_canal`, `margem_lucro_minimo`

### 🔹 Testes de Integração

- Simular fluxo completo com WebSocket falso ou mockado
- Verificar integração entre:
    - WebSocket → Estratégia → Banco de Dados
    - Estratégia → API REST → Consulta das operações

### 🔹 Testes de Persistência

- Validar que operações e logs são corretamente gravados
- Garantir consistência após restart da aplicação (ex: posição em aberto continua ativa)

### 🔹 Testes de API

- Testar endpoints `/start`, `/stop`, `/status`
- Testar rotas de consulta de operações e logs com diferentes filtros

---

## 🛠️ Ferramentas Recomendadas

- `pytest` para testes unitários e integração
- `unittest.mock` para simular WebSocket e banco
- `fastapi.testclient` para testes de endpoints

---

## ✅ Benefícios Esperados

- Prevenção de falhas em produção
- Base para refatorações seguras
- Redução do tempo de debug em ambientes reais
- Confiança para operar com capital real

---


<sup><sub>
Criptoren - Renée Maksoud - julho de 2025
</sub></sup>